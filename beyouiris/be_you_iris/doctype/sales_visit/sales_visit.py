# Copyright (c) 2022, Lovin Maxwell and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils.data import cstr

class SalesVisit(Document):
	pass

@frappe.whitelist()
def get_events(start, end, filters=None):
	events = []

	sales_person = frappe.db.get_value("Sales Person", {"user": frappe.session.user})

	# if not sales_person:
	# 	return events

	from frappe.desk.reportview import get_filters_cond
	conditions = get_filters_cond("Sales Visit", filters, [])
	add_sales_visit(events, start, end, conditions=conditions,sales_person = sales_person)
	return events

def add_sales_visit(events, start, end, conditions=None,sales_person = None):
	q_sales_person = ""
	if sales_person:
		q_sales_person = f"and sales_person = '{sales_person}'"
	query = """select name, date, salon_name
		from `tabSales Visit` where
		date between %(from_date)s and %(to_date)s
		%(sales_person)s"""
	if conditions:
		query += conditions

	result = frappe.db.sql(query, {"from_date":start, "to_date":end, "sales_person":q_sales_person}, as_dict=True)
	from beyouiris.utils import beYouLogger
	beYouLogger.debug(result)

	for d in result:
		e = {
			"name": d.name,
			"doctype": "Sales Visit",
			"start": d.date,
			"end": d.date,
			# "title": cstr(d.status),
			"title": cstr(d.salon_name),
			# "docstatus": d.docstatus
		}
		if e not in events:
			events.append(e)
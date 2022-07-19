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

	sales_representative = frappe.db.get_value("Sales Representative", {"user": frappe.session.user})

	# if not sales_representative:
	# 	return events

	from frappe.desk.reportview import get_filters_cond
	conditions = get_filters_cond("Sales Visit", filters, [])
	add_sales_visit(events, start, end, conditions=conditions,sales_representative = sales_representative)
	return events

def add_sales_visit(events, start, end, conditions=None,sales_representative = None):
	q_sales_representative = ""
	if sales_representative:
		q_sales_representative = f"and sales_representative = '{sales_representative}'"
	query = """select name, date, salon_name
		from `tabSales Visit` where
		date between %(from_date)s and %(to_date)s
		%(sales_representative)s"""
	if conditions:
		query += conditions

	result = frappe.db.sql(query, {"from_date":start, "to_date":end, "sales_representative":q_sales_representative}, as_dict=True)
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
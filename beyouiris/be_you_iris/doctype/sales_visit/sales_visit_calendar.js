frappe.views.calendar["Sales Visit"] = {
	field_map: {
		"start": "date",
		"end": "date",
		"id": "name",
		"title": "salon_name",
		"allDay": "allDay"
	},
	filters: [
		{
			"fieldtype": "Link",
			"fieldname": "name",
			"options": "Sales Visit",
			"label": __("Sales Visit")
		}
	],
	gantt: true,
	get_events_method: "frappe.desk.calendar.get_events"
	// options: {
	// 	header: {
	// 		left: 'prev,next today',
	// 		center: 'title',
	// 		right: 'month'
	// 	}
	// },
	// get_events_method: "beyouiris.be_you_iris.doctype.sales_visit.sales_visit.get_events"
}

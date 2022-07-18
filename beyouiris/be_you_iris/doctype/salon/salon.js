// Copyright (c) 2022, Lovin Maxwell and contributors
// For license information, please see license.txt

frappe.ui.form.on('Salon', {
	refresh: function(frm) {
		frm.toggle_display(['address_html','contact_html'], !frm.doc.__islocal);
		frappe.dynamic_link = {doc: frm.doc, fieldname: 'name', doctype: 'Salon'}
		if (frm.doc.__islocal) {
			frm.set_df_property('address_and_contact', 'hidden', 1);
			frappe.contacts.clear_address_and_contact(frm);
		}
		else {
			frm.set_df_property('address_and_contact', 'hidden', 0);
			frappe.contacts.render_address_and_contact(frm);
		}

		if(frm.doc.primary_address == ""){
			frm.trigger("salon_primary_address");
		}
	},

	salon_primary_address: function(frm){
		if(frm.doc.salon_primary_address){
			frappe.call({
				method: 'frappe.contacts.doctype.address.address.get_address_display',
				args: {
					"address_dict": frm.doc.salon_primary_address
				},
				callback: function(r) {
					frm.set_value("primary_address", r.message);
				}
			});
		}
		if(!frm.doc.salon_primary_address){
			frm.set_value("primary_address", "");
		}
	},
	salon_primary_contact: function(frm){
		if(!frm.doc.salon_primary_contact){
			frm.set_value("mobile_no", "");
			frm.set_value("email_id", "");
		}
	},
});

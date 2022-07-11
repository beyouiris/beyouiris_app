import frappe
from frappe.utils.logger import set_log_level

set_log_level("DEBUG")
beYouLogger = frappe.logger("beyou", allow_site=True, file_count=50)
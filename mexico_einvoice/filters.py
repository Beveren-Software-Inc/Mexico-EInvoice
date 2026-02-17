import frappe

# def filter_payment_form(doctype, txt, searchfield, page_len, start, filters):


@frappe.whitelist()
def filter_payment_form(
    doctype: str,
    txt: str,
    searchfield: str,
    page_len: int,
    start: int,
    filters: dict | None = None,
):
    return frappe.db.sql("""select name, description from `tabPayment Form` where enable=1""")

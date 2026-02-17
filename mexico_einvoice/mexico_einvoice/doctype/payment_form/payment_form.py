# Copyright (c) 2023, Beveren-Software-Inc and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class PaymentForm(Document):
    def on_update(self):
        if self.default:
            # query = f""" update `tabPayment Form` set `default` = 0
            # frappe.db.sql(query)
            frappe.db.sql(
                """
                        UPDATE `tabPayment Form`
                        SET `default` = 0
                        WHERE name != %s
                    """,
                (self.name,),
            )

            # Note: frappe.db.commit() removed for v16 compatibility
            # Document hooks cannot commit transactions in v16
            self.reload()

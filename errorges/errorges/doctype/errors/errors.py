# -*- coding: utf-8 -*-
# Copyright (c) 2015, Pau Rosello and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Errors(Document):
	def on_update(self):
            frappe.sendmail(recipients="paurosello@gmail.com, santi@servipro.eu", subject="Error "+ self.titul +" Actualitzat: " + self.estat, message="http://13.80.115.15/desk#Form/Errors/"+self.name+"\n\n\n\n" + self.descripcio, sender="paur@servipro.eu")

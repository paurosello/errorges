# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Errorges",
                        "_doctype":"Errors",
			"color": "red",
			"icon": "octicon octicon-file-directory",
			"type": "link",
                        "link": "List/Errors",
			"label": _("Errors")
		}
	]

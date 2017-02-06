# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "errorges"
app_title = "Errorges"
app_publisher = "Pau Rosello"
app_description = "App to deal with programming errors"
app_icon = "octicon octicon-file-directory"
app_color = "red"
app_email = "paurosello@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/errorges/css/errorges.css"
# app_include_js = "/assets/errorges/js/errorges.js"

# include js, css files in header of web template
# web_include_css = "/assets/errorges/css/errorges.css"
# web_include_js = "/assets/errorges/js/errorges.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "errorges.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "errorges.install.before_install"
# after_install = "errorges.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "errorges.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"errorges.tasks.all"
# 	],
# 	"daily": [
# 		"errorges.tasks.daily"
# 	],
# 	"hourly": [
# 		"errorges.tasks.hourly"
# 	],
# 	"weekly": [
# 		"errorges.tasks.weekly"
# 	]
# 	"monthly": [
# 		"errorges.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "errorges.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "errorges.event.get_events"
# }


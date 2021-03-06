#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '


class MIMEMail(MIMEMultipart):
	def __init__(self, subject, message, exp, from_address=None):
		MIMEMultipart.__init__(self)
		if not from_address:
			from_address = exp["email"]
		self["Subject"] = subject
		self["From"] = from_address

		self.exp = exp

		self.attach(MIMEText(message, "plain", "utf-8"))

		self.mailserver = smtplib.SMTP_SSL(exp["smtp"])

	def sendMails(self, dests):
		self.mailserver.login(self.exp["email"], self.exp["password"])

		self["To"] = COMMASPACE.join(dests)

		self.mailserver.sendmail(self.exp["email"], dests, self.as_string())

		self.mailserver.quit()

	def send(self, dest):

		self.mailserver.login(self.exp["email"], self.exp["password"])
		self["To"] = dest

		self.mailserver.sendmail(self.exp["email"], dest, self.as_string())
		self.mailserver.quit()

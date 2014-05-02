#! /usr/local/bin/python2.7
# -*- coding: utf-8 -*- #

class NrzStore():
	RERhour = None
	RERday = None
	
	def __init__(self):
		self.reinitStorage()

	def reinitStorage(self):
		self.RERhour = None
		self.RERday = None

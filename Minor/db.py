
import re
from parser import Parser_module as Pobj

class Data_base:
	
	def __init__(self, fn_set):
		self.fn_set  = fn_set;
		self.func_db = ["scanf","strcpy","memset","gets"]


	def search_for_vuln_fun(self):
		for a in self.fn_set:
			if self.exist_in_db(a):
				self.add_in_queue(a)

	def exist_in_db(self, func):
		continue

	def add_in_queue(self):
		continue
#Parser Module to load information
#TODO Add exception Module
#perform_analysis return (core,bin), list of functios
import r2pipe
import json

class Parser_module:

	def __init__(self, name):
		#Initialize
		self.name = name
		

	def perform_analysis(self):
		r2 = r2pipe.open(self.name)
		print("[+]Performing Analysis...")
		#TODO Suppress Warnings
		_ = r2.cmd('aaa')
		print("[+] Extracting Information")
		Info_bin = json.loads(self.get_info(r2))
		List_of_fun = json.loads(self.get_func(r2))
		return Info_bin, List_of_fun

	def get_info(self, r_obj):
		x = r_obj.cmd("ij")
		return x

	def get_func(self ,r_obj):
		x = r_obj.cmd("aflj")
		return x
#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from sys import argv as sys_argv, exit as sys_exit, path as sys_path
from os import path as os_path

# IMPORT MODULE MENU #
# UNHASH BELOW 4 LINES IF YOU WANT TO PUT MENU SCRIPT IN OTHER LOCATION AND LOAD IT TO MAIN SCRIPT #
# path_menu = '/path/to/menu/'
# sys_path.append(os_path.dirname(os_path.expanduser(os_path.join(path_menu, 'menu.py'))))
# sys_path.append(os_path.dirname(os_path.expanduser(os_path.join(path_menu, 'menu_text.py'))))
# sys_path.append(os_path.dirname(os_path.expanduser(os_path.join(path_menu, 'menu_signs.py'))))
import menu, menu_text, menu_signs



########################################################################
### BELOW CLASS CONTAINS ALL CONFIG SETTINGS TO BE FULLFILLED BY YOU ###
########################################################################

class MenuConfig(object):

	### BASIC INFO VARIABLES ###
	application_name = 'NAME'
	application_type = 'SCRIPT / APPLICATION'
	additional_application_description = 'Description what your application / scrip does'
	# CONFIGURATION VARIABLES #
	need_second_argument = False # TRUE IF YOU NEED SECOND ARGUMENT EACH TIME FOR EVERY ARGUMEN

	# BELOW PUT LIST OF ARGUMENTS AS DICTIONARY
	# EXAMPLE OF USE:
	# 'ARGUMENT': 'DESCRIPTION',
	letter_for_menu = 'm' # SHOULD NOT BE CHANGED
	need_first_argument = False # TRUE ONLY IF APPLICATION HAVE TO BE LUNCHED WITH ADDITIONAL ARGUMENT EVERYTIME
	argument_list = { 
						'm': 'menu',
						'h': 'help',
						'q': 'quit (only for menu)',
						'a': 'description what your function does'
					}

	# BELOW PUT ARGUMENTS FROM UPPER LIST, WHICH NEED ADDITIONAL ARGUMENT TO BE SPECIFIED
	# SEPARATE ARGUMENTS BY COMMA
	additional_argument_list =  [ ]

	# BELOW REPEAT FROM ARGUMENT_LIST KEY VALUES, WHICH HAVE SUBMENUS AS LIST
	# EXAMPLE:
	# 'ARGUMENT_1': [ELEMENT_1, ELEMENT_2, ELEMENT_3],
	# 'ARGUMENT_2': [ELEMENT_1, ELEMENT_2, ELEMENT_3],
	any_argument_have_submenu = False # TRUE ONLY IF YOU HAVE ARGUMENT, WHICH YOU WANT TO BE PRINTED AS SUBMENU
	submenu_arguments_list =	{ }



############################################################################################
### BELOW CLASS IS YOUR MAIN CLASS TO FULFILL LOGIC IN FUNCTIONS. NAME CLASS AS YOU WANT ###
############################################################################################

class YourClassName(object):

	def your_function(self, argument_list, additional_argument):
		print( ', '.join([ argument_list, additional_argument ]) )




	#########################################################
	### ARGUMENTS - HERE CONNECT ARGUMENTS WITH FUNCTIONS ###
	#########################################################

	def arguments(self, menu_object, argument_list, additional_argument):
		self.menu_object = menu_object
		# BASIC FUNCTIONS #
		if 'm' in argument_list:
			menu_object.menu()
		if 'h' in argument_list:
			menu_object.help()
		if 'q' in argument_list:
			sys_exit( menu_signs.sign_empty.join([ menu_signs.sign_newline, menu_text.close_text, menu_signs.sign_newline ]) )
		# YOUR FUNCTIONS HERE #
		if 'a' in argument_list:
			self.your_function( argument_list, additional_argument )



	############
	### INIT ###
	############

	def __init__(self, argument_list, additional_argument, menu_config):
		menu_addres = menu.Menu(self, argument_list, additional_argument, menu_config)





#####################
### LOAD FUNCTION ###
#####################

def load_arguments():
	try:
		quantity_of_arguments = len(sys_argv)
		first_list_of_arguments = ''
		second_additional_argument = ''
		if quantity_of_arguments > 2:
			first_list_of_arguments = str(sys_argv[1])
			second_additional_argument = ''
			for arg in sys_argv[2:]:
				second_additional_argument += ''.join([ arg, ' ' ])
			second_additional_argument = second_additional_argument.strip( )	
		elif quantity_of_arguments == 2: first_list_of_arguments = str(sys_argv[1])
		
		menu_config = MenuConfig()
		self_main = YourClassName(first_list_of_arguments, second_additional_argument, menu_config)

	except KeyboardInterrupt:
		sys_exit( menu_signs.sign_empty.join([ menu_signs.sign_newline_double, menu_text.error_keyboard_interrupt, menu_signs.sign_newline_double ]) )
	except IndexError as error:
		sys_exit( menu_signs.sign_empty.join([ menu_signs.sign_newline, menu_text.error_index_error, menu_signs.sign_newline_double, str(error), menu_signs.sign_newline_double ]))
	### HASH BELOW 2 LINES IF YOU WANT TO SEE MORE DETAILED INFO ABOUT ERRORS ###
	#except Exception as error:
	#	sys_exit(menu_signs.sign_empty.join([ menu_signs.sign_newline, menu_text.error_other_type_of_error, menu_signs.sign_newline_double, str(error), menu_signs.sign_newline_double ]))




if __name__ == "__main__":
	load_arguments()

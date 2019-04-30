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
	additional_application_description = 'Script created to ease your work with creating scripts - instant menu for them'
	# CONFIGURATION VARIABLES #
	need_second_argument = False # TRUE IF YOU NEED SECOND ARGUMENT EACH TIME FOR EVERY ARGUMEN

	# BELOW PUT LIST OF ARGUMENTS AS DICTIONARY
	# EXAMPLE OF USE:
	# 'ARGUMENT': 'DESCRIPTION',
	letter_for_menu = 'm' # SHOULD NOT BE CHANGED
	need_first_argument = True # TRUE ONLY IF SCRIPT HAVE TO BE LUNCHED WITH ADDITIONAL ARGUMENT EVERYTIME
	argument_list = { 
						'm': 'menu',
						'h': 'help',
						'q': 'quit (only for menu)',
						'a': 'Run function 1 [NEED ADDITIONAL ARGUMENT]',
						'b': 'Run function 2 (additional function goto example)', # ADDITIONAL ARGUMENT LET YOU KNOW IF OPTION WAS CHOOSEN AS ARGUMENT OR FROM MENU
						'c': 'Run function 3 [OPTION HAVE SUBMENU LIST]',
						'd': 'Run function 4',
						'e': 'Run function 5 -add value for c option',
						'f': 'Run function 6 - add values for g option',
						'g': 'this option is only for e function, to show\n    how fullfill from empty list of subarguments'
					}

	# BELOW PUT ARGUMENTS FROM UPPER LIST, WHICH NEED ADDITIONAL ARGUMENT TO BE SPECIFIED
	# SEPARATE ARGUMENTS BY COMMA
	additional_argument_list =  [ 'a' ]

	# BELOW REPEAT FROM ARGUMENT_LIST KEY VALUES, WHICH HAVE SUBMENUS AS LIST
	# EXAMPLE:
	# 'ARGUMENT_1': [ELEMENT_1, ELEMENT_2, ELEMENT_3],
	# 'ARGUMENT_2': [ELEMENT_1, ELEMENT_2, ELEMENT_3],
	any_argument_have_submenu = True # TRUE ONLY IF YOU HAVE ARGUMENT, WHICH YOU WANT TO BE PRINTED AS SUBMENU
	submenu_arguments_list =	{
									'c': [ 'sub-argument 1', 'sub-argument 2', 'sub-argument 3', 'sub-argument 4', 'sub-argumend dupa' ],
									'g': [ ],
								}



############################################################################################
### BELOW CLASS IS YOUR MAIN CLASS TO FULFILL LOGIC IN FUNCTIONS. NAME CLASS AS YOU WANT ###
############################################################################################

class Main(object):

	def function_1(self, argument_list, additional_argument):
		# SIMPLE USAGE OF FUNCTION WITH GIVEN ADDITIONAL ARGUMENT #
		print(menu_signs.sign_empty.join(["\n1. Argument: ", argument_list, "\nAdditional argument: ", additional_argument, "\n"]))

	def function_2(self, argument_list):
		print(menu_signs.sign_empty.join(["\n2. Argument: ", argument_list, "\n"]))
		# RUNNING BELOW FUNCTION WILL GO TO MAIN MANU OR EXIT THE SCRIPT, DEPENDS IF SCRIPT WAS LUNCHED WITH 'm' option or with other argument.
		# ALSO FUNCTION MAY TAKE ADDITIONAL PARAMETER AS IN EXAMPLE BELOW:
		# self.menu_object.goto_exit_or_main_menu( 'Some message passed', menu_text.goto_exit )
		# OR:
		# self.menu_object.goto_exit_or_main_menu( 'Some message passed', menu_text.goto_menu )
		# THEN FUCTION WILL DO CHOOSEN OPERATION: EXIT OR GO TO MAIN MENU
		# IF YOU NOT CHOOSE GOTO_EXIT OR GOTO_MENU THEN IT WILL BE AUTOMATICALLY CHOOSEN DEPENDING HOW WHOLE SCRIPT WAS LUNCHED - WITH ARGUMENT OR FROM MENU
		self.menu_object.goto_exit_or_main_menu( '\nHere you can put your logic.\n' )

	def function_3(self, argument_list, additional_argument):
		# ARGUMENT WITH SUBMENU ARGUMENTS LIST #
		print(menu_signs.sign_empty.join(["\n3. Argument: ", argument_list, "\nAdditional argument: ", additional_argument, "\n"]))

	def function_4(self, argument_list):
		# SIMPLE USAGE OF FUNCTION WITH ONE ARGUMENT #
		file_name = 'menu/menu_text.py'
		file_path = '/some/path/to/file/'
		print(os_path.join(file_path, file_name))
		print(menu_signs.sign_empty.join(["\n4. Argument: ", argument_list, "\n"]))

	def function_5(self):
		value = raw_input('\nPlease enter new sub-argument name: ')
		# EXAMPLE SHOWS HOW DOES THE ADDING VALUE TO SUBMENU FUNCTION WORKS, WITHOUT OMMITING REPEATING VALUES #
		self.menu_object.add_value_to_submenu_arguments(__file__, value, ommit_repeating_values=False,  argument_name='c')

	def function_6(self):
		values = [ 'value 1', 'value 2', 'value 3', 'value 2', 'value 1', 'value 4' ]
		# EXAMPLE SHOWS HOW DOES THE ADDING VALUE TO SUBMENU FUNCTION WORKS, WITH OMMITING REPEATING VALUES #
		for value in values:
			self.menu_object.add_value_to_submenu_arguments(__file__, value, ommit_repeating_values=True, argument_name='g')



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
		# EXAMPLE FUNCTIONS SHOWING HOW SCRIPT WORKS #
		if 'a' in argument_list:
			self.function_1(argument_list, additional_argument)
		if 'b' in argument_list:
			self.function_2(argument_list)
		if 'c' in argument_list:
			self.function_3(argument_list, additional_argument)
		if 'd' in argument_list:
			self.function_4(argument_list)
		if 'e' in argument_list:
			self.function_5()
		if 'f' in argument_list:
			self.function_6()
		if not argument_list: # WORKS ONLY WHEN VARIABLE need_first_argument SET TO False
			print('\nNothing choosed\n')



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
		self_main = Main(first_list_of_arguments, second_additional_argument, menu_config)

	except KeyboardInterrupt:
		sys_exit( menu_signs.sign_empty.join([ menu_signs.sign_newline_double, menu_text.error_keyboard_interrupt, menu_signs.sign_newline_double ]) )
	except IndexError as error:
		sys_exit( menu_signs.sign_empty.join([ menu_signs.sign_newline, menu_text.error_index_error, menu_signs.sign_newline_double, str(error), menu_signs.sign_newline_double ]))
	### HASH BELOW 2 LINES IF YOU WANT TO SEE MORE DETAILED INFO ABOUT ERRORS ###
	#except Exception as error:
	#	sys_exit(menu_signs.sign_empty.join([ menu_signs.sign_newline, menu_text.error_other_type_of_error, menu_signs.sign_newline_double, str(error), menu_signs.sign_newline_double ]))




if __name__ == "__main__":
	load_arguments()

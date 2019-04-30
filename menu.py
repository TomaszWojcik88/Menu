#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from sys import exit as sys_exit
import menu_text, menu_signs


class Menu(object):

	####################
	### PRESENTATION ###
	####################

	def print_name(self):
		print( menu_signs.sign_empty.join([ menu_signs.sign_newline, self.menu_config.application_type.upper(), menu_signs.sign_space, self.menu_config.application_name.upper(), menu_signs.sign_newline,
						menu_signs.sign_separating*( len(self.menu_config.application_type) + len(self.menu_config.application_name) + 1 ), menu_signs.sign_newline ]) )

	def app_info(self):
		print( menu_signs.sign_empty.join([ self.menu_config.additional_application_description, menu_signs.sign_newline,
						menu_signs.sign_separating*( len(self.menu_config.application_type) + len(self.menu_config.application_name) + 1 ), menu_signs.sign_newline ]) )

	def iterate_arguments(self):
		key_list = list(self.menu_config.argument_list.keys())
		argument_list = self.menu_config.argument_list
		key_list.sort()
		for key in key_list:
			print( menu_signs.sign_minus_separator.join([key, argument_list[key]]) )



	############
	### HELP ###
	############

	def help(self):
		if self.if_lunched_from_init:
			self.print_name()
		self.app_info()
		if self.if_lunched_from_init:
			self.iterate_arguments()
			sys_exit( menu_signs.sign_empty.join([ menu_signs.sign_newline, menu_text.close_text, menu_signs.sign_newline ]) )
		elif self.if_lunched_from_init == False:
			self.menu()



	#######################
	### CHECK ARGUMENTS ###
	#######################

	def check_arguments(self):
		# REMOVE '-' SIGN FROM FIRST ARGUMENT #
		if self.arguments_list:
			self.arguments_list = self.arguments_list.replace( menu_signs.sign_minus, menu_signs.sign_empty )
		# IF EVEN ONE ARGUMENT NOT GIVEN BUT FIRST ARGUMENT NEED #
		if self.menu_config.need_first_argument:
			if not self.arguments_list:
				if self.if_lunched_from_init:
					print( menu_signs.sign_empty.join([ menu_signs.sign_newline, menu_text.no_first_argument_given_text, menu_signs.sign_newline ]) )
					self.help()
				elif not self.if_lunched_from_init:
					print( menu_signs.sign_empty.join([ menu_signs.sign_newline, menu_text.no_first_argument_given_text, menu_signs.sign_newline ]) )
					self.menu()
		# IF GIVEN FIRST ARGUMENT NOT IN POSSIBLE ARGUMENT LIST #
		possible_arguments_list = list(self.menu_config.argument_list.keys())
		for argument in self.arguments_list:
			if argument not in possible_arguments_list:
				if self.if_lunched_from_init:
					print( menu_signs.sign_empty.join([ menu_signs.sign_newline, menu_text.not_found_argument_text, menu_signs.sign_newline ]) )
					self.help()
				elif not self.if_lunched_from_init:
					print( menu_signs.sign_empty.join([ menu_signs.sign_newline, menu_text.not_found_argument_text, menu_signs.sign_newline ]) )
					self.menu()
		# ADDITIONAL ARGUMENT CHECK IF EXIST #
		if self.menu_config.need_second_argument:
			if not self.additional_argument:
				if self.if_lunched_from_init:
					print( menu_signs.sign_empty.join([ menu_signs.sign_newline, config_text.this_app_always_need_second_argument, menu_signs.sign_newline ]) )
					self.help()
				elif not self.if_lunched_from_init:
					print( menu_signs.sign_empty.join([ menu_signs.sign_newline, menu_text.no_second_argument_given_text, menu_signs.sign_newline, ]) )
					self.menu()
		# ADDITIONAL ARGUMENT CHECK FOR ARGUMENTS THAT NEED ADDITIONAL ARGUMENT #
		for argument in self.arguments_list:
			if any(argument in additional_argument for additional_argument in self.menu_config.additional_argument_list):
				if not self.additional_argument:
					if self.if_lunched_from_init:
						print( menu_signs.sign_empty.join([ menu_signs.sign_newline, menu_text.no_second_argument_given_text, menu_signs.sign_newline, ]) )
						self.help()
					elif not self.if_lunched_from_init:
						print( menu_signs.sign_empty.join([ menu_signs.sign_newline, menu_text.no_second_argument_given_text, menu_signs.sign_newline, ]) )
						self.menu()
		# ARGUMENTS WHICH HAVE LIST TO BE PRINTED AS SUBMENU #
		if self.menu_config.any_argument_have_submenu:
			key_submenu_list = list(self.menu_config.submenu_arguments_list.keys())
			for argument in self.arguments_list:
				if any(argument in key_submenu for key_submenu in key_submenu_list):
					additional_arguments_list = self.menu_config.submenu_arguments_list[argument]
					if self.additional_argument:
						if any(self.additional_argument == additional_argument_possible for additional_argument_possible in additional_arguments_list):
							self.main.arguments(self, self.arguments_list, self.additional_argument)
							if self.if_lunched_from_init:
								sys_exit( menu_signs.sign_empty.join([ menu_signs.sign_newline, menu_text.close_text, menu_signs.sign_newline ]) )
							elif not self.if_lunched_from_init:
								self.menu()
						else:
							print( menu_signs.sign_empty.join([ menu_signs.sign_newline, menu_text.second_argument_not_found_on_submenu_list, menu_signs.sign_newline ]) )
							for number, argument in enumerate(additional_arguments_list):
								print( menu_signs.sign_dot.join([ str(number+1), str(argument) ]) )
							if self.if_lunched_from_init:
								sys_exit( menu_signs.sign_empty.join([ menu_signs.sign_newline, menu_text.close_text, menu_signs.sign_newline ]) )
							elif not self.if_lunched_from_init:
								self.menu()
					elif not self.additional_argument:
						if self.if_lunched_from_init:
							print( menu_signs.sign_empty.join([ menu_signs.sign_newline, menu_text.second_argument_not_exist_at_all,
									menu_signs.sign_newline, menu_text.submenu_list, menu_signs.sign_newline ]) )
							for number, argument in enumerate(additional_arguments_list):
								print( menu_signs.sign_dot.join([ str(number+1), str(argument) ]) )
							sys_exit( menu_signs.sign_empty.join([ menu_signs.sign_newline, menu_text.close_text, menu_signs.sign_newline ]) )
						elif not self.if_lunched_from_init:
							self.submenu(argument)

	def submenu(self, argument):
		subarguments = self.menu_config.submenu_arguments_list[argument]
		while True:
			print( menu_signs.sign_empty.join([ (len(menu_text.choosen_menu_option)*menu_signs.sign_separating), menu_signs.sign_newline, menu_text.choosen_menu_option, argument,
							menu_signs.sign_minus_separator, self.menu_config.argument_list[argument], menu_signs.sign_newline,
							menu_signs.sign_newline, menu_text.submenu_choose_one_option_text, menu_signs.sign_newline ]) )
			for number, subargument in enumerate(subarguments):
				print( menu_signs.sign_dot.join([ str(number+1), subargument ]) )
			print(menu_text.come_back_to_main_menu)
			submenu_choosen_digit = raw_input( menu_signs.sign_empty.join([ menu_signs.sign_newline, menu_text.submenu_choosen_option_text ]) )
			if submenu_choosen_digit == self.menu_config.letter_for_menu:
				self.menu()
			if submenu_choosen_digit.isdigit():
				submenu_choosen_digit = int(submenu_choosen_digit)-1
				if submenu_choosen_digit >= 0 and submenu_choosen_digit < (len(subarguments)):
					self.additional_argument = subarguments[submenu_choosen_digit]
					self.main.arguments(self, self.arguments_list, self.additional_argument)
				else:
					print( menu_signs.sign_empty.join([ menu_signs.sign_newline, menu_text.submenu_option_out_of_list, menu_signs.sign_newline ]) )
			else: print( menu_signs.sign_empty.join([ menu_signs.sign_newline, menu_text.given_option_is_not_digit, menu_signs.sign_newline ]) )



	############
	### MENU ###
	############

	def menu(self):
		self.print_name()
		while True:
			self.arguments_list = ''
			self.additional_argument = ''
			print( menu_signs.sign_empty.join([ menu_signs.sign_newline, menu_text.menu_choose_one_option_text, menu_signs.sign_newline ]) )
			self.iterate_arguments()
			argument_list_string = ( raw_input( menu_signs.sign_empty.join([ menu_signs.sign_newline, menu_text.menu_choosen_option_text ]) ) )
			if len(argument_list_string) == 0:
				if not self.menu_config.need_first_argument:
					self.main.arguments(self, self.arguments_list, self.additional_argument)
				print( menu_signs.sign_empty.join([ menu_signs.sign_newline, menu_text.no_option_choosed, menu_signs.sign_newline ]) )
				self.menu()
			argument_list_array = argument_list_string.split( )
			self.arguments_list = argument_list_array[0]
			if len(argument_list_array) > 1:
				additional_argument = ''
				for additional in argument_list_array[1:]:
					additional_argument += ''.join([ additional, ' ' ])
				additional_argument = additional_argument.strip( )	
				self.additional_argument = additional_argument
			self.if_lunched_from_init = False
			self.check_arguments()
			self.main.arguments(self, self.arguments_list, self.additional_argument)



	############################
	### ADDITIONAL FUNCTIONS ###
	############################

	### ADD VALUE TO LIST OF CHOOSEN SUBMENU ARGUMENT ###
	def add_value_to_submenu_arguments(self, main_file_name, value, ommit_repeating_values, argument_name):
		# CREATE NEW LIST WITH ADDED VALUE #
		submenu_arguments = self.menu_config.submenu_arguments_list[argument_name]
		# CHECK IF VALUE ALLREADY EXIST AND OMMIT ADDING IF REQUESTED #
		if any( value == element for element in submenu_arguments ) and ommit_repeating_values:
			pass
		# IF OMMIT NOT REQUESTED #
		else:
			submenu_arguments.append(value)
			submenu_arguments = ''.join([ menu_signs.sign_tabulator*9, "'", str(argument_name), "': [ '", "', '".join(submenu_arguments), "' ]," ])
			# CREATE LIMMITED LIST 
			searched_value = ''.join([ menu_signs.sign_tabulator*9, "'", str(argument_name), "': [" ])
			file_content = list()
			with open(main_file_name) as file:
				file_content = file.readlines()
			file_new_content = ''
			for line in file_content:
				if searched_value in line:
					if '}' in line:
						file_new_content += ''.join([ submenu_arguments, ' }', menu_signs.sign_newline ])
					else:
						file_new_content += ''.join([ submenu_arguments, menu_signs.sign_newline ])
				else:
					file_new_content += line
			with open(main_file_name, 'w') as file:
				file.write(file_new_content)


	### GO: TO EXIT OR BACK TO MAIN MENU ###
	def goto_exit_or_main_menu(self, return_message, choosen_exit_or_menu=False):
		if choosen_exit_or_menu:
			if choosen_exit_or_menu == menu_text.goto_exit:
				sys_exit(return_message)
			elif choosen_exit_or_menu == menu_text.goto_menu:
				print(return_message)
				self.menu()
			else:
				sys_exit(''.join([ menu_signs.sign_newline_double, menu_text.menu_error, menu_signs.sign_newline, menu_text.choosen_option_not_recognized,
									menu_signs.sign_newline,	menu_text.please_use_one_of_options, menu_signs.sign_newline, menu_text.goto_exit,
									menu_signs.sign_newline,	menu_text.goto_menu, menu_signs.sign_newline_double ]))
		elif not choosen_exit_or_menu:
			if self.if_lunched_from_init:
				sys_exit(return_message)
			elif not self.if_lunched_from_init:
				print(return_message)
				self.menu()





	############
	### INIT ###
	############

	def __init__(self, main, argument_list, additional_argument, menu_config):
		self.menu_config = menu_config
		self.main = main
		self.arguments_list = argument_list
		self.additional_argument = additional_argument
		self.if_lunched_from_init = True
		self.check_arguments()
		if self.menu_config.letter_for_menu in self.arguments_list:
			self.menu()
		else:
			main.arguments(self, self.arguments_list, self.additional_argument)

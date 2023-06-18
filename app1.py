Telephone_book = {'Rahaf': '0546771330', 'Waleed': '0554258100', 'Sharefh': '0554943200'}
sir_madam_name = input("Please enter your name : ")

def display_menue():
	print("\nHello , Good evening " + sir_madam_name + "\n")
	print("**************\tTelephone Book Menue\t**************\n\n")
	print("1) Display Telephone Book\n"
		  "2) Display Number\n"
		  "3) Display Name\n"
		  "4) Add User\n"
		  "5) Done \n")
	choice = input("please choose an number : ")

	if choice == "1":
		print("\n----------------------------------------------------")
		display_Telephone_book()
	elif choice == "2":
		print("\n----------------------------------------------------")
		display_number()
	elif choice == "3":
		print("\n----------------------------------------------------")
		display_name()
	elif choice == "4":
		print("\n----------------------------------------------------")
		add_user()
	elif choice == "5":
		print("\n----------------------------------------------------")
		end_process()
	else:
		print("This is invalid number")

def display_menue_again():
	print("----------------------------------------------------\n\n")
	print("**************\tTelephone Book Menue\t**************\n\n")
	print("1) Display Telephone Book\n"
		  "2) Display Number\n"
		  "3) Display Name\n"
		  "4) Add User\n"
		  "5) Done \n")
	choice = input("please choose an number : ")

	if choice == "1":
		print("\n----------------------------------------------------")
		display_Telephone_book()
	elif choice == "2":
		print("\n----------------------------------------------------")
		display_number()
	elif choice == "3":
		print("\n----------------------------------------------------")
		display_name()
	elif choice == "4":
		print("\n----------------------------------------------------")
		add_user()
	elif choice == "5":
		print("\n----------------------------------------------------")
		end_process()
	else:
		print("This is invalid number")


def display_Telephone_book():
	print(Telephone_book)
	display_menue_again()

def add_user():
	number_of_users = int(input("home many users you want to add : "))

	for x in range(number_of_users):
		name = input("Please enter your name : ")  # key
		phone_Number = input("Please enter your phone number : ")  # vlaue
		Telephone_book[name] = phone_Number

	print(Telephone_book)
	display_menue_again()

def display_number():
	name = input("please enter the name ")
	if name in Telephone_book:
		print(Telephone_book[name])


	else:
		print("Sorry, the name is not found ")

	display_menue_again()

def display_name():
	phone_Number = input("please enter the phone number ")
	if phone_Number in Telephone_book:
		print(Telephone_book.keys(phone_Number))

	else:
		print("Sorry, the number is not found ")

	display_menue_again()


def end_process():
	print("Thank you for time ! ")



display_menue()







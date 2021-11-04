menu = ""

while menu != '1' or menu != '2':
	menu = input("What would you like to do?"
		"\n1. Input new password"
		"\n2. View saved password"
		"\n3. Exit\n")
	if menu == '1':
		software_or_website_name = input("Enter the name of software/website: ")
		username = input("Enter your username: ")
		password = input("Enter new password: ")
		file = open("data.txt", "a")
		file.write(software_or_website_name+";|"+username+";|"+password+"\n")
		file.close()
	
	if menu == '2':
		file = open("data.txt", "r")
		print("Software\tUsername\tPassword")
		for i in file:
			data = i.split(";|")
			print(data[0]+"\t\t"+data[1]+"\t\t"+data[2])

	if menu == '3':
		exit()
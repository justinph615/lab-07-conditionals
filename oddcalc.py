

firstnum = int(float(input("Give me a number: ")))
secondnum = int(float(input("Give me another number: ")))
operation = float(input("What operation do you want? (mul/div/mod) "))


if operation == "mul"or operation == "MUL":
		
			print(float(firstnum) * float(secondnum))


elif operation == "div" or operation == "DIV":


		print(int(firstnum) / int(secondnum))


		 
elif operation == "mod" or operation == "MOD":


		
		print(int(firstnum) % int(secondnum))


else: 
		print("*** invalid operation")


		



	
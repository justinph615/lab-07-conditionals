import datetime


now = datetime.datetime.now()
print(now.year, now.month, now.day, now.hour, now.minute, now.second)


#usertime = input(now.hour)

if  now.hour <= 5:

	print("It's early!")


elif now.hour <= 7:

	print("Wake up!")


elif now.hour <= 9:

	print("Time for work!")

elif now.hour <= 12:

	print("You should be working!")



elif now.hour <= 13:

	print("Take your lunch break!")


elif now.hour <= 17:

	print("Do you feel that afternoon lull?")
	

elif now.hour <= 19:

	print("Time to hit the gym…")


elif now.hour <= 21:

	print("Gotta eat that dinner")


elif now.hour <= 23:

	print("Get that SLEEP. And rePEAT!")


else: 
		
	print("Check back later")


		



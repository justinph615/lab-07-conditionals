myFirstQuestion = input("What is your answer to my 1st question? (yes/no) ")  
if myFirstQuestion == "yes":
  mySecondQuestion = input("What is your answer to my 2nd question? (yes/no) ")
  if mySecondQuestion == "yes":
    print("Great. You answered both questions")
  elif mySecondQuestion == "no":
    print("You only said yes to my 1st question")
  else:
    print("Answer my question! You didn't type yes or no.")
elif myFirstQuestion == "no":
  print("You answered no to my first question.")
else:
  print("You didn't type yes or no.")
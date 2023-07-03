#write a python program to calculate the ticket price for a movie theatre based on the age of the customer.
#0-5 years Free
#6-12 500
#13-17 1000
#18+ 1500
Age=int(input("Enter Age"))
if Age >= 0 and Age <= 5:
    print("Free")
elif Age >= 6 and Age <= 12:
    print("KES 500")
elif Age >= 13 and Age <= 17:
    print("KES 1,000")
elif Age >= 18 and Age <= 40:
    print("KES 1,500")
else:
    print("Wrong input")
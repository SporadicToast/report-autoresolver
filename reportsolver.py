import os
os.system ("title Report Autoresolver")
os.system ("cls")
print ("Welcome to the Report Autosolver")
print ("Current build : Final Product Build - Public Alpha Release")
print ("Coded and Programmed by Marc Macaraeg") 
print ("Advanced Microsystems and Computers Incorporated (AMAC)")
print ("")
print ("Press any key to continue.")
os.system ("PAUSE >NUL")

#setvar
os.system ("cls")
reportvalue = 1
valuefromsg = 0.0
valuefromprevrep = 0.0
valuefrommisc = 0.0
valuefromdiscr = 0.0
valuefromsucrep = 0.0
totalreports = 0
valuesaveprev = 0.0
totalsolve = 0.0
prevrep = 0
actualcash = 0.0
finalamount = 0.0	
totalreports = int(input("How many reports are we to do? : "))
PreviousDetect = False
setshift = "C"
currentprev = 0.0
#date/month
month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
setmonth = int(input("Enter the numeral of the current month : "))
daysmonth = month[setmonth]
setday = int(input("What is the reportdate? : "))
setshift = str(input("What is the shift? A for morning, C for evening : "))

print ("Current date is (MM/DD/Shift) ", setmonth, "/", setday, "-", setshift)
os.system("PAUSE")
while reportvalue <= totalreports:
	os.system("cls")
	print ("Current date is (MM/DD/Shift) ", setmonth, "/", setday, "-", setshift)
	print ("Input Values	-	Report ", reportvalue, "of ", totalreports)
	print ("")
	valuefromsg = float(input("Enter the Value from ServerGuard itself : "))
	if valuefromsg == 0.0:
		print("")
		print("The day had no report. Inputting 0 to all remaining remarks")
		valuesaveprev = 0.0
		print("")
	else:	
		if PreviousDetect == False:
			valuefromprevrep = float(input("Enter the amount decreased by previous report : "))
		else: 
			print("Previous reports state that the value from previous is ", valuesaveprev)
		valuefrommisc = float(input("Enter the value from misc. purchases : "))
		valuefromdiscr = float(input("Enter the value of discrepancy if any : "))
		valuefromsucrep = float(input("Enter the value added from the suceeding report : "))
		print("")
		actualcash = float(input("Enter the actual cash recieved. : "))
		
		
		os.system("cls")
		print ("Current date is (MM/DD/Shift) ", setmonth, "/", setday, "-", setshift)
		print("")
		print("     ", valuefromsg, "    --- Value from Serverguard")
		if PreviousDetect == True:
			currentprev = valuesaveprev
		else:
			currentprev = valuefromprevrep
		if PreviousDetect == True:
			print("-    ", valuesaveprev, "    --- Value from previous report. (Detected)")
		else:
			print("-    ", valuefromprevrep, "    --- Value from previous report.(NotDetected)")
			PreviousDetect = True
		print("+    ", valuefrommisc, "    --- Value from misc")
		print("+-   ", valuefromdiscr, "    --- Value from discrepancy")
		print("+    ", valuefromsucrep, "     --- Value from next report")
		print("______________________")

		totalsolve = valuefromsg - currentprev + valuefrommisc + valuefromdiscr + valuefromsucrep
		print("     ", totalsolve)
		finalamount = actualcash - totalsolve 
		print("-    ", actualcash, "     --- Actual recieved")
		print("______________________")
		print("     ", finalamount, "     --- Indicates if excess + or short -")
		valuesaveprev = valuefromsucrep
		print("")
	reportvalue +=1
	print("Press any key to continue to the next, current count is", reportvalue, "/", totalreports)
	if setshift =="A":
		setshift = "C"
	else:
		setshift = "A"
		setday +=1
	if setday > daysmonth:
		setmonth +=1
		setday = 1	
		if setmonth > 12:
			setmonth = 1
			daysmonth = month[setmonth]
		else:
			daysmonth = month[setmonth]

	os.system("PAUSE >NUL")
else:
	os.system("cls")
	print("A total of ", totalreports, "solved. Restart the system to perform the operation again.")

os.system ("PAUSE >NUL")		
# Import
import math
from math import *

# Colours
RED = "\033[31m" # Wrong 
WHITE = "\033[37m" # Enter a ...:
GREEN = "\033[32m" # Decision points / commands
ORANGE = "\033[33m" # Header / footer
CYAN = "\033[36m" # Input
PURPLE = "\033[0;35m" # Output question
YELLOW = "\033[1;33m" # Error
BLUE = "\033[0;34m" # Output answer

memory = 0

# PI
PI = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989"

def headerFooter():
	print(ORANGE + "\n--------------------------------------------------- \n \n \n \n " + WHITE)

#-------------------------------------------------------------

def getNumber(): # makes parameter False
	return getNumberActual(False) 

def getNumberMean(): # makes parameter True
	return getNumberActual(True)

def getNumberActual(end): # Gets an input number and checks if it is a number (returns str)
	a = "test"
	a1 = isfloat(a) # a1 can change, a stays constant
	while a1 != True:
		a = input( WHITE + "Enter a number: " + CYAN) # Input 
		if a == "mem":
			return memory
		if end == True:
			if a == "end": # Checks if input is a command ("end") and skips verification
				return "end"
		if not a: # Check if ""
			a = "test2"
		if a.count("/") == 1: # Count the number of /
			a = fractionToDecimal(a) # Fraction to decimal
		a1 = isfloat(a) # Check if it is a float
		if a1 != True:
			print(YELLOW + "Not a number") # error statement 
	return a

def fractionToDecimal(a): # Converts a fraction to a float (returns str(float)/test)
	splitAt = a.index("/") # Find the /
	l, r = a[:splitAt] , a[splitAt:] # split at /
	r = r[1:] # Remove / from right half
	if isfloat(l) == False: # Check if l half is float
		return "test3"
	elif isfloat(r) == False: # Check if r half is float
		return "test4"
	elif float(r) == 0.0:
		print(RED + "Stop trying to break the calculator")
		return "test5"
	else:
		a = (float(l) / float(r)) # divide l by r
		return str(a)

def isfloat(num): # Check if float (returns True/False)
  try:
    float(num)
    return True
  except ValueError:
     return False

def isint(num): # Check if int (returns True/False)
	try:
		int(num)
		return True
	except ValueError:
		return False

# ------------------------------------------------------

def getInteger():
	num = "test"
	while isint(num) == False:
		num = input(WHITE + "Enter an integer: " + CYAN)
	return num
		
# -------------------------------------------------------

def getMultiplier():
	print(GREEN + "Enter an integer that you want to the number to be multiplied by.")
	multiplier = getInteger()
	return multiplier

# -------------------------------------------------------

def getDecimalNumber():
	num = getInteger()
	return str(num)

def getHexNumber():
	print(GREEN + "\nEnter a hexidecimal number. ")
	loop = True
	while loop == True:
		num =input(WHITE + "Enter a number: " + CYAN)
		try:
			hexToDecimal(num)
			loop = False
		except ValueError:	
			loop = True
			print(ORANGE + "Not a hex number" )
	return str(num)

def getBinaryNumber():
	print(GREEN + "\nEnter a binary number. ")
	loop = True
	while loop == True:
		num = input(WHITE + "Enter a number: " + CYAN)
		try:
			x = binaryToHex(num)
			x = hexToBinary(x)
			num = expandBinary(num)
			loop = False
			if x != num:
				loop = True
				print(ORANGE + "Not a Binary number.")
			if x == "":
				loop = True
				print(ORANGE + "Not a Binary number.")				
		except ValueError:
			loop = True
			print(ORANGE + "Not a Binary number")
	num = shortenBinary(num)
	num = expandBinary(num)
	return str(num)

# ----------------------------

def shortenBinary(x): # removes all 0s from the front of a number
	while x[0] == "0": # while the first number = 0
		x = x[1:] # romove the first number
	return x

def expandBinary(binary): # expands a binary number so that it is a multiple of 4 long by adding 0s on the front
	length = len(binary)
	numOfBinPos = (math.ceil(length/4)) * 4 # number of binary positions needed = current length / 4 rounded up * 4
	addNeeded = numOfBinPos - length # amount of 0s needed = number of binary positions needed - current length
	for i in range(addNeeded):
		binary = "0" + binary # adds the required number of 0s to the front
	return binary

#--------------------------------------------------------

def getMeanNumbers(): # returns a list of numbers
	list = [] # creates the list
	input = 0
	print(GREEN + "\nEnter 'end' when you have finished entering numbers")
	while input != "end":
		input = str(getNumberMean())
		if input != "end":
			list.append(input) # adds the last inputed number to the list
	return list

def calcMean(list): # adds the numbers in a list together and find the mean 
	total = 0
	length = len(list)
	for i in range(length):
		total = total + float(list[i]) # adds up all numbers in the list
	avg = total / length # divides total by number of numbers
	return(avg)

# ------------------------------------------------------

def stopping(menu,memory): # Takes a type of menu (str) returns("menu"/"")
	if memory == True:
		saveToMemory()
	stop = "test"
	print(GREEN + "\nEnter 'm' to go back to the", str(menu) + ". \nPress enter to continue.")
	while stop not in ["m",""]: # Check input
		stop = input(WHITE + "Enter a choice: " + CYAN) # Input
	return stop

def sq(a): # squares parameter
	return a*a

# --------------------------------------------------

def saveToMemory(): # asks you if you want to save a number and if yes then it asks you to enter a number to save to memory
	print(GREEN + "\nEnter a number to save it to memory. Press Enter to continue without saving anything to memory")
	x = getFloatOrEnter()
	global memory # makes 'memory' refence a global variable
	if x != "": # if x is a float then it gets saved to memory
		memory = str(x)

def getFloatOrEnter(): # gets a float or nothing 
	x = input(WHITE + "Enter a number or press Enter: " + CYAN)
	floatOrBlank = isfloat(x) # if the input is a float then loop = False (floatOrBlank = True)
	if x == "": # if the input is Enter then loop = False
		floatOrBlank = True
	while floatOrBlank != True: # loops to make x either a float or Enter
		print(ORANGE + "Not a valid input.")
		x  = input(WHITE + "Enter a number or press Enter: " + CYAN)
		floatOrBlank = isfloat(x)
		if x == "":
			floatOrBlank = True
	return x # returns float or blank

#-------------------------------------------------------------

def add(a,b):
	return a + b

def sub(a,b):
	return a - b

def mult(a,b):
	return a * b

def div(a,b):
	if b == 0:
		print(RED + "Stop trying to break the calculator")
		return "undefined"
	return a/b

def getTwoNumbers(): # gets 2 inputs , (returns float a,b)
	print(GREEN + "\nEnter your first number." )
	a = float(getNumber())
	print(GREEN + "\nEnter your second number.")
	b = float(getNumber())
	return a,b

def getOperator(): # gets an operator (returns str op)
	op = "test"
	print(GREEN + "\nEnter an operator (+,-,*,/): ")
	while op not in ["/","+","*","-"]: # check input
		op = input(WHITE + "Enter a choice: " + CYAN)
		if op not in ["/","+","*","-"]:
			print(YELLOW + "Not a valid operator")
	return op

def getAnswer(a,b,op): # takes a,b,op - finds what the operator is - returns answer (float)
	if op == "+":
		return add(a,b)
	elif op == "-":
		return sub(a,b)
	elif op == "*":
		return mult(a,b)
	elif op == "/":
		return div(a,b)
	else:
		return "error"

def getSum(): # Combines getTwoNumbers and getOperator
	a,b = getTwoNumbers()
	op = getOperator()
	return a,b,op

def outputAnswer(a,b,op,answer): # prints basic calculation in the form (a op b = ans)
	print("\n" + PURPLE + str(a), str(op), str(b), "= " + BLUE + str(answer))

def basicCalculator(): # combines all basicCalculator subroutines
	stop = "test"
	while stop != "m": # loop / menu
		a,b,op = getSum()
		answer = getAnswer(a,b,op)
		outputAnswer(a,b,op,answer)
		stop = stopping("main menu",True) # loop / menu

#-------------------------------------------------------------------

def getDiameter(): # gets diameter returns float
	print( GREEN + "\nEnter a diameter.")
	return float(getNumber())

def getArcAngle(): # gets diameter returns float
	print(GREEN + "\nEnter an arc angle.")
	return float(getNumber())

def getRadius(dia): # dia to radius - returns float
	return dia/2

def getCircumference(dia): # dia to circumference - returns float
	return dia * 3.14159

def getArea(dia): # dia to area - return float
	radius = dia/2
	return radius * radius * 3.14159

def getArcLen(dia,arc): # dia + arcAngle to arc len - returns float
	circum = dia * 3.14159
	return circum * (arc/360)

def getArcArea(dia,arc): # dia + arcAngle to arc area - returns float 
	radius = dia/2
	area = radius * radius * 3.14159
	return area * (arc/360)

def getCircleAnswerFull(): # gets dia + arc angle   finds all properties - returns float dia, arc, rad, circ, area, arcLen, arcArea
	dia,rad,circ,area = getCircleAnswerPart()
	arc = getArcAngle()
	arcLen = getArcLen(dia,arc)
	arcArea = getArcArea(dia,arc)
	return dia,arc,rad,circ,area,arcLen,arcArea

def getCircleAnswerPart(): # gets dia   finds some properties - returns float dia, rad, circ, area
	dia = getDiameter()
	rad = getRadius(dia)
	circ = getCircumference(dia)
	area = getArea(dia)
	return dia,rad,circ,area

def fullOrPartCircle(): # asks what inputs you have returns 1 or 2
	print(GREEN + "\nEnter 1 if you have a diameter and an arc angle. Enter 2 if you only have a diameter.")
	choice = "test"
	while choice not in ["1","2"]: # check if 1 or 2
		choice = input(WHITE + "Enter a choice: " + CYAN)
		if choice not in ["1","2"]:
			print(YELLOW + "Not a valid choice. ")
	return choice

def outputCircleFull(dia,arc,rad,circ,area,arcLen,arcArea): # takes float dia, arc, rad, circ, area, arcLen, arcArea - outputs them
	outputCirclePart(dia,rad,circ,area)
	print(PURPLE + "The arc angle is: " + BLUE + str(arc))
	print(PURPLE + "The arc length is: " + BLUE + str(arcLen))
	print(PURPLE + "The sector area is: " + BLUE + str(arcArea))

def outputCirclePart(dia,rad,circ,area): # takes float dia, rad, circ, area - outputs them
	print(PURPLE + "\nThe diameter is: " + BLUE + str(dia))
	print(PURPLE + "The radius is: " + BLUE + str(rad))
	print(PURPLE + "The circumference is: " + BLUE + str(circ))
	print(PURPLE + "The area is: " + BLUE + str(area))

def circleCalculator(): # combines all circleCalculator subroutines ; can do full or partr circle 
	stop = "test"
	while stop != "m": # loop / menu
		choice = fullOrPartCircle()
		if choice == "1": # checks if they chose full circle
			stop = "test"
			while stop != "m": # loop / secondary menu
				dia,arc,rad,circ,area,arcLen,arcArea = getCircleAnswerFull() # gets all values
				outputCircleFull(dia,arc,rad,circ,area,arcLen,arcArea) # outputs all values
				stop = stopping("full or part circle menu",True) # loop / secondary menu
		else:
			stop = "test"
			while stop != "m": # loop / secondary menu
				dia,rad,circ,area = getCircleAnswerPart()
				outputCirclePart(dia,rad,circ,area)
				stop = stopping("full or part circle menu",True) # loop / secondary menu
		stop = stopping("main menu",False) # loop / menu

# ---------------------------------------------------------------------------

def quadraticFormula(a,b,c): # takes values for a,b,c and uses quadratic formula to find the x values returns (float(x1),float(x2)) or str Does not cross x axis *2
	discriminant = sq(b) - (4*a*c) # bit inside the square root of the quadratic formula
	if discriminant < 0: # checks if discriminant is less than 0 
		return "Does not cross x axis." , "Does not cross x axis"
	else: # rest of the quadratic formula
		x1 = (-b+sqrt(discriminant))/(2*a) 
		x2 = (-b-sqrt(discriminant))/(2*a)
		return x1 , x2

def convertQuadratic(a,b,c,d): # converts (ax+b)(cx+d) to ax^2 + bx + c returns float (a,b,c)
	P1 = (a*c) 
	P2 = ((b*c) + (d*a))
	P3 = (b*d)
	return P1, P2, P3

def turningPoint(a,b,c): # takes quadratic (a,b,c) returns mid,min
	mid = -b/(2*a) # finds mid point
	min = ( (a * sq(mid)) + (b*mid) + c ) # puts mid point back into quadratic to find min
	return mid,min

def outputQuadratic(a,b,c,x1,x2,TPx,TPy): # outputs quadratic, x intercepts, y intercept, turning point
	print("\n" + PURPLE + str(a) + "x^2 + " + str(b) + "x + " + str(c))
	print(PURPLE + "The x intercept is " + BLUE + str(x1))
	print(PURPLE + "The x intercept is " + BLUE + str(x2))
	print(PURPLE + "The y intercept is " + BLUE + str(c) )
	print(PURPLE + "The turning point is " + BLUE + "(" + str(TPx) + "," + str(TPy) + ")")

def getQuadratic(i): # gets all values for a quadratic (i for which part you want)(i must be a letter)
		print(GREEN + "Enter a value for " + i)
		a = float(getNumber())
		return a
	
def allQuadratic(a,b,c): # finds all outputs from a simple quadratic
	x1,x2 = quadraticFormula(a,b,c)
	TPx,TPy = turningPoint(a,b,c)
	outputQuadratic(a,b,c,x1,x2,TPx,TPy)
	
def decideQuadratic(): # decides which kind of quadratic you want to do - returns str 1/2/3/4
	choice = "test"
	print(GREEN + "\nEnter 1 if your quadratic is in the form: ax^2 + bx + c = 0 \nEnter 2 if your quadratic is in the form: ax^2 + bx + c = d \nEnter 3 if your quadratic is in the form: (ax + b) (cx + d) = 0 \nEnter 4 if your quadratic is in the form: (ax + b) (cx + d) = e")
	while choice not in ["1","2","3","4"]: # check if input is 1,2,3,4
		choice = input(WHITE + "Enter a choice: " + CYAN)
		if choice not in ["1","2","3","4"]:
			print(YELLOW + "Not a valid choice. ")
	return choice

# ax^2 + bx + c = 0
def expandedQuadratic():
	print(GREEN + "\nEnter values for a, b, c, where ax^2 + bx + c = 0")
	a,b,c = getQuadratic("a"),getQuadratic("b"),getQuadratic("c")
	allQuadratic(a,b,c)

# ax^2 + bx + c = d
def unevenExpandedQuadratic():
	print(GREEN + "\nEnter values for a, b, c, where ax^2 + bx + c = d")
	a,b,c,d = getQuadratic("a"),getQuadratic("b"),getQuadratic("c"),getQuadratic("d")
	c = c + d # converts to simple quadratic
	allQuadratic(a,b,c)

# (ax + b) (cx + d) = 0
def factorisedQuadratic():
	print(GREEN + "\nEnter values for a, b, c, d, where (ax + b) (cx + d) = 0")
	a,b,c,d = getQuadratic("a"),getQuadratic("b"),getQuadratic("c"),getQuadratic("d")
	a,b,c = convertQuadratic(a,b,c,d) # converts to simple quadratic 
	allQuadratic(a,b,c)

# (ax + b) (cx + d) = e
def unevenFactorisedQuadratic():
	print(GREEN + "\nEnter values for a, b, c, d, e where (ax + b) (cx + d) = e")
	a,b,c,d,e = getQuadratic("a"),getQuadratic("b"),getQuadratic("c"),getQuadratic("d"),getQuadratic("e")
	a,b,c = convertQuadratic(a,b,c,d) # converts to simple quadratic  
	c = c + e # converts to simple quadratic
	allQuadratic(a,b,c)

def goToQuadratic(n): # takes a choice; decides which quadratic to do
	stop = "test"
	while stop != "m": # loop / secondary
		if n == "1":
			expandedQuadratic() # ax^2 + bx + c = 0
		elif n == "2":
			unevenExpandedQuadratic() # ax^2 + bx + c = d
		elif n == "3":
			factorisedQuadratic() # (ax + b) (cx + d) = 0
		elif n == "4":
			unevenFactorisedQuadratic() # (ax + b) (cx + d) = e
		stop = stopping("type of quadratic menu",True) # loop / secondary

def pickQuadratic(): # combines all quadratic subroutines
	stop = "test"
	while stop != "m": # loop / menu
		choice = decideQuadratic()
		goToQuadratic(choice)
		stop = stopping("main menu",False) # loop / menu

	#------------------------------------------------------

def outputTrig(a,choice,ans):
	print(PURPLE + str(choice) + "(" + str(a) + ") = " + BLUE + str(ans) )

def getTrigFunction(): # gets input; returns sin/cos/tan/asin/acos/atan
	print(GREEN + "\nWhat trig function do you want to use?\n(cos sin tan acos asin atan)")
	choice = "test"
	while choice not in ["cos" , "sin" , "tan" , "acos" , "asin" , "atan"]: # checks input
		choice = input(WHITE + "Enter a choice: " + CYAN )
		if choice not in ["cos" , "sin" , "tan" , "acos" , "asin" , "atan"]:
			print(YELLOW + "Not a valid operator. ")
	return choice

def trigCheckRange(a): # makes a between 0-360
	if a < 0: 
		while a < 0:
			a = a + 360
			return a
	elif a > 360:
		while a > 360:
			a = a - 360
			return a
	else:
		return a

def getTrigNumberCosSinAtan():
	return float(getNumber())

def getTrigNumberAcosAsin():
	inRange = False
	while inRange != True:
		a = float(getNumber())
		if (a <=1) and (a>=-1): # checks if a is between -1 and 1
			inRange = True
		else:
			print(YELLOW + "Must be in range -1 to 1. ") # error statement 
			inRange = False
	return a

def getTrigNumberTan():
	inf = True
	while inf == True:
		a = float(getNumber())
		a1 = trigCheckRange(a) # makes a1 between 0 - 360
		if str(a1) in ["90.0","270.0"]: # checks if a1 is 90/270
			inf = True
		else:
			inf = False
		if inf == True:
			print(YELLOW + "Invalid input; would be infinite") # error statement 
	return a 

def getTrigAnswer(choice): # takes a choice, runs that trig function, returns input and answer
	if choice == "sin":
		a = getTrigNumberCosSinAtan()
		ans = sin(radians(a))
		return ans,a
	elif choice == "cos":
		a = getTrigNumberCosSinAtan()
		ans = cos(radians(a))
		return ans,a
	elif choice == "tan":
		a = getTrigNumberTan()
		ans = tan(radians(a))
		return ans,a
	elif choice == "acos":
		a = getTrigNumberAcosAsin()
		ans = degrees(acos(a))
		return ans,a
	elif choice == "asin":
		a = getTrigNumberAcosAsin()
		ans = degrees(asin(a))
		return ans,a
	elif choice == "atan":
		a = getTrigNumberCosSinAtan()
		ans = degrees(atan(a))
		return ans,a
	else:
		return "error","error"

def TrigCalculator():
	stop = "test"
	while stop != "m": # loop
		choice = getTrigFunction()
		ans,a = getTrigAnswer(choice)
		outputTrig(a,choice,ans)
		stop = stopping("main menu",True) # loop

#------------------------------------------------------

def piCounter(a): # finds where you stopped being correct
	n = 0 
	a = str(a)
	while a[n] == PI[n]: # while the nth number of both strings is the same
		if n == len(a)-1 : # checks if it has reached the end of the input
			return n
		if n == len(PI)-1: # checks if it has reached the end of pi
			return n
		n = n+1
	return n - 1 # n - 1 reverses the n + 1 at the end of the while loop

def piNumFinder(n): # finds how many digits of pi you have (takes the position of final correct digit)(returns number of correct digits)
	if n == 0: # if theres is only one character there is 1 digit
		num = 1
	elif n == 1: # if there are 2 characters there is one digit
		num = 1
	else: # otherwise the number of digits is equal to the index of the final number
		num = n
	return num

def piSplit(n): # finds the next 5 digits of pi
	next = PI[n+1:]
	next = next[:5]
	return next

def colourInInputPi(n,input): # takes your input and colours in everything after you started to go wrong
	correct = PI[:n+1]
	incorrect = input[n+1:]
	output = str(correct) + RED + str(incorrect)
	return output

def getPiInput():
	print(GREEN + "\nEnter as many digits of pi as you can.")
	return getNumber()

def outputPi(output,next,num):
	print(PURPLE + "You got " + BLUE + str(num) + PURPLE + " digits correct.")
	print(PURPLE + "You are correct up to: " + BLUE + str(output))
	print(PURPLE + "The next 5 digits are: " + BLUE + str(next))
	
def piTrainer(): # combines all piTrainer subroutines
	stop = "test"
	while stop != "m": # loop
		input = getPiInput()
		n = piCounter(input)
		num = piNumFinder(n)
		next = piSplit(n)
		output = colourInInputPi(n,input)
		outputPi(output,next,num)
		stop = stopping("main menu",False) # loop

#--------------------------------------------------------------
	
def calculatePercentageChange(new,original): # claculates percentage change from original and new
	change = new - original # percent change calculation
	percChange = (change/original) * 100 # percent change calculation
	percChange = str(percChange)
	if percChange[0] != "-": # checks if it has a - in front
		percChange = "+" + percChange # if there is no - add a +
	return percChange

def getOriginalAndNew(): # gets values for new and original
	print(GREEN + "\nEnter the original value")
	original = float(getNumber())
	print(GREEN + "\nEnter the new value")
	new = float(getNumber())
	return original,new

def outputPercentageChange(new,original,percChange): # outputs percentage change
	print("\n" + PURPLE + str(original) + " -> " + str(new) + "is a change of " + BLUE + str(percChange) + "%" )

def percentageChange(): # combines all percenatgeChange subroutines
	stop = "test"
	while stop != "m":
		original,new = getOriginalAndNew()
		percChange = calculatePercentageChange(new,original)
		outputPercentageChange(new,original,percChange)
		stop = stopping("main menu",True)

# ------------------------------------------------------------------

def calcCompoundInterest(start,change,time): # calculates final amount
	change = change + 100 # turns it from + x% to * x%
	change = change / 100 # makes it a decimal instead of a percentage
	ans = start * (change ** time) # actual calculation
	return ans

def getStartChangeTime(): # gets starting amount, num of times it changes, amount it changes by
	print(GREEN + "\nWhat is the starting amount? ")
	start = float(getNumber())
	time = "hello"
	while isint(time) == False:
		print(GREEN + "\nHow many times will the amount change?")
		time = float(getNumber())
		if isint(time) == False:
			print(YELLOW + "Not a valid time period")
	print(GREEN + "\nHow much will the amount change by in percent?")
	change = float(getNumber())
	return start,change,time

def outputCompoundInterest(start,time,change,ans): 
	print(PURPLE + "Starting at " + str(start) + " with " + str(time) + " intervals and a change of " + str(change) + "% per interval." + " \nThe final amount will be: " + BLUE + str(ans))

def compoundInterest(): # combines all compoundInterest subroutines
	stop = "test"
	while stop != "m": # loop
		start,change,time = getStartChangeTime()
		ans = calcCompoundInterest(start,change,time)
		outputCompoundInterest(start,time,change,ans)
		stop = stopping("main menu",True) # loop

#-------------------------------------------------------------

def calcCylinderVolume(h,r): # takes height , radius of a cyclinder - returns volume
	base = (sq(float(r)))*float(PI) # calculates area of base
	volume = base*float(h) # calculates volume
	return volume,base

def calcCylinderArea(base,h,r): # takes height , radius of a cyclinder - returns surface area
	circ = float(r)*2*float(PI) # calculates circumference
	cArea = circ * float(h) # calculates curved surface area
	area = cArea + (2*float(base)) # calculates total surface area
	return area

def outputCylinder(volume,area,h,r): # outputs volume and area of a cylinder
	print(PURPLE + "\nThe cylinder with radius " + str(r) + " and height " + str(h) + " has: ")
	print(PURPLE + "A volume of: " + BLUE + str(volume))
	print(PURPLE + "A surface area of: " + BLUE + str(area))

def getCylinderNumbers(): # gets height and radius of a cylinder
	print(GREEN + "\nEnter the values for the height and radius of a cyclinder.")
	print(GREEN + "Enter the value for the radius.")
	r = getNumber()
	print(GREEN + "Enter the value for the height.")
	h = getNumber()
	return float(r),float(h)

def cylinder(): # combines all cylinder subroutines
	stop = "test"
	while stop != "m": # loop
		r,h = getCylinderNumbers()
		volume,base = calcCylinderVolume(h,r)
		area = calcCylinderArea(base,h,r)
		outputCylinder(volume,area,h,r)
		stop = stopping("3D shapes menu",True) # loop

# -------------------

def outputCuboid(volume,area,diagonal,a,b,c): # outputs volume, area, interior diagonal of a cuboid
	print(PURPLE + "\nThe cuboid with sides " + str(a)  + "*" + str(b) + "*" + str(c) + " has: ")
	print(PURPLE + "A volume of: " + BLUE + str(volume))
	print(PURPLE + "A surface area of: " + BLUE + str(area))
	print(PURPLE + "An interior diagonal of: " + BLUE + str(diagonal))

def calcCuboidVolume(a,b,c): # calculates volume
	ans = a*b*c
	return ans

def calcCuboidArea(a,b,c): # calculates area
	x = a*b*2 # side 1 x 2
	y = a*c*2 # side 2 x 2
	z = b*c*2 # side 3 x 2
	area = x + y + z
	return area

def calcCuboidDiagonal(a,b,c): # calculates the interior diagonal of a cuboid
	diagonal = sqrt((a*a)+(b*b)+(c*c)) # 3D pythagoras
	return diagonal

def getCuboidNumbers(): # gets height, width, length of a cuboid
	print(GREEN + "\nEnter the values for each side of a cuboid. ")
	print(GREEN + "Enter the value for the length.")
	a = float(getNumber())
	print(GREEN + "Enter the value for the width.")
	b = float(getNumber())
	print(GREEN + "Enter the value for the height.")
	c = float(getNumber())
	return float(a),float(b),float(c)

def cuboid(): # combines all cuboid subroutines
	stop = "test" # set
	while stop != "m": # loop
		a,b,c = getCuboidNumbers()
		volume = calcCuboidVolume(a,b,c)
		area = calcCuboidArea(a,b,c)
		diagonal = calcCuboidDiagonal(a,b,c)
		outputCuboid(volume,area,diagonal,a,b,c)
		stop = stopping("3D shapes menu",True)

# -------------------

def calcConeBase(r): # calculates the area of the base of a cone
	base = (sq(r))*float(PI)
	return base

def calcConeEdge(r,h): # calculates the diagonal edge of a cone
	l = sqrt((r*r)+(h*h))
	return l

def calcConeVolume(h,base): # calculates the volume of a cone
	volume = 1/3 * base * h
	return volume

def calcConeArea(base,r,l): # calculates the surface area of a cone
	cArea = float(PI) * r * l
	area = cArea + base
	return area

def getConeNumbers(): # gets the radius and height of a cone
	print(GREEN + "\nEnter the radius and height of a cone.")
	print(GREEN + "\nEnter the radius.")
	r = getNumber()
	print(GREEN + "\nEnter the height.")
	h = getNumber()
	return float(r),float(h)

def outputCone(sArea,volume,base,edge,h,r): # outputs surface area, volume, area of base, and diagonal edge
	print(PURPLE + "The cone with height " + str(h) + " and radius " + str(r) + " has:")
	print(PURPLE + "A surface area of: " + BLUE + str(sArea))
	print(PURPLE + "A volume of: " + BLUE + str(volume))
	print(PURPLE + "A base of: " + BLUE + str(base))
	print(PURPLE + "A diagonal of: " + BLUE + str(edge))

def cone(): # combines all cone subroutines
	stop = "test"
	while stop != "m": # loop
		r,h = getConeNumbers()
		base = calcConeBase(r)
		l = calcConeEdge(r,h)
		volume = calcConeVolume(h,base)
		sArea = calcConeArea(base,r,l)
		outputCone(sArea,volume,base,l,h,r)
		stop = stopping("3D shapes menu",True) # loop

# -------------------

def calcSphereVolume(r): # calculates volume of a sphere
	volume = (4/3)*float(PI)*(r*r*r)
	return volume

def calcSphereArea(r): # calculates surface area of a sphere
	area = 4*float(PI)*r*r
	return area

def getSphereNumbers(): # gets the radius of a sphere
	print(GREEN + "\nEnter the radius of a sphere: ")
	r = getNumber()
	return float(r)

def outputSphereNumbers(r,volume,area): # outputs volume and surface area of a sphere
	print(PURPLE + "\nA sphere with radius " + str(r) + "has: ")
	print(PURPLE + "A volume of: " + BLUE + str(volume))
	print(PURPLE + "A surface area of: " + BLUE + str(area))

def sphere(): # combines all sphere subroutines
	stop = "test"
	while stop != "m": # loop
		r = getSphereNumbers()
		volume = calcSphereVolume(r)
		area = calcSphereArea(r)
		outputSphereNumbers(r,volume,area)
		stop = stopping("3D shapes menu",True) # loop

#-------------------------

def calcPyramidVolume(a,b,h): # takes 2 sides and a height; returns float(volume)
	volume = 1/3 * float(a) * float(b) * float(h)
	return volume 

def calcPyramidArea(a,b,h):# takes 2 sides and a height; returns float(surface area)
	face1Height = sqrt(sq(float(b)/2) + sq(float(h))) # calcs height of one triangular face
	face1 = (face1Height * float(a))/2 # calculates area of triangular face
	face2Height = sqrt(sq(float(a)/2) + sq(float(h))) # calculates height of other triangular face
	face2 = (face1Height * float(b))/2 # calculates area of triangular face
	surfaceArea = face1 + face1 + face2 + face2 + (float(a)*float(b)) # adds up all triangular faces and base
	return surfaceArea

def getPyramidNumbers():
	print(GREEN + "\nEnter the value for one of the sides of the base.")
	a = getNumber()
	print(GREEN + "Enter the value for another side of the base.")
	b = getNumber()
	print(GREEN + "Enter the height")
	h = getNumber()
	return a,b,h

def outputPyramid(a,b,h,volume,sArea):
	print(PURPLE + "\nThe pyramid with base " + str(a) + "x" + str(b) + " and height " + str(h) + " has: ")
	print(PURPLE + "A volume of: " + BLUE + str(volume))
	print(PURPLE + "A surface area of: " + BLUE + str(sArea))

def pyramid():
	stop = "test"
	while stop != "m":
		a,b,h = getPyramidNumbers()
		volume = calcPyramidVolume(a,b,h)
		sArea = calcPyramidArea(a,b,h)
		outputPyramid(a,b,h,volume,sArea)
		stop = stopping("3D shapes menu",True)

# ------------------------

def threeDimensionalShapes():
	stop = "test" # set
	while stop != "m": # loop
		choice = "test"
		print(GREEN + "\nEnter 1 for cuboids. \nEnter 2 for cylinders. \nEnter 3 for spheres. \nEnter 4 for cones. \nEnter 5 for pyramids." + WHITE)
		while choice not in ["1","2","3","4","5"]:
			choice = input(WHITE + "Enter a choice: " + CYAN)
			if choice not in ["1","2","3","4","5"]:
				print(YELLOW + "Not a valid choice")
		if choice == "1":
			cuboid()
		elif choice == "2":
			cylinder()
		elif choice == "3":
			sphere()
		elif choice == "4":
			cone()
		elif choice == "5":
			pyramid()
		stop = stopping("main menu",False) # loop

# ------------------------------------------------------------

def isPrime(n): # checks if prime - returns Boolean
	if n <= 3: # if n is less than or equal to 3 
		return n > 1 # if it is greater than 1 (2 or 3) then it is prime - returns 2 ,   if it is 1 or less then it is not prime
	if not n%2 or not n%3: # % sign checks if n divided by the number has a remainder
		# if it has a remainder then it is not divisible by the number (2 or 3)
		# if it doesn't have a remainder then it is exactly divisible by that number (2or3) - making it not prime
		return False # returns false if the number has no remainder when divided by 2 or 3
	# all primes are in the form 6k ± 1, where k is any integer greater than 0
	k = 1
	stop = int(sqrt(n)) # all factor pairs will have one digit that is smaller than the sqrt of n, this is because after the factor pair x*x the factor pairs start repeating themselves, for example 100 is divisible by 2×50, 4×25, 5×20, 10×10, 20×5, 25×4, 50×2 note that after 10x10 (the square roots of 100) the factors start to repeat themselves - this means that you only need to check for factors up to the sqrt of n
	while ((6*k)-1) <= stop: # counts in 6k (from 6k±1) up to the sqrt of n
		if not n%((6*k)-1) or not n%((6*k)+1): # checks if dividing by 6k±1 results in a whole number - not prime 
			return False # if n can be divided by any of the tested numbers then it is not prime so False is returned
		k = k + 1 # increments k by 1 in order to test all possible factors of 6k±1
	return True # if all of the tested possible factors do not work then the number is prime

def getPotentialPrime(): # gets a number to check if it is prime
	print(GREEN + "\nEnter a number to check if it is a prime.")
	n = float(getNumber())
	while isint(n) == False:
		print(YELLOW + "You can only check whole numbers.")
		n = float(getNumber())
	return n 

def outputPrime(n,TorF): # outputs a number and says if it is prime or not
	if TorF == True:
		print(PURPLE + "\n" + str(n) + BLUE + " is " + PURPLE + "a prime number.")
	if TorF == False:
		print(PURPLE + "\n" + str(n) + BLUE + " is not " + PURPLE + "a prime number.")

def prime(): # combines all prime checker subroutines
	stop = "test"
	while stop != "m":
		n = getPotentialPrime()
		TorF = isPrime(n)
		outputPrime(n,TorF)
		stop = stopping("main menu",True)

# ------------------------------------------------------------

def	findPrimes(start,stop):
	with open('listOfPrimes','w') as listOfPrimes: # opens the file and allows you to write in it (this replaces text in the file)
		keepGoing = True
		n = 0
		k = 0
		l = 0
		memory = []
		n = int(start/6) # sets n (which is then multiplied by 6 for 6n +/- 1)
		if start < 4:
			if 2 >= start and 2 <= stop: # adds 2 to the list
				listOfPrimes.write("\n" + str(2))
			if 3 >= start and 3 <= stop: # adds 3 to the list
				listOfPrimes.write("\n" + str(3))
		while keepGoing == True:
			if 6*n > stop: # checks if the stop point has been passed
				keepGoing = False
				n = -1 # stops anything more from being written after the stop point has been passed
			k = 6*n - 1
			l = 6*n + 1
			if isPrime(k) == True:
				listOfPrimes.write("\n" + str(k)) # writes to file
			if isPrime(l) == True:
				listOfPrimes.write("\n" + str(l)) # writes to file
			n = n + 1

def getFindPrimesRange():
	print(GREEN + "\nEnter the range that you want to search within.")
	print(GREEN + "Enter the start of the range.")
	start = int(getInteger())
	print(GREEN + "Enter the end of the range.")
	stop = int(getInteger())
	return start,stop

def outputFindPrimes(start,stop,list):
	print(PURPLE + "\nThe primes between " + str(start) + " and " + str(stop) + " are: " + BLUE)
	print(list)

def primeSearch():
	stop= "test"
	while stop != "m":
		start,stop = getFindPrimesRange()
		findPrimes(start,stop)
		print(PURPLE + "Check the file named 'listOfPrimes' to see the output. ")
		stop = stopping("main menu",True)

# --------------------------------------------------------

def outputMean(avg):
	print(PURPLE + "The mean is: " + BLUE + str(avg))

def mean(): # combines all average calculator subroutines
	stop = "test"
	while stop != "m":
		list = getMeanNumbers()
		avg = calcMean(list)
		outputMean(avg)
		stop = stopping("main menu",True)

# --------------------------------------------------------------

def calcStandardDeviation(list,mean,type): # calculates the standard division of a set of numbers (spread)
	length = len(list)
	sum = 0
	for i in range(length): # for each number in the list
		sum = sum + sq(float(list[i])-float(mean)) # sum of all of the (differences between each number and the mean) squared
	if type == "population": # if you have an entire population divide by the number of inputs
		return sqrt(sum/length)
	elif type == "sample": # if you have a sample to estimate the standard deviation of a population divide by the number of inputs -1 - this makes the spread much larger for small samples and not much larger for large samples
		return sqrt(sum/(length-1))

def calcStandardDeviationPercentage(mean,standardDeviation):
	percDiff = float(standardDeviation) / float(mean) * 100
	return percDiff

def getStandardDeviationInputs(): # gets a list of numbers, the mean of those numbers, and weather they have an entire population or a sample
	type = "test"
	list = getMeanNumbers()
	mean = calcMean(list)
	print(GREEN + "\nWhat type of data set do you have - a population or a sample.")
	while type not in ["population","sample"]:
		type = input(WHITE + "Enter a choice: " + CYAN)
		if type not in ["population","sample"]:
			print(YELLOW + "Not a valid choice")
	return list,mean,type

def outputStandardDeviation(standardDeviation,mean): # outputs mean and standard deviation
	print(PURPLE + "\nThe mean is: " + BLUE + str(mean))
	print(PURPLE + "The standard deviation is: " + BLUE + str(standardDeviation))

def standardDeviation(): # combines all standard deviation subroutines
	stop = "test"
	while stop != "m":
		list,mean,type = getStandardDeviationInputs()
		standardDeviation = calcStandardDeviation(list,mean,type)
		perDiff = calcStandardDeviationPercentage(mean,standardDeviation)
		print(perDiff)
		outputStandardDeviation(standardDeviation,mean)
		stop = stopping("main menu",True)

# ------------------------------------------------------------------------------------

def binaryToHex(binary): # takes a binary number and converts it to hex; returns str(hex)
	binary = str(binary)
	length = len(binary)
	numOfHexPos = math.ceil(length/4) # the number of hex positions needed is the number of binary positions/4 rounded up 
	binary = expandBinary(binary) # makes binary number a multiple of 4 long
	ans = ""
	for i in range(numOfHexPos): # repeats for each hex pos (4 binary digits)
		x = 0 
		jump = (i*4) + 3 # jump by 4 (1 hex pos), +3(goes to the right of each chunk)
		for j in range(4): # 4 times
			x = x + (int(binary[jump-j])*(2**j)) # jump - j moves from right to left of each chunk; *2**j mens x1 x2 x4 x8,  makes x an integer between 0 and 15
		if x == 10: # elif block turns numbers 10 or higher into letters
			x = "A"
		elif x == 11:
			x = "B"
		elif x == 12:
			x = "C"
		elif x == 13:
			x = "D"
		elif x == 14:
			x = "E"
		elif x == 15:
			x = "F"	
		ans = ans + str(x) # adds each hex number to the front of the final answer
	return ans

def binaryToDecimal(binary):
	binary = str(binary)
	length = len(binary)
	pos = length - 1 # goes to far right of binary
	x = 0
	for i in range(length):  # for every number
		x = x + (int(binary[pos]) * (2**i)) # total = position * 2 to the power of 1 meaning it timeses by 1 then 2 then 4 etc...
		pos = pos - 1 # counts pos from right to left
	return x

def hexToBinary(hex):
	hex = str(hex)
	length = len(hex)
	ans = ""
	for i in range(length):
		x = ""
		if hex[i] == "A":
			hexNumber = 10
		elif hex[i] == "B":
			hexNumber = 11
		elif hex[i] == "C":
			hexNumber = 12
		elif hex[i] == "D":
			hexNumber = 13
		elif hex[i] == "E":
			hexNumber = 14
		elif hex[i] == "F":
			hexNumber = 15
		else:
			hexNumber = int(hex[i])		
		decByHalf = 8
		for j in range(4):
			if hexNumber - decByHalf >= 0:
				x = x + "1"
				hexNumber = hexNumber - decByHalf
			else:
				x = x + "0"
			decByHalf = decByHalf/2
		ans = ans + x
	return ans

def decimalToBinary(decimal):
	length = len(decimal)
	decimal = float(decimal)
	decimal = int(decimal)
	approxBinaryLength = length*4
	check = 2**approxBinaryLength
	x = ""
	while check > 1:
		if decimal - check >= 0:
			x = x + "1"
			decimal = decimal - check
		else:
			x = x + "0"
		check = check / 2
	if decimal - check >= 0:
		x = x + "1"
	else:
		x = x + "0"
	x = shortenBinary(x)
	x = expandBinary(x)
	return x

def hexToDecimal(hex):
	length = len(hex)
	ans = 0
	posValue = 16**(length-1)
	for i in range(length):
		if hex[i] == "A":
			hexNumber = 10
		elif hex[i] == "B":
			hexNumber = 11
		elif hex[i] == "C":
			hexNumber = 12
		elif hex[i] == "D":
			hexNumber = 13
		elif hex[i] == "E":
			hexNumber = 14
		elif hex[i] == "F":
			hexNumber = 15
		else:
			hexNumber = int(hex[i])
		trueHexNumber = hexNumber * posValue
		posValue = posValue/16
		ans = ans + trueHexNumber
	return ans

def decimalToHex(decimal):
	decimal = float(decimal)
	nextPart = int(decimal)
	ans = ""
	while nextPart > 0:
		remainder = int(nextPart)%16
		if remainder == 10:
			remainder = "A"
		elif remainder == 11:
			remainder = "B"
		elif remainder == 12:
			remainder = "C"
		elif remainder == 13:
			remainder = "D"
		elif remainder == 14:
			remainder = "E"
		elif remainder == 15:
			remainder = "F"
		else:
			remainder = int(remainder)
		ans = str(remainder) + ans
		nextPart = int(nextPart/16)
	return ans

def binaryToDecimalConversions():
	stop = "test"
	while stop != "m":
		start = "binary"
		to = "decimal"
		num = getBinaryNumber()
		ans = binaryToDecimal(num)
		outputConversions(num,ans,start,to)
		stop = stopping("conversions menu",True)
	return num,ans,start,to

def binaryToHexConversions():
	stop = "test"
	while stop != "m":
		start = "binary"
		to = "hex"
		num = getBinaryNumber()
		ans = binaryToHex(num)
		outputConversions(num,ans,start,to)
		stop = stopping("conversions menu",True)
	return num,ans,start,to

def decimalToBinaryConversions():
	stop = "test"
	while stop != "m":
		start = "decimal"
		to = "binary"
		num = getDecimalNumber()
		ans = decimalToBinary(num)
		outputConversions(num,ans,start,to)
		stop = stopping("conversions menu",True)
	return num,ans,start,to 

def decimalToHexConversions():
	stop = "test"
	while stop != "m":
		start = "decimal"
		to = "hex"
		num = getDecimalNumber()
		ans = decimalToHex(num)
		outputConversions(num,ans,start,to)
		stop = stopping("conversions menu",True)
	return num,ans,start,to

def hexToDecimalConversions():
	stop = "test"
	while stop != "m":
		start = "hex"
		to = "decimal"
		num = getHexNumber()
		ans = hexToDecimal(num)
		outputConversions(num,ans,start,to)
		stop = stopping("conversions menu",True)
	return num,ans,start,to

def hexToBinaryConversions():
	stop = "test"
	while stop != "m":
		start = "hex"
		to = "binary"
		num = getHexNumber()
		ans = hexToBinary(num)
		outputConversions(num,ans,start,to)
		stop = stopping("conversions menu",True)
	return num,ans,start,to

def outputConversions(num,ans,start,to):
	print(PURPLE  + str(num) + " in " + str(start) + " = " + BLUE + str(ans) + PURPLE + " in " + str(to))

def decideConversion():
	stop = "test"
	while stop != "m":
		print(GREEN + "\nPick which conversion you want to do.")
		print(GREEN + "Enter 1 for binary to decimal conversions.")
		print(GREEN + "Enter 2 for binary to hexadecimal conversions.")
		print(GREEN + "Enter 3 for decimal to binary conversions.")
		print(GREEN + "Enter 4 for decimal to hexadecimal conversions.")
		print(GREEN + "Enter 5 for hexadecimal to decimal conversions.")
		print(GREEN + "Enter 6 for hexadecimal to binary conversions.")
		choice = input(WHITE + "Enter a choice: " + CYAN)
		while choice not in ["1","2","3","4","5","6"]:
			print(YELLOW + "Not a valid choice")
			choice = input(WHITE + "Enter a choice: " + CYAN)
		if choice == "1":
			binaryToDecimalConversions()
		elif choice == "2":
			binaryToHexConversions()
		elif choice == "3":
			decimalToBinaryConversions()
		elif choice == "4":
			decimalToHexConversions()
		elif choice == "5":
			hexToDecimalConversions()
		elif choice == "6":
			hexToBinaryConversions()
		stop = stopping("main menu",False)

# ---------------------------------------------

def binaryAddition(bin1,bin2):
	ans = float(binaryToDecimal(bin1)) + float(binaryToDecimal(bin2))
	ans = decimalToBinary(ans)
	return str(int(float(ans)))

def binaryMultiplication(times,binary):
	ans = float(binaryToDecimal(binary)) * times
	ans = decimalToBinary(ans)
	return str(int(float(ans)))

def binaryDivision(times,binary):
	ans = float(binaryToDecimal(binary)) / times
	ans = decimalToBinary(ans)
	return str(int(float(ans)))

def binaryDivisionControl():
	binary = getBinaryNumber()
	times = 0
	times = getMultiplier()

# ----------------------------------------------

def calculatorPicker(): # master subroutine
	headerFooter()
	print(GREEN + "Enter 1 for a basic calculator.\nEnter 2 for circle properties. \nEnter 3 for quadratics. \nEnter 4 for trig functions. \nEnter 5 for Pi trainer. \nEnter 6 for percentage change. \nEnter 7 for compound interest. \nEnter 8 for mean average. \nEnter 9 for 3D shapes. \nEnter 10 to find if a number is prime. \nEnter 11 to search for primes. \nEnter 12 for standard deviation. \nEnter 13 to convert between binary, hex, and decimal." + WHITE)
	choice = input(WHITE + "Enter a choice: " + CYAN)
	while choice not in ["1","2","3","4","5","6","7","8","9","10","11","12","13"]:
		print(YELLOW + "Not a valid choice")
		choice = input(WHITE + "Enter a choice: " + CYAN)		
	if choice == "1":
		basicCalculator()
	elif choice == "2":
		circleCalculator()
	elif choice == "3":
		pickQuadratic()
	elif choice == "4":
		TrigCalculator()
	elif choice == "5":
		piTrainer()
	elif choice == "6":
		percentageChange()
	elif choice == "7":
		compoundInterest()
	elif choice == "8":
		mean()
	elif choice == "9":
		threeDimensionalShapes()
	elif choice == "10":
		prime()
	elif choice == "11":
		primeSearch()
	elif choice == "12":
		standardDeviation()
	elif choice == "13":
		decideConversion()

while True:
	calculatorPicker()






#1, Printing Hello World

print("Hello World")

#2, Creating 3 variables - name, surname and course

name = "Josh"
surname = "Coleman"
course = "Computer Science with Cyber-security"

#3, Write a for loop using variables in #2 printing a sentence

for x in range(0,6):
    print("This is the FOR loop")
    print("My name is " + name + " " + surname + " and I am studying " + course)
    print("                 ")
print("\n-------SPACER-------\n")
#4, Write a while loop using variables in #2 printing a sentence

counter1 = 0
while counter1 < 6:
    print("This is the WHILE loop")
    print("My name is " + name + " " + surname + " and I am studying " + course)
    counter1 = counter1 + 1
    print("                 ")
print("\n-------SPACER-------\n")
    
#5, Create a function called WeekDay which asks for a number and converts it to a weekday

dayInput = input("Enter a number 1-7")

def weekDay(dayInput):
    dayInput = int(dayInput)
    if dayInput ==1:
        print("Monday")
    elif dayInput ==2:
        print("Tuesday")
    elif dayInput ==3:
        print("Wednesday")
    elif dayInput ==4:
        print("Thursday")
    elif dayInput ==5:
        print("Friday")
    elif dayInput ==6:
        print("Saturday")
    elif dayInput ==7:
        print("Sunday")
    else:
        print("Not accepted")

weekDay(dayInput)
print("\n-------SPACER-------\n")

#6, Slice the phrase "Artificial Intelligence", print into two chunks

def chunk(x):
    print(x[:3])
    print(x[3:])

chunk("Artificial Intelligence")
print("\n-------SPACER-------\n")


#7, Create a function that takes in any number of integers and returns sum

def sumMachine():
    numOfNums = int(input("How many numbers do you want to add? 2-10 "))
    if numOfNums < 2 or numOfNums >10:
        print("NOT ACCEPTED, enter number between 2-10")
    else:
        total = 0
        for i in range(numOfNums):
            num = int(input("Enter a number: "))
            total = total + num
        print("The sum is:", total)

sumMachine()

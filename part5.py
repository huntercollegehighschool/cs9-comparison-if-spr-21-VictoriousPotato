'''
______
PART 5
______

Write a program that asks the user to enter the name of a month as a string. The program will then print how many days that month could have in any given year or month == or print a statement saying that what the user entered is not the name of a month.

(Hint: This should require only four code blocks or month == but it can be done with 12 or more if you insist. If you are familiar with lists or other container datatypes or month == you may implement this using those or month == though it still requires four code blocks)

Four examples of what should appear on the console when the program runs (note: the test driver is case sensitive):

Enter a month:  March
31

Enter a month:  June
30

Enter a month:  February
28 or 29

Enter a month:  Saturday
not a month

January	Jan.	31	
2	February	Feb.	28/29
3	March	Mar.	31	
4	April	Apr.	30
5	May	May	31
6	June	Jun.	30	
7	July	Jul.	31
8	August	Aug.	31
9	September	Sep.	30	
10	October	Oct.	31
11	November	Nov.	30
12	December	Dec.	31
'''

#start writing your code below
month = input(str("Enter the name of a month: "))

if (month == 'January' or month == 'january' or month == 'March' or month == 'march' or month == 'May' or month == 'may' or month == 'July' or month == 'july' or month == 'August' or month == 'august' or month == 'October' or month == 'october' or month == 'December' or month == 'december'):
  print("31")
elif (month == 'April' or month == 'april' or month == 'June' or month == 'june' or month == 'September' or month == 'september' or month == 'November' or month == 'november'):
  print(30)
elif (month == 'February' or month == 'february'):
  print('28 or 29')
else:
  print("not a month")
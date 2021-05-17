# *******************************************************************************
# Author: Gregory Shenefelt
# Lab: Lab 3
# Date: 04/21/2021
# Description: A program that helps you see how much you lost on a shipment \n
#  due to markdowns
# Input: The invoice total, the numbers of items to markdown, and the amount \n
#  of dollars the item has been redeuced by
# Output: The total of the shipment, how many dollars it was redeuced by \n
# and the percentage of loss.
# Sources: course materials, gaddis book.


# Pseudocode:
# // This program will tell the user how much they have lost in a shipment
# // Due to markdowns.
# // It will then display to the user the amount they have lost in
# // both dollars and %
# // It will then output a message to the user
# // it will also
# // Input List: shipmentValue – the total cost of the shipment,
# // itemsCost – the cost of the item
# // markdownAmount – amount the item has been marked down in dollars
# // Output List: shipmentValue //dollarsLost – the amount of dollars lost // firstRun – an optional message if this is their first time using the program
# // lossPercentage – the total amount of the loss as a percent
# // A message to the user showing the original cost of the shipment
# // The amount of dollars lost // and what percentage of the shipmentValue
# // was lost

# //newUserMsg() asks the user if this is their first time running the program
# // if the user enters y it will let the user know how this program works
# // if the user enters n it will just tell the user to proceed
# Module newUserMsg()
# 	// Local Variable
# 	Declare String msg
# 	Display “Is this the first time using this program? Enter y/n”
# 	If msg == ‘y’ Then
# 	Display “Welcome to your first run”
#   Display “I will ask for your invoice total, number of  markdowns, and the sum to reduce by”
#   Display “I will then calculate your loss in dollars and percent”
#   Display “And advise you if you should reorder them or not”
#   Else
# 	Display “Please begin entering your values”
#   End If
# End Module

# // getValue() gets the total cost of the shipment and returns it
# Module getValue()
# 	// Local Variable
# 	Declare Real shipmentValue
# 	Display “Enter the total from the invoice:”
# 	Input shipmentValue
# // Return the shipment value to the main module
# Return shipmentValue
# End Module

# // the itemValue() asks the user to input the number of items that
# // need to be marked down and collects the cost of the item
# // and then returns it

# Module itemValue()
# 	// Declare local variables
# 	// these values will allow the user to control the amount of times
# // the loop will iterate.
#   Declare Integer, numItems
#    Display “How many items would you like to markdown?”
#   Input numItems
#   // Enter the user controlled for loop that will iterate from 1 to numItems + 1 // so that way we capture all the items the user wishes to markdown
#   For counter = 1, numItems +1
#   // Declare a variable to hold the cost of the item
#   Declare Real itemVal = 0.0
#   Declare Real cost
#   Display “Enter the cost of item”,counter
#   Input cost
#   Set itemVal = itemVal + cost
# End For
# // Return the total amount of the markdowns to the main module
# Return itemVal
# End Module

# // The reducedby() will take the itemCost and the shipmentValue as arguments and subtract the two then it will return the product to the markdownAmount variable
# Module reducedby(Declare Real x, Declare Real y)
# 	// define a local variable to hold the calculations sum
# 	Declare Real sum
# 	// x will hold the shipmentValue and y will hold the itemCost
# 	Set sum = x – y
# // return the sum back to the main module
# Return sum
# End Module

# // the lossPercent() will take the shipmentValue and itemCost as arguments and convert it to a percent
# Module lossPercent(declare Real a, Real b)
# 	// Declare the local variables that will perform a calculation
# 	Declare Real perHundred
# 	// calculate the percentage of the shipment that was lost due to markdowns
# 	perHundred = (b/a) * 100
# Return perHundred
# End module

# // the lossAlert(real z) module will take the itemCost as an argument and depending on the amount will output a message
# Module lossAlert(real z)
# 	// Determine the message to output to the user
# 	If z > 100 Then
# 		Display “High losses reported, please review order flow”
# 	Else If z > 35 Then
# 		Display “Please don’t order anymore”
# 	Else
# 		Display “Low losses reported”
# 		Display “Please track sales on items”
# 		Display “to determine if you should keep them on hand”
# 	End If
# // Return the message back to the main module
# Return z
# End Module

# // The main() will call all the modules and run them and output
# // The total spent, the total dollars lost, and the percent lost

# Module main()
# 	// Local Variables
# 	Declare String firstRun, message
# Declare Real shipmentValue,itemCost,markdownAmount
# 	Declare Real markdownPercent,
# 	Call newUserMsg
# 	Set firstRun
# 	Call getValue()
# 	Set shipmentValue
# 	Call redeucedby(shipmentCost,itemCost)
# 	Set markdownAmount
# 	Call lossPercent(shipmentValue,itemCost)
# 	Set markdownPercent
# 	Call lossAlert(itemCost)
# 	Set message
# 	Display “You spent: $”, shipmentValue
# 	Display “You did a total markdown for: $”,itemCost
# 	Display “Which is”,markdownPercentage,”%”
# End Module
# Call main()
# *******************************************************************************
# Begin Python Program

# define newUserMsg() which will ask the user if this is their first time launching this program
# it will then use an if statement to determine if it should outprint what it does
# to the user
def newUserMsg():
    while True:
        # validate that the usesr has input y or n
        try:
            msg = input(
                'Is this your first time using this program? Enter y/n ')
            msg = msg.lower()
            print(" ")
            if msg != 'y' and msg != 'n':
                raise ValueError
            # if msg is valid break out of the loop
            else:
                break
        except ValueError:
            # if msg is invalid remind the user of the choices and continue
            print('y for yes - n for no')
            continue

    if msg == 'y':
        print('Welcome to your first run')
        print(
            'I will ask you for your invoice total, number of markdowns, and the value to reduce by')
        print('I will then calculate your loss in dollars and percent')
        print('and advise you if you should reorder them or not')
        print('   ')
    else:
        print('Please begin entering your values')
        print(' ')


# define the getValue() module
# Which will get the total of the invoice from the user
def getValue():
    while True:
        try:
            purchaseValue = float(input('Please enter the invoice total: $'))
            if purchaseValue <= 0.00:
                raise ValueError
        except ValueError:
            print('Cost cannot be less than zero')
            continue
        else:
            break
    return purchaseValue


# define the itemValue module
# Using a user controlled for loop and an accumulator we will collect the cost of each item
# and return their total
def itemValue():
    itemVal = 0.00
    while True:
        try:
            numItems = int(input('How many items would you like to '
                                 'markdown?: '))
            if numItems <= 0:
                raise ValueError
            else:
                break
        except ValueError:
            print('Number of items must be more than 0')
            continue

    # Run a for loop controled by the input of numItems
    for counter in range(1, numItems + 1):
        # use a nested while True loop to validate that the cost
        # is not 0; if it is keep telling the user
        while True:
            try:
                cost = float(input('amount off item ' + str(counter) + ' $'))
                if cost <= 0.00:
                    raise ValueError
            except ValueError:
                print('Cost cannot be less than zero')
                continue
            # if the cost is all good - break out of this loop
            # and continue with the for loop
            else:
                break
        itemVal = itemVal + cost
    return itemVal


# Declare the redeuced by module to calculate the sum of the markdowns
def redeucedby(x, y):
    sum = x - y
    return sum


# declare the lossPercent() which will take the shipmentValue and
# markdownAmount as arguments to conver the loss to a percentage

def lossPercent(a, b):
    # When calculating percent we know the maths is
    # x/y = (y/x) * 100
    # This module will not do the multiplication - it will only do the division
    # as the main module will format this output and the format('%') function will
    # actually perform the multiplication when it formats the floating point number
    perHundred = (b / a)
    return perHundred


# declare the lossAlert()
# Which uses a decision structure to decide which message to output
# which takes markdownPercentage as an argument

def lossAlert(z):
    print(' ')
    if z > 100:
        print(' High losses reported, please review order flow ')
    elif z > 30:
        print(' Please don\'t order anymore ')
    else:
        print(' Low losses reported. \n Please track sales on items ', sep='')
        print(' to determine if you should keep them on hand ')
    return z


# declare the main()

def main():
    again = 'y'
    while again:
        firstRun = newUserMsg()
        shipmentValue = getValue()
        itemCost = itemValue()
        markdownAmount = redeucedby(shipmentValue, itemCost)
        markdownPercentage = lossPercent(shipmentValue, itemCost)
        message = lossAlert(itemCost)
        print(' ')
        print('You spent: $', format(shipmentValue, ',.2f'), sep='')
        print('You did a total markdown for: $', format(itemCost, ',.2f'),
              sep='')
        print('Which is: ', format(markdownPercentage, '.1%'), sep='')
        again = input('Would you like to do another invoice? (y/n): ')
        # convert it to lower so it can be case insensitive
        again = again.lower()
        # if the user enters anything other than y or yes break
        if again != 'y' and again != 'yes':
            print('Thanks for using me!')
            break


main()
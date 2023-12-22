# Question 1 
# Complete the code to output the statement, “Marjery lives at her home address of 1234 Mockingbird Lane”. Remember that precise syntax must be used to receive credit.
name = "Marjery"
home_address = "1234 Mockingbird Lane"
print(name + " lives at her home address of " + home_address)
# Should print "Marjery lives at her home address of 1234 Mockingbird Lane"

# Question 2
# What's the value of this Python expression: "big" > "small"?
# Ans：
# False 

# Question 3
# What directly follows the elif keyword in an elif statement?
# Ans:
# A comparsion 

# Question 4
# Consider the following scenario about using if-elif-else statements:
# Police patrol a specific stretch of dangerous highway and are very particular about speed limits.  The speed limit is 65 miles per hour. Cars going 80 miles per hour or more are given a “Reckless Driving” ticket. Cars going more than 65 miles per hour are given a “Speeding” ticket.  Any cars going less than that are labeled “Safe” in the system.  
# Fill in the blanks in this function so it returns the proper ticket type or label.

def speeding_ticket(speed):
    if speed > 80:
        ticket = "Reckless Driving"
    elif speed > 65:
        ticket = "Speeding"
    else:
        ticket = "Safe"
    return ticket


print(speeding_ticket(87)) # Should print Reckless Driving
print(speeding_ticket(66)) # Should print Speeding
print(speeding_ticket(65)) # Should print Safe
print(speeding_ticket(85)) # Should print Reckless Driving
print(speeding_ticket(35)) # Should print Safe
print(speeding_ticket(77)) # Should print Speeding

# Question 5
# In the following code, what would be the output?
test_num = 12
if test_num > 15:
    print(test_num / 4)
else:
    print(test_num + 3)
# Ans :
# 15

# Question 6
# Fill in the blanks to complete the function.  The character translator function receives a single lowercase letter, then prints the numeric location of the letter in the English alphabet.  For example, “a” would return 1 and “b” would return 2. Currently, this function only supports the letters “a”, “b”, “c”, and “d” It returns "unknown" for all other letters or if the letter is uppercase.
def letter_translator(letter):
    if letter == "a":
        letter_position = 1
    elif letter == "b":
        letter_position = 2
    elif letter == "c":
        letter_position = 3
    elif letter == "d":
        letter_position = 4
    else:
        letter_position = "unknown"
    return letter_position


print(letter_translator("a")) # Should print 1
print(letter_translator("b")) # Should print 2
print(letter_translator("c")) # Should print 3
print(letter_translator("d")) # Should print 4
print(letter_translator("e")) # Should print unknown
print(letter_translator("A")) # Should print unknown
print(letter_translator("")) # Should print unknown

# Question 7
# Can you calculate the output of this code?
def sum(x, y):
        return(x+y)
print(sum(sum(1,2), sum(3,4)))

# Ans : 
# 10

# Question 8
# What's the value of this Python expression?
((24 == 5*2) and (24 > 3*5) and (2*6 == 12))
# Ans:
# False

# Question 9
# Fill in the blanks to complete the function. The fractional_part function divides the numerator by the denominator, and returns just the fractional part (a number between 0 and 1). Complete the body of the function so that it returns the right number. Note: Since division by 0 produces an error, if the denominator is 0, the function should return 0 instead of attempting the division.
def fractional_part(numerator, denominator):
    # Operate with numerator and denominator to
    # keep just the fractional part of the quotient 
    if denominator == 0 or denominator == numerator or numerator == 0:
        part = 0
    else:
        part = (numerator%denominator)/denominator
    return part


print(fractional_part(5, 5)) # Should print 0
print(fractional_part(5, 4)) # Should print 0.25
print(fractional_part(5, 3)) # Should print 0.66...
print(fractional_part(5, 2)) # Should print 0.5
print(fractional_part(5, 0)) # Should print 0
print(fractional_part(0, 5)) # Should print 0


# Question 10 
# Which of the following are good coding-style habits? Select all that apply.
# Ans: 
# Cleaning up duplicate code by creating a function that can be reused
# Adding comments
# Refactoring the code


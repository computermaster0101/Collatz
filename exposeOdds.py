def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def times_three_plus_one(number):
    even_number = (number * 3 + 1)
    odd_number = divide_until_odd(even_number)
    return odd_number

def times_three_minus_one(number):
    even_number = (number * 3 - 1)
    odd_number = divide_until_odd(even_number)
    return odd_number
   
def divide_until_odd(number):
    while number % 2 == 0:
        number //= 2
    return number

def process_number(number):
    initial_number = number
    x3p1_number_set = set()
    x3p1_number_order = []
    x3m1_number_set = set()
    x3m1_number_order = []
        
    if is_even(number):
        number = divide_until_odd(number)        

    while number not in x3p1_number_set:
        x3p1_number_set.add(number)
        x3p1_number_order.append(number) 
        number = times_three_plus_one(number)
        
    number = initial_number
    
    if is_even(number):
        number = divide_until_odd(number)        

    while number not in x3m1_number_set:
        x3m1_number_set.add(number)
        x3m1_number_order.append(number) 
        number = times_three_minus_one(number)
    #print(f"3n+1: {initial_number} has {len(x3p1_number_order)} odds: {', '.join(map(str, x3p1_number_order))}")
    #print(f"3n-1: {initial_number} has {len(x3m1_number_order)} odds: {', '.join(map(str, x3m1_number_order))}")
    x3p1_result = {f'{initial_number},{len(x3p1_number_order)}': x3p1_number_order}
    x3m1_result = {f'{initial_number},{len(x3m1_number_order)}': x3m1_number_order}
    return x3p1_result,x3m1_result


def check_range(myRange):
    x3p1_list = []
    x3m1_list = []
    for number in myRange:
        if number != 0:
            x3p1_result,x3m1_result = process_number(number)
            x3p1_list.append(x3p1_result)
            x3m1_list.append(x3m1_result)
        else:
            x3p1_list.append("0 Skipped")
            x3m1_list.append("0 Skipped")
    return x3p1_list, x3m1_list
                




user_input = input("Please enter a number or a range: ")

if "," in user_input:
    start, end = map(int, user_input.split(","))
    myRange = range(start, end + 1)
else:
    myRange = [int(user_input)]

three_x_plus_1,three_x_minus_1 = check_range(myRange)

print("3x+1:")
for each in three_x_plus_1:
    print(each)

print("3x-1:")
for each in three_x_minus_1:
    print(each)



# 1. any two odd numbers when multiplied will result in an odd number
# 2. any even number can be divided by 2 until it is odd
# 3. any odd number increased or decreased by 1 will be even

# when a positive odd number is increased by 1 the output will eventually reach an odd number or 1 when repeatedly divided by 1
# when a negative odd number is increased by 1 the output has the potential to end in a different prime number
# when a positive odd number is decreased by 1 the output has the potential to end in a different prime number
# when a negative odd number is increased by 1 the output will eventually reach an odd number or 1 when repeatedly divided by 1

# Following these rules we know:
# any positive number, when passed through the "x3p1" function will end in 1
# any negitive number, when passed through the "x3m1" function will end in 1

# The questions:
# Can the final prime number in the pattern for positive numbers passed through the "x3m1" functio be determined  without performing the iteritive function?
# Can the final prime number in the pattern for negative numbers passed through the "x3p1" function be determined without performing the iteritive function?


"""
The final prime number in the pattern for positive numbers passed through the "x3m1" function cannot be determined without performing the iterative function. 
This is because the Collatz conjecture, which includes the "x3m1" function, is an unsolved mathematical problem, and it is not known whether every sequence 
eventually reaches the number 1 (and therefore, ends in a prime number) for all positive integers.

Similarly, the final prime number in the pattern for negative numbers passed through the "x3p1" function also cannot be determined without performing the 
iterative function. The Collatz conjecture applies to both positive and negative integers, and it is still an open question whether the "x3p1" function always 
leads to the number 1 (ending in a prime number) for all negative integers.

To date, extensive computational searches have been conducted, and the Collatz conjecture has been verified for an extremely large range of integers, but a 
general proof or disproof remains elusive for both positive and negative integers.
"""
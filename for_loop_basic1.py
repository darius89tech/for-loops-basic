# Task 1:  Printing all integers from 0 to 150.
print("Task 1: Printing all integers from 0 to 150.")
for i in range(151):
    print(i)

# Task 2: Multiples of Five - Printing all the multiples of 5 from 5 to 1,000.
print("\nTask 2: Printing all the multiples of 5 from 5 to 1,000.")
for i in range(5, 1001, 5):
    print(i)

# Task 3: Counting, the Dojo Way - Printing integers 1 to 100. 
# If divisible by 5, printing "Coding" instead. If divisible by 10, printing "Coding Dojo".
print("\nTask 3: Printing integers 1 to 100.If divisible by 5, printing Coding instead. If divisible by 10, printing Coding Dojo. ")
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# Task 4: Whoa. That sucker's Huge - Adding odd integers from 0 to 500,000, and printing the final sum.
print("\nTask 4: Adding odd integers from 0 to 500,000, and printing the final sum ")
total = sum(i for i in range(500001) if i % 2 != 0)
print(total)

# Task 5: Countdown by Fours - Printing positive numbers starting at 2018, counting down by fours.
print("\nTask 5: Printing positive numbers starting at 2018, counting down by fours ")
for i in range(2018, 0, -4):
    print(i)

# Task 6: Flexible Counter - Setting three variables: lowNum, highNum, mult. 
# Starting at 2 and going through 37, printing only the integers that are a multiple of 4.
print("\nTask 6: Starting at 2 and going through 37, printing only the integers that are a multiple of 4 ")
lowNum = 2
highNum = 37
mult = 4
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)

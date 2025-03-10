print("program_start")
program_choice = int(input((
"""
Choose program:\n
0 - Exploring Python Concepts\n
1 - Explore Loops in Python\n
2 - Exploring String Methods\n
3 - Hands on Python Data Structures\n
4 - About Parameters of Functions\n
5 - Check your Knowledge on Errors\n
999 - to quit.
Program choice: 
"""
)))

if program_choice == 999:
    print("Exiting program")

elif program_choice == 0:
    print("TASK 1:")
    name = "James"
    age = "900"
    height = "7.0"

    print(f"Hey there, my name is {name}!\nI'm {age} years old and {height} feet tall.")

    print("\nTASK 2:")
    num_one = float(input("Enter num_one: "))
    num_two = float(input("Enter num_two: "))

    add_res = num_one + num_two
    sub_res = num_one - num_two
    mul_res = num_one * num_two
    div_res = num_one / num_two
    print(f"Addition op result for {num_one} and {num_two}: {add_res}")
    print(f"Subtraction op result for {num_one} and {num_two}: {sub_res}")
    print(f"Multiplication op result for {num_one} and {num_two}: {mul_res}")
    print(f"Division op result for {num_one} and {num_two}: {div_res}")

    print("\nTASK 3:")
    num_check = int(input("Enter a number to check whether it’s positive, negative, or zero.: "))

    if num_check > 0:
        print("This number is positive. Awesome!")
    elif num_check < 0:
        print("This number is negative. Better luck next time!")
    else:
        print("Zero it is. A perfect balance!")
    



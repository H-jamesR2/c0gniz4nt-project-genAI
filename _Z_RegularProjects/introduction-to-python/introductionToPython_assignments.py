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
    
elif program_choice == 1:
    print("TASK 1:")
    loop_num = int(input("Enter a starting number greater than 1: "))
    if loop_num < 1:
        print("Number is less than 1...")
    print('\n')
    while(loop_num > 0):
        print(loop_num)
        loop_num -= 1
    print("Blast off! 🚀")

    print("\nTASK 2:")
    mul_table_num = int(input("Enter a number: "))
    for i in range(1, 11, 1):
        mul_table_res = mul_table_num * i
        print(f"{mul_table_num} * {i} = {mul_table_res}")
        print("\n")

    print("\nTASK 3:")
    factorial_n = int(input("Enter a number: "))  
    factorial_memo = {0: 1}  # Base case for factorial(0)

    for i in range(1, factorial_n + 1):
        factorial_memo[i] = factorial_memo[i - 1] * i

    factorial_result = factorial_memo[factorial_n]
    print(f"The factorial of {factorial_n} is {factorial_result}")

elif program_choice == 2:
    print("TASK 1:")
    taskOne_string = "Python is amazing!"

    # Extract the first 6 characters (Python)
    first_word = taskOne_string[:6]

    # Extract the word "amazing"
    amazing_part = taskOne_string[11:18]

    # Extract the entire string in reverse order
    reversed_string = taskOne_string[::-1]

    # Print the slices with clear labels
    print("First word:", first_word)
    print("Amazing part:", amazing_part)
    print("Reversed string:", reversed_string)

    print("\nTASK 2:")
    taskTwo_string = " hello, python world! "

    # Use the strip() method to remove extra spaces
    stripped_string = taskTwo_string.strip()

    # Use the capitalize() method to capitalize the first letter
    capitalized_string = taskTwo_string.capitalize()

    # Use the replace() method to replace "world" with "universe"
    replaced_string = taskTwo_string.replace("world", "universe")

    # Use the upper() method to convert the string to uppercase
    uppercase_string = taskTwo_string.upper()

    # Print the results
    print("Stripped string:", stripped_string)
    print("Capitalized string:", capitalized_string)
    print("Replaced string:", replaced_string)
    print("Uppercase string:", uppercase_string)

    print("\nTASK 3:")
    pali_word = input("Enter a word: ")

    # Use slicing to reverse the string
    reversed_word = pali_word[::-1]

    # Compare the original word with the reversed word
    if pali_word == reversed_word:
        print(f"Yes, '{pali_word}' is a palindrome!")
    else:
        print(f"No, '{pali_word}' is not a palindrome.")


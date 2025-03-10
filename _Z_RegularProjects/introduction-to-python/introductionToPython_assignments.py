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

elif program_choice == 3:
    print("TASK 1:")
    fruits = ['apple', 'banana', 'blueberry', 'pineapple', 'orange']

    # Print the original list
    print("Original list:", fruits)

    # Append a new fruit to the list
    fruits.append('fig')
    print("After adding a fruit:", fruits)

    # Remove one fruit from the list using the remove() method
    fruits.remove('blueberry')
    print("After removing a fruit:", fruits)

    # Print the list in reverse order using slicing
    reversed_fruits = fruits[::-1]
    print("Reversed list:", reversed_fruits)
    
    print("\nTASK 2:")
    # Create a dictionary with personal information
    personal_info = {
        "name": "Alice",
        "age": 21,
        "city": "New York"
    }

    # Add a new key-value pair for "favorite color"
    personal_info["favorite color"] = "Green"
    personal_info["occupation"] = "Political Scientist"

    # Update the "city" key with a new value
    personal_info["city"] = "Washington"
    personal_info["name"] = "Eleanor"

    personal_info["age"] = -1

    # Print all the keys and values using a loop
    print("Keys:", ", ".join(personal_info.keys()))
    print("Values:", ", ".join(map(str, personal_info.values())))

    print("\nTASK 3:")
    # Create a tuple with three elements: favorite movie, song, and book
    favorite_things = ('Inception', 'ABCD - Nayeon', 'Why Nations Fail')

    # Print the tuple
    print("Favorite things:", favorite_things)

    # Try to change one of the elements (this will raise an error)
    try:
        favorite_things[0] = 'The Matrix'  # Attempting to change the movie
    except TypeError:
        print("Oops! Tuples cannot be changed.")

    # Print the length of the tuple
    print("Length of tuple:", len(favorite_things))

elif program_choice == 4:
    print("TASK 1:")

    def greet_user(name):
        print(f"Hello, {name}! Welcome aboard.")

    def add_numbers(num1, num2):
        return num1 + num2

    # Example usage
    user_name = "Alice"
    greet_user(user_name)

    # Add two numbers and display the result
    num1, num2 = 5, 10
    sum_result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {sum_result}.")

    print("\nTASK 2:")
    def describe_pet(pet_name, animal_type="dog"):
        print(f"I have a {animal_type} named {pet_name}.")

    # Example usage
    describe_pet("Buddy")  # Using the default animal type "dog"
    describe_pet("Whiskers", "cat")  # Specifying "cat" as the animal type

    print("\nTASK 3:")
    # make_sandwich function uses variable arguments
    def make_sandwich(*ingredients):
        print("Making a sandwich with the following ingredients:")
        for ingredient in ingredients:
            print(f"- {ingredient}")

    # Example usage
    make_sandwich("Lettuce", "Tomato", "Cheese", "Bacon")

    print("\nTASK 4:")
    # factorial made more efficient w/ slight caching.
    def factorial_memoization(n, memo={}):
        if n in memo:
            return memo[n]
        if n == 0:
            return 1
        memo[n] = n * factorial_memoization(n - 1, memo)
        return memo[n]

    def fibonacci_memoization(n, memo={}):
        """
        Calculates the nth Fibonacci number using recursion and memoization.

        Args:
            n: The index of the Fibonacci number to calculate (non-negative integer).
            memo: A dictionary to store previously calculated Fibonacci numbers.

        Returns:
            The nth Fibonacci number.
        """
        if not isinstance(n, int):
            print("Error: Input must be an integer.")
            return None

        if n < 0:
            print("Error: Input must be a non-negative integer.")
            return None

        if n in memo:
            return memo[n]

        if n <= 1:
            return n

        memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
        return memo[n]

    ## fixing ordinal numbers.
    def ordinal_suffix(number):
        """
        Returns the ordinal suffix (st, nd, rd, th) for a given integer.

        Args:
            number: The integer for which to determine the suffix.

        Returns:
            The ordinal suffix as a string.
        """
        if not isinstance(number, int):
            return ""  # Return empty string for non-integer inputs

        if 10 <= number % 100 <= 20:  # Handle teens (11th, 12th, ..., 20th)
            return "th"

        remainder = number % 10
        if remainder == 1:
            return "st"
        elif remainder == 2:
            return "nd"
        elif remainder == 3:
            return "rd"
        else:
            return "th"

    def format_ordinal(number):
        """
        Formats an integer with its ordinal suffix.

        Args:
            number: The integer to format.

        Returns:
            The formatted ordinal string (e.g., "1st", "2nd", "3rd").
        """
        return str(number) + ordinal_suffix(number)

    factorial_n = int(input("Enter a number to find factorial: "))
    fibonacci_n = int(input("Enter a number to find the fibonacci number: "))


    print(f"The factorial of {factorial_n} is {factorial_memoization(factorial_n)}")
    print(f"The {format_ordinal(fibonacci_n)} Fibonacci number is {fibonacci_memoization(fibonacci_n)}.")

elif program_choice == 5:
    print("TASK 1:")
    # Ask the user to enter a number
    try:
        user_input = input("Enter a number: ")
        number = float(user_input)  # Try to convert input to a float

        # Try to divide 100 by the number
        result = 100 / number
        print(f"100 divided by {number} is {result}")

    # Handle ZeroDivisionError
    except ZeroDivisionError:
        print("Oops! You cannot divide by zero.")

    # Handle ValueError for non-numeric input
    except ValueError:
        print("Invalid input! Please enter a valid number.")

    print("\nTASK 2:")
    # Example of handling IndexError
    try:
        my_list = [1, 2, 3]
        # Trying to access an invalid index (index 5 does not exist in the list)
        print(my_list[5])
    except IndexError:
        print("IndexError occurred! List index out of range.")

    # Example of handling KeyError
    try:
        my_dict = {"name": "Alice", "age": 25}
        # Trying to access a non-existent key "address"
        print(my_dict["address"])
    except KeyError:
        print("KeyError occurred! Key not found in the dictionary.")

    # Example of handling TypeError
    try:
        num = 10
        text = "Hello"
        # Trying to add an integer and a string, which raises a TypeError
        print(num + text)
    except TypeError:
        print("TypeError occurred! Unsupported operand types.")

    print("\nTASK 3:")
    # Prompt the user to enter two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Try to divide the first number by the second number
        result = num1 / num2

    except ZeroDivisionError:
        # Handle the case when the second number is zero
        print("Error! You cannot divide by zero.")
    except ValueError:
        # Handle invalid input if the user enters non-numeric values
        print("Error! Please enter valid numbers.")

    else:
        # This block is executed if no exception occurs
        print(f"The result is {result}.")

    finally:
        # This block always executes, regardless of whether an exception occurs or not
        print("This block always executes.")

else:
    print("Invalid Choice!")

print("\nprogram_end")
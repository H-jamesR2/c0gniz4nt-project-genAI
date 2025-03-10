print("program_start")
program_choice = int(input((
"""
Choose program:\n
0 - Eligible Electors\n
1 - Number Guessing\n
2 - Password Strength Checker\n
3 - Implementing Your Own Data Structures \n
4 - Menu Functioning\n
5 - Exception Handling (Calculator)\n
999 - to quit.
Program choice: 
"""
)))

if program_choice == 999:
    print("Exiting program")


elif program_choice == 0:
    # ask age
    age = int(input("How old are you? "))

    if age >= 18:
        print("Congratulations! You are eligible to vote. Go make a difference!")
    else:
        age_left = (18 - age)
        print(f"Oops! You’re not eligible yet. But hey, only {age_left} more years to go!")

elif program_choice == 1:

    import random
    number_to_guess = random.randint(1, 100)

    number_of_guesses = 1
    while number_of_guesses <= 10:
        num_guessed = int(input("Guess the number (between 1 and 100): "))
        if num_guessed == number_to_guess:
            print(f" {num_guessed} Congratulations! You guessed it in {number_of_guesses} attempts!")
            break
        elif num_guessed > number_to_guess:
            print(f" {num_guessed} Too high! Try again.")
        elif num_guessed < number_to_guess:
            print(f" {num_guessed} Too low! Try again.")

        number_of_guesses += 1

elif program_choice == 2:
    import re

    def check_password_strength(password):
        # Initialize a score for password strength
        score = 0
        messages = []
        
        # Check length of the password
        if len(password) >= 8:
            score += 2  # 2 points for length
        else:
            messages.append("Your password needs to be at least 8 characters long.")
        
        # Check for at least one uppercase letter
        if any(char.isupper() for char in password):
            score += 2  # 2 points for having uppercase letter
        else:
            messages.append("Your password needs at least one uppercase letter.")
        
        # Check for at least one lowercase letter
        if any(char.islower() for char in password):
            score += 2  # 2 points for having lowercase letter
        else:
            messages.append("Your password needs at least one lowercase letter.")
        
        # Check for at least one digit
        if any(char.isdigit() for char in password):
            score += 2  # 2 points for having a digit
        else:
            messages.append("Your password needs at least one digit.")
        
        # Check for at least one special character
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            score += 2  # 2 points for special character
        else:
            messages.append("Your password needs at least one special character.")
        
        # Final message
        if score == 10:
            print("Your password is strong! 💪")
        else:
            print("Your password isn't strong enough.")
        
        # Display all the messages
        for message in messages:
            print(message)
        
        # Bonus: Password strength meter (out of 10)
        print(f"Password Strength: {score}/10")

    # Step 1: Input the Password
    password = input("Enter a password: ")

    # Step 2: Evaluate the Password
    check_password_strength(password)

elif program_choice == 3:
    # Step 1: Create the Inventory
    inventory = {
        "apple": (10, 2.5),
        "banana": (20, 1.2)
    }

    # Function to display the inventory
    def display_inventory():
        print("Current inventory:")
        for item, (quantity, price) in inventory.items():
            print(f"Item: {item}, Quantity: {quantity}, Price: ${price}")

    # Step 2: Add, Remove, and Update Items

    # Function to add a new item to the inventory
    def add_item(item_name, quantity, price):
        inventory[item_name] = (quantity, price)
        print(f"Added {item_name} to the inventory.")

    # Function to remove an item from the inventory
    def remove_item(item_name):
        if item_name in inventory:
            del inventory[item_name]
            print(f"Removed {item_name} from the inventory.")
        else:
            print(f"Item {item_name} not found in inventory.")

    # Function to update the quantity or price of an existing item
    def update_item(item_name, quantity=None, price=None):
        if item_name in inventory:
            current_quantity, current_price = inventory[item_name]
            
            # Update quantity if provided
            if quantity is not None:
                current_quantity = quantity
            
            # Update price if provided
            if price is not None:
                current_price = price
            
            # Update the inventory
            inventory[item_name] = (current_quantity, current_price)
            print(f"Updated {item_name}: Quantity: {current_quantity}, Price: ${current_price}")
        else:
            print(f"Item {item_name} not found in inventory.")

    # Step 4: Bonus - Calculate Total Value
    def calculate_total_value():
        total_value = 0
        for quantity, price in inventory.values():
            total_value += quantity * price
        return total_value

    # Main Program
    def inventory_manager():
        print("Welcome to the Inventory Manager!\n")
        
        # Initial display of the inventory
        display_inventory()
        
        while True:
            print("\nChoose an option:")
            print("1. Add a new item")
            print("2. Remove an item")
            print("3. Update an item")
            print("4. Display current inventory")
            print("5. Calculate total value")
            print("6. Exit")
            
            choice = input("Enter your choice (1-6): ")
            
            if choice == "1":
                item_name = input("Enter item name: ")
                quantity = int(input(f"Enter quantity for {item_name}: "))
                price = float(input(f"Enter price for {item_name}: "))
                add_item(item_name, quantity, price)
            
            elif choice == "2":
                item_name = input("Enter item name to remove: ")
                remove_item(item_name)
            
            elif choice == "3":
                item_name = input("Enter item name to update: ")
                print("Leave the field blank if you don't want to update it.")
                quantity = input(f"Enter new quantity for {item_name} (current: {inventory.get(item_name, (0, 0))[0]}): ")
                price = input(f"Enter new price for {item_name} (current: {inventory.get(item_name, (0, 0))[1]}): ")
                
                # Convert inputs to correct types or None if blank
                quantity = int(quantity) if quantity else None
                price = float(price) if price else None
                update_item(item_name, quantity, price)
            
            elif choice == "4":
                display_inventory()
            
            elif choice == "5":
                total_value = calculate_total_value()
                print(f"Total value of inventory: ${total_value:.2f}")
            
            elif choice == "6":
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice, please try again.")

    # Run the inventory manager
    inventory_manager()
         
elif program_choice == 4:
    # RECURSIVE FUNCTIONS:

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

    import turtle

    def draw_tree(branch_len, t, angle, min_branch_len):
        """
        Draws a fractal tree using recursion.

        Args:
            branch_len: The length of the current branch.
            t: The turtle object.
            angle: The angle of the branches.
            min_branch_len: The minimum branch length to draw.
        """
        if branch_len > min_branch_len:
            t.forward(branch_len)
            t.right(angle)
            draw_tree(branch_len - 15, t, angle, min_branch_len)  # Recursive call for right branch

            t.left(2 * angle)
            draw_tree(branch_len - 15, t, angle, min_branch_len)  # Recursive call for left branch

            t.right(angle)
            t.backward(branch_len)

    def treeProgram():
        """Sets up the turtle and draws the fractal tree."""
        screen = turtle.Screen()
        screen.bgcolor("white")

        t = turtle.Turtle()
        t.speed(0)  # Fastest speed
        t.left(90)  # Start pointing upwards
        t.penup()
        t.backward(100)
        t.pendown()
        t.color("brown")

        draw_tree(100, t, 20, 10)  # Initial branch length, angle, and minimum branch length.
        screen.mainloop()

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

    def main():
        choice_ = int(input(
        """
        Choose an option: 
        1. Calculate Factorial 
        2. Find Fibonacci 
        3. Draw a Recursive Fractal 
        4. Exit
        """
        ))

        if choice_ == 1:
            factorial_n = int(input("Enter a number to find its factorial: "))
            print(f"The factorial of {factorial_n} is {factorial_memoization(factorial_n)}")
        elif choice_ == 2:
            fibonacci_n = int(input("Enter the position of the Fibonacci number: "))
            print(f"The {format_ordinal(fibonacci_n)} Fibonacci number is {fibonacci_memoization(fibonacci_n)}.")
        elif choice_ == 3:
            treeProgram()
        elif choice_ == 4:
            print("Exiting Recursion Program")
            pass

elif program_choice == 5:
    import logging

    # Configure logging
    logging.basicConfig(filename='error_log.txt', level=logging.ERROR,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    def get_number(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                logging.error("ValueError: Invalid number input")

    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Oops! Division by zero is not allowed.")
            logging.error("ZeroDivisionError: Division by zero attempted")
            return None

    def main():
        while True:
            print("\nWelcome to the Error-Free Calculator!")
            print("Choose an operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exit")
            
            choice = input("> ")
            
            if choice == '5':
                print("Goodbye!")
                break
            
            if choice not in ('1', '2', '3', '4'):
                print("Invalid choice! Please select a valid option.")
                continue
            
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            
            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                result = divide(num1, num2)
                if result is not None:
                    print("Result:", result)

    if __name__ == "__main__":
        main()
        
else:
    print("Invalid Choice!")

print("program_end")
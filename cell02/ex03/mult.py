#!/usr/bin/env python3

def main():
    # Prompt for two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Multiply the numbers
        result = num1 * num2
        
        # Determine if the result is positive, negative, or zero
        if result > 0:
            sign = "positive"
        elif result < 0:
            sign = "negative"
        else:
            sign = "zero"
        
        # Display the result
        print(f"The result of multiplying {num1} and {num2} is {result}, which is {sign}.")
    
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()

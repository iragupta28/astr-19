# Write a Python program that prints the sum of two floating point numbers, the difference between two integers, and the product of a floating point number and an integer. In each case, have the program print out the data type of the resulting answer.

# defining a function to do the math
def math(x,y):
    print("x + y = ", (float(x))+(float(y)))
    print("x - y = ", (int(x))-(int(y)))
    print("x * y = ", (float(x))*(int(y)))

# defining the main function
def main():
    x = input("Enter a number (x): ")
    y = input("Enter a second number (y): ")
    
    math(x,y)
    
if __name__ == "__main__":
    main()
    

# Write a Python that prints the sum of two floating point numbers, the difference between two integers, and the product of a floating point number and an integer. In each case, have the program print out the data type of the resulting answer.

# addition function
def add1():
    a = 2.0
    b = 10.6
    addition = a + b
    x = print(f"{a} + {b} = {a+b}")
    print(type(addition))
    print(" ") # to have spaces between the operations
    
# subtraction function
def subtract1():
    c = 208
    d = 167
    subtraction = c - d
    y = print(f"{c} - {d} = {c-d}")
    print(type(subtraction))
    print(" ")
    
# multiplication function
def multiply1():
    e = 7.8
    f = 3
    multiplication = e * f
    z = print(f"{e} * {f} = {e*f}")
    print(type(multiplication))
    print(" ")
    
def main():
    add1()
    subtract1()
    multiply1()
              
if __name__ == "__main__":
    main()
    

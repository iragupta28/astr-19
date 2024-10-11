# Write a Python program that defines a function f(x) that returns x**3 + 8. In the main function of the program, call f(x) with x = 9 and print the result.  Use an if statement that executes if the result is larger than 27 and prints “YAY!”.

import math
import numpy as np

def function1(x):
    result = ((x**3) + 8)
    return(result)
    
def main():
    result2 = function1(9)
    print(result2)
    if result2 > 27:
        print("YAY!")
    else:
        pass

if __name__ == "__main__":
    main()
    

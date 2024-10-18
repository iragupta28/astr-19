# Write a Python program that writes out a table of the function sin(x) vs. x, where x is tabulated between 0 and 2 with a thousand entries. Follow the basic Python program structure, including a main program function.

import numpy as np

def journal5():
    x = np.linspace(0, 2*np.pi, 1000)
    y = np.sin(x)
    
    answer = np.zeros(shape=(1000,2))
    
    answer[:, 0] = x #this sets x as the first column of answer
    answer[:, 1] = y
    
    print(answer)
    
def main():
    journal5()
    
if __name__ == "__main__":
    main()

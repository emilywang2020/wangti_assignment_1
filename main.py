# Author: Ting-Chen Wang
# Computational Biology Spring 2020
# Assignment 1
# Due Date: 1/26/2020
# main

import sys
import re
import string
from checkSequence import checkSequence  # import the checkSequence class


# The main function
def main():
    if len(sys.argv) == 2:  # take two command line arguments, the python file and the method
        method = sys.argv[1]
        # if the name of method is not correct, output an error message and exit the program
        if method != "method_1" and method != "method_2":
            sys.exit("Invalid method")

        else:
            sequence = input("Enter a DNA Sequence: \n")  # ask for a sequence from the standard input
            x = checkSequence(sequence)  # create an object of the checkSequence class
            if not x.isSequence():  # call isSequence function to check if a sequence is valid
                sys.exit("Invalid sequence!")  # if it is not valid, print out an error message and exit the program.
                # otherwise, process the sequence according to the indicated method
            else:
                # method_1 reverses the input sequence first. It then uses a for loop to  find the complement base
                # at each position based on the conditions specified in the if, elif, and else statement.
                # The final result is printed by the standard output.
                print(type(sys.argv[1]))
                if sys.argv[1].find("method_1"):
                    print("reverse complement sequence: ", end='')
                    dna_reverse = x.sequence[::-1]
                    # for each base in the reversed sequence
                    for i in dna_reverse:
                        # If the base if A, the complement base T will be printed.
                        if i == 'A':
                            print('T', end='')
                        # If the base if T, the complement base A will be printed.
                        elif i == 'T':
                            print('A', end='')
                        # If the base if C, the complement base G will be printed.
                        elif i == 'C':
                            print('G', end='')
                        # Otherwise, the complement base C will be printed.
                        else:
                            print('C', end='')
                    # output formatting
                    print("")

                # method_2 uses two built-in functions, maketrans() and translate(), to find the complement
                # base at each position first. The result is then being reversed to find the reverse complement sequence.
                # The final result is printed by the standard output.
                elif sys.argv[1].find("method_2"):
                    print("reverse complement sequence: ", end='')
                    original = "ACGT"
                    reverse = "TGCA"
                    translation = x.sequence.maketrans(original, reverse)
                    result = x.sequence.translate(translation)
                    print(result[::-1])

                # print an error message
                else:
                    print("Please enter either method_1 or method_2 for the method.")

    else:  # print out an error message indicating the wrong number of commandline arguments
        sys.exit("The number of arguments is not correct.")


if __name__ == '__main__':
    main()

# Author: Ting-Chen Wang
# Computational Biology Spring 2020
# Assignment 1
# Due Date: 1/26/2020
# class checkSequence

import sys
import re

class checkSequence:
    # parameterized constructor that takes a sequence in the parameter
    def __init__(self, sequence):
        self.sequence = sequence

    # This function checks if a sequence is valid
    def isSequence(self):
        # capitalize all the bases in the sequence
        dna_sequence = self.sequence.upper()
        # compile a regular expression pattern that includes characters other than "ACGT" to find_pattern object
        find_pattern = re.compile('[^ACGT]')
        # call .findall() to find all non-overlapping matches that contain bases other than ACGT
        pattern = find_pattern.findall(dna_sequence)
        # if a sequence contains bases other than "ACGT," return false to indicate that this sequence is invalid
        if pattern:
            return False
        # otherwise, assign the input sequence to self.sequence and return true
        else:
            self.sequence = dna_sequence
            return True

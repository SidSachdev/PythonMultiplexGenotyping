#!/usr/bin/env python3
"""

Problem: Multiplex Genotyping
Solution: Using the data given, we segregate the data into the mutations and normals. We focus on the mutations and try
          to map them with the normals. The concept is to iterate through the lines of the input file and do the
          processing in a batch. Once the processing is finished, the output returns to the text file. After that,
          our data dictionary gets flushed and resets to a blank dictionary, hence, saving memory space.
          (Additional Test Cases along with their output is provided Below)

Time Complexity of Solution: O(n log(n)) As we're iterating and sorting the data as well, I believe the time complexity
                            would be O(n log(n)).
"""
__author__ = "Sid Sachdev"

# Standard Input/Output Files
fileopen = open("input.txt", "r")
openfile = open('output.txt', 'w')
lines = fileopen.readlines()

# Outside Libraries
import collections

# Initial Declarations
data = {}
mutationList = []


def processValues(data, mutationList):
    """
    A function used to process the values in the data dictionary.

    :param data: A dictionary that gets iterated while maintaining the data and their states.
                The key values are the numbers that are associated with their states (Normal, Mutation, Unknown)
                The unknown is for initial iteration purposes. If it remains after a pass, it helps us understand
                that the data has an abnormality.
    :param mutationList: A Mutation List that keeps a record of all the mutations


    :return: Prints the Output to the text File as required.
    """
    # An inconsistency boolean offset that prevents unnecessary iterations
    inconsistency = False

    # Processing of Mutants by iterating through the list
    for muts in mutationList:
        count = 0
        elem = -1
        for m in muts:
            # While iterating through the list, we check if the data exists
            if not data.get(m) or data.get(m) != "NORM":
                # An unknown setter as we wouldn't know in the first pass whether the Mutation is truly a Mutation
                data[m] = "UNKNOWN"
                count += 1
                elem = m
        # Here, we are dealing with inconsistencies.
        # If our count remains at 0, we can presume there's an inconsistency and flip the switch (bool value)
        if count == 0:
            inconsistency = True
            break
        # If our count is at 1, we can set it's state to a Mutation
        if count == 1:
            data[elem] = "MUT"
    # If our inconsistency is True, we state that as an answer.
    if inconsistency:
        openfile.write("INCONSISTENT" + '\n' + '\n')
    else:
        # If it's false, AND we're still dealing with an "Unknown", we can set it to Non-unique.
        if 'UNKNOWN' in data.values():
            openfile.write("NONUNIQUE" + '\n' + '\n')
        # We can now deal with the cases where the data is a normal mapping
        else:
            # Counter Variables for our Mutations and Normal values
            counterMut = 0
            counterNorm = 0

            for values in data.values():
                if values == "NORM":
                    counterNorm += 1
                else:
                    counterMut += 1

            openfile.write("MUT COUNT: " + str(counterMut) + '\n')
            openfile.write("NORM COUNT: " + str(counterNorm) + '\n')

            # As our keys are string values, to sort them, we must map them as integer values in a temp Dictionary
            # We use an ordered dictionary here, to pass information from the tempData
            # Finally, we return the output of the sorted Mutations, Normal values to the text file.
            tempData = {int(k): str(v) for k, v in data.items()}
            tempData = collections.OrderedDict(sorted(tempData.items()))
            for k, v in tempData.items(): openfile.write(str(k) + "," + str(v) + '\n')
            openfile.write('\n')


# Using the fileopen function above, we're now iterating through the lines.
for line in lines:
    # As a new line represents a new user, we work through it accordingly.
    if line != "\n":
        line = line.rstrip()
        splits = line.split(",")
        # We segregate the Mutations and Normals
        if splits[0] == "NORM":
            for s in splits[1:]:
                # We use the numbers as keys to represent the Mutation/Normal
                data[s] = "NORM"
        else:
            mutationList.append(splits[1:])
    else:
        # We call the processValues function and flush the data for a new user.
        processValues(data, mutationList)
        data = {}
        mutationList = []
"""
Additional Test Cases for Edge cases
---------------------------------------------------------------------------------------------------
Additional Test Case 1: We edit the given input (user 2 in input file) file that returns a norm count and 
                        mut count, but in this test case, we will take off MUT,49 to represent that it will become
                        NON-UNIQUE.  

NORM,11,44,118,11
MUT,49,83
NORM,122,43,98
MUT,83
NORM,146,122,121
NORM,11,100,50

Output: Non-Unique 
---------------------------------------------------------------------------------------------------
Additional Test Case 2: A test to check the inconsistencies.

NORM,0,110
NORM,110,330
NORM,123,4530
MUT,110,4530

Output: Inconsistent

"""

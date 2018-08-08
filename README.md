# PythonMultiplexGenotyping
Using the data given, we segregate the data into the mutations and normals. We focus on the mutations and try to map them with the normals.


Problem: Multiplex Genotyping
Solution: Using the data given, we segregate the data into the mutations and normals. We focus on the mutations and try
          to map them with the normals. The concept is to iterate through the lines of the input file and do the
          processing in a batch. Once the processing is finished, the output returns to the text file. After that,
          our data dictionary gets flushed and resets to a blank dictionary, hence, saving memory space.
          (Additional Test Cases along with their output is provided Below)

Time Complexity of Solution: O(n log(n)) As we're iterating and sorting the data as well, I believe the time complexity
                            would be O(n log(n)).



### Main Function:

def processValues(data, mutationList):
    
    A function used to process the values in the data dictionary.

    :param data: A dictionary that gets iterated while maintaining the data and their states.
                The key values are the numbers that are associated with their states (Normal, Mutation, Unknown)
                The unknown is for initial iteration purposes. If it remains after a pass, it helps us understand
                that the data has an abnormality.
    :param mutationList: A Mutation List that keeps a record of all the mutations


    :return: Prints the Output to the text File as required.


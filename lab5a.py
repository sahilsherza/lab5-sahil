#!/usr/bin/env python3

# Author ID: [124876228]



def read_file_string(file_name):

    """Takes file_name as a string and returns its entire contents as a string."""

    with open(file_name, 'r') as f:

        return f.read()



def read_file_list(file_name):

    """Takes file_name as a string and returns its entire contents as a list of lines without new-line characters."""

    with open(file_name, 'r') as f:

        lines = f.readlines()

        return [line.strip() for line in lines]  # Remove newline characters from each line



if __name__ == '__main__':

    file_name = 'data.txt'

    print(read_file_string(file_name))

    print(read_file_list(file_name))



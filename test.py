

def read_even_numbered_lines(file_name):
    """ Reads in the even numbered lines of a file

    [IMPLEMENT ME]
        1. Open and read the given file into a variable
        2. Read the file line-by-line and add the even-numbered lines to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list of the even-numbered lines of the file
    """
    # WRITE SOLUTION HERE
    list = []
    with open(file_name) as f:
        for index, line in f:
            if index % 2 == 0:
                list.append(line)
    return list

def print_alternating(file_name, n):
    # open the file using the open function that takes the file name and the access mode hence 
    # returnig the opened file object
    open_file = open(file_name, 'r') # open the file in read mode
    # The readlines function reads all the lines at once and returns a list
    # containing each line in the file as a list item.
    lines = open_file.readlines()
    
    start_position = 0 # keeps track of which position to start reading from in a line; it's reset to 0 in case of a blank line or to 1 if the nth word has been reached
    
    # using for loop, go through all the lines in the file
    for line in lines:     
        # strip the new line character from the line
        line = line.strip()
        # split the line into a list of words using white space
        words = line.split(" ")

        # maintain the sequence, if start_position is equal to n then reset the start position to 0
        if start_position == n:
            start_position = 0
        # ensure the words start at the correct position by removing the words before the start_position
        words = words[start_position:]
        # get all the nth words
        for word in words[::n]:
            # print the nth word
            print(word, end=" ")
        # break to new line
        print("")
        # increment the start position
        start_position += 1

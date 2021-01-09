def spacer(string_value, length):
    """method to take a string of less then length and add the number of spaces to be length"""
    output_string = ""
    #print(string_value)
    if len(string_value) < length:
        added_space = " "*(length-len(string_value)-1)
        output_string = " "+string_value+added_space
    return output_string

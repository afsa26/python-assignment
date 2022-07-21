#write a python program to get a string made of the first 2
# chars from a given string lenghth is less than 2.return 
# instead of the empty string.
# Go to the editor
# sample string:"w3resource"
# expected result:"w3ce"
# sample string:"w3"
# expected result:"w3w3"
# sample string:"w"
# expected result:Empty string 
def string_both_ends(str):
    if len(str)<2:
        return ''
    return str[0:2]+str[-2:]
    print(string_both_ends("w3resource"))
    print(string_both_ends("w3"))
    print(string_both_ends('w'))













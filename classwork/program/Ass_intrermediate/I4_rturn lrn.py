#write a python function to reverse a string if its length multiple of 4
def reverse_string(a):
    if len(a)%4==0:
        return''.join(reversed(a))
        return a
        print(reverse_string('abcd'))

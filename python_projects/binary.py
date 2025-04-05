# This function use normal text string to convert into it as a binary code!

def binary_code(data):
    return " ".join(format(ord(i),'b')for i in data)

print(binary_code('stay out of that girl'))


#This function use binary code to convert into it as a normal text string!
def normal_text(code):
    return "".join((chr(int(x,2)))for x in code.split(" "))

print(normal_text('1110011 1110100 1100001 1111001 100000 1101111 1110101 1110100 100000 1101111 1100110 100000 1110100 1101000 1100001 1110100 100000 1100111 1101001 1110010 1101100'))


#This function get the value of what the output of "binary_code()"return and convert into it as a normal text string!
def normal_text(mix):
    return "".join((chr(int(x,2)))for x in mix.split(' '))

print(normal_text(binary_code('stay out of that girl')))

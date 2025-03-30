datetime1 = [2025,12,2]
datetime2 = [2024,2,21]
def compare(first,second):

    if first[0]>second[0]:
        return "True"
    elif first[0]<second[0]:
        return "False"
    elif first[1]>second[1]:
        return "True"
    elif first[1]<second[1]:
        return "False"
    elif first[2]>second[2]:
        return "True"
    elif first[2]<second[2]:
        return "False"
    else:
        return 0

print(compare(datetime1,datetime2))
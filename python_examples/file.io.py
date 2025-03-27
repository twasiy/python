def chek_for_word():
    with open('sample . txt', 'r') as f:
        data = f.read()
        if('learning'in data):
            print('FOUND!')
        else:
            print('NOT FOUND!')

chek_for_word()

def chek_for_line():
    with open('sample . txt', 'r') as f:
        data = True
        line_no = 1
        while data:
            data = f.readline()
            if('learning'in data):
                print( 'The line number is:',line_no)
                return
            line_no +=1
    return 'There is nothing about it'
chek_for_line()



with open('demo.txt','r') as f:
    data= f.read()
    count = 0
    nums = data.split(',')
    for i in nums:
        if(int(i) % 2 == 0):
            count+=1


print(count)

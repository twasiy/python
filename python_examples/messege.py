try:
    num =int(input("Enter a number: "))
except:
    print("Invalid input")
   

print(f"The multiplication table of {num} is")

try:
    for i in range(1,11):
        print(f"{num}x{i}={num*i}")

except:
    print("Something went wrong")


print("This line is very important")

    
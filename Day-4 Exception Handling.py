# # Try and Except
a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")
try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a) * i}")
except:
    print("Invalid Input")

print("Some imp lines of code")
print("End of program")

try: 
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Index Error")

# # Finally Clause 
def func1():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occurred")
        return 0
    finally:
        print("I am always executed")
    # print("I am always executed")
x = func1()
print(x)

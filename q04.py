import sys

number_list=[]
print("enter numbers")

for line in sys.stdin:
    try:
        num = float(line)  
        number_list.append(num)
    except ValueError:
        break  

print("list:")

for num in reversed(number_list):
    print(num)

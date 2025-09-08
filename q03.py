import sys

print("enter numbers")
max_number=float(sys.stdin.readline().strip())

for num in sys.stdin:
    try:
          num=float(num)
          if(num>max_number):
             max_number=float(num)
    except ValueError:
         break

print(f"the mux number is: {max_number}")
       
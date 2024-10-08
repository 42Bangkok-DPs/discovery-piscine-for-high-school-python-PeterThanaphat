number = int(input("Enter a number for the multiplication table: "))
print(f"Multiplication Table for {number}:")
for i in range(0, 10):
    result = number * i
    print(f"{number} x {i} = {result}")
    



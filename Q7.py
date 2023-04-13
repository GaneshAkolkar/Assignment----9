# 7. Write a python script to print first N even natural numbers in reverse order


n = int(input("Enter the value of N: "))

for i in range(2*n, 0, -2):
    print(i)

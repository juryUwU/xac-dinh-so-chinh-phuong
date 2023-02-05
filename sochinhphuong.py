n = int(input("so n:"))
for i in range(1, n + 1):
    if i**2 == n:
        print(n, "là số chính phương")
    
    elif i**2 != n:
        print(n, "không phải là số chính phương")
    break

star_no=int(input("Enter number:"))
for i in range(star_no):
    for j in range(star_no):
        if i>=j:
            print(end=' ')
        else:
            print("*", end='')

    print()

star=int(input("Enter number:"))
for i in range(star):
    for j in range(star):
        if i>=j:
            print("*", end='')
    print()            

# stars pattern
stars=int(input("Enter number:"))
for i in range(stars):
    for j in range(stars):
        if i<=j:
            print("*", end='')
    print()

# star patter
star_no=int(input("Enter number:"))
for i in range(star_no):
    for j in range(star_no):
        if i>=j:
            print("*", end='')
    print()

for i in range(star_no):
    for j in range(star_no):
        if i<=j:
            print("*", end='')
    print()
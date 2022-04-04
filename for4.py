num1=0
for i in range(1,6):
    ask=str(input("Are you tired? "))
    if ask=='yes':
        print("You didn't finish the race")
        break
    else:
        num1+=1
        continue
if num1==5:
    print("Congratulation! you have finished the race") 


result=["heads", "tails", "tails", "heads","tails","heads","heads","tails","tails","tails"]
key='heads'
count=0
print(result)
for i in range(len(result)):
    if key==result[i]:
        count=count+1
        
print("heads:",count)    

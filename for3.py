expense_list=[2340, 2500, 2100, 3100, 2980]
count=0
exp=int(input("Enter your monthly expense:"))
for i in range(len(expense_list)):
    if exp==expense_list[i]:
        print("Month:",(i+1), "Expense:", expense_list[i])
        break
    count+=1
if count==len(expense_list):
    print(exp)
  


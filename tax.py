empo=input()
empname=input()
empdesign=input()
basicsalary=int(input())
da=int(input())
ta=int(input())
hra=int(input())

netsalary=basicsalary+da+ta+hra
if netsalary==basicsalary>100000:
   tax=netsalary*10/100
if netsalary>50000:
    tax=netsalary*7/100
if netsalary>40000:
   tax=netsalary*4/100
if netsalary<20000:
   tax=0
   print(empo)
   print(empname)
   print(empdesign)
   print(basicsalary)
print("the total tax:",tax)



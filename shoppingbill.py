salt=100
maggie=500
bread=300
jam=50
flour=150
cphno=int(input())
cname=input()
address=input()
sq=int(input('no of salt packets:'))#2
mq=int(input('no of maggie packets:'))#1
bq=int(input('no of bread packets:'))#2
jq=int(input('no of jam bottles:'))#4
fq=int(input('no of flour packs:'))
bill=(sq*salt)+(mq*maggie)+(bq*bread)+(jq*jam)+(fq*flour)
print(bill)
if bill>3000:
 tax=bill*5/100
elif bill>2000:
 tax=bill*7/100
elif bill>500:
 tax=bill*15/100
else:
 tax=100
bill=tax+bill
print(cphno)
print(cname)
print(address)
print(bill)

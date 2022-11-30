salt=100
maggie=500
bread=300
jam=50
flour=150
cphno=int(input())
cname=input()
address=input()
coupon=input()
sq=int(input('no of salt packets:'))
mq=int(input('no of maggie packets:'))
bq=int(input('no of bread packets:'))
jq=int(input('no of jam bottles:'))
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
if coupon=='DIWALI' and bill>=5000:
      dis=bill*10/100
if coupon=='DIWALI' and bill>=3000:
     dis=bill*6/100
if coupon=='DIWALI' and bill>=1000:
     dis=bill*4/100
           
bill=tax+bill
print('tax',tax)
print(cphno)
print(cname)
print(address)
print(bill)
print(dis)

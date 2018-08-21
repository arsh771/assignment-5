
#Q1
yr=int(input('Enter Year:'))
if yr%4==0:
    if yr%100==0:
         if yr%400==0:
             print(yr,'is a leap year ')
         else:
             print(yr,'is not a leap year ')
    else:
         print(yr,'is a leap year ')
else:
     print(yr,'is not a leap year ')

#Q2
l=int(input('Enter Length:'))
b=int(input('Enter Breadth:'))
if(l>0 and b>0):
    if(l==b):
         print("It is a square")
    else:
        print("It is a rectangle")
else:
   print("Input given is incorrect")

#Q3
a1=int(input("Enter age 1:"))
a2=int(input("Enter age 2:"))
a3=int(input("Enter age 3:"))
if(a1>=a2 and a1>=a3):
    print("Age of the eldest is:",a1)
    if(a2>=a3):
      print("Age of the youngest is:",a3)
    else:
      print("age of the youngest is:",a2)
      
elif(a2>=a1 and a2>=a3):
    print("Age of the eldest is:",a2)
    if(a1>=a3):
      print("Age of the youngest is:",a3)
    else:
      print("Age of the youngest is:",a1)
      
else:
    print("Age of the eldest is:",a3)
    if(a1>=a2):
      print("Age of the youngest is:",a2)
    else:
      print("Age of the youngest is:",a1)
    
#Q4
age=int(input("Enter age:"))
sex=input("Enter Sex( M or F):")
status=input("Enter Marital Status (Y or N):")
if(sex=='F' or sex=='f'):
    print("Place of Service: URBAN AREA ONLY ")
elif(sex=='M' or sex=='m'):
    if(age>=20 and age<=40):
        print("Place of Service: ANYWHERE ")
    elif(age>40 and age<=60):
        print("Place of Service: URBAN AREA ONLY")
    else:
        print("ERROR")
else:
   print("ERROR")
   


#Q5
u=int(input("Enter units:"))
# u stands for units
c=int(input("Enter cost:"))
#c stands for cost
amount=u*c
print('Amount:',amount)
if(amount>=1000):
    print('Amount after discount:',amount-(amount*(1/10)))
else:
    print("NO DISCOUNT")

#Q6
integers=[]
for i in range(10):
    value=int(input('Enter value:'))
    integers.append(value)
print('List:',integers)


#Q7
a=1
while a>0:
    print(a)
    a=a+1


#Q8

list1=[]
list2=[]
a=int(input("Enter No of Values:"))
for i in range(a):
    b=int(input('Enter digits:'))
    list1.append(b)
print('List:',list1)
for i in range(a):
    sq=list1[i]*list1[i]
    list2.append(sq)
print('List of Squared element:',list2)

#Q9

list1=[]
list2=[]
list3=[]
list4=[]
a=int(input("Enter No of Values:"))
for i in range(a):
    d=input('Enter values:')
    list1.append(d)
print('List:',list1)
for i in range(a):
    if str(list1[i]).isdigit():
        list2.append(list1[i])
    elif str(list1[i]).isalpha():
        list3.append(list1[i])
    else:
        list4.append(list1[i])
print('Int List:',list2)
print('String List:',list3)
print('Float List:',list4)


#Q10

print("Prime numbers are:")

for i in range(1,101):
   if i > 1:
       for x in range(2,i):
           if (i % x) == 0:
               break
       else:
           print(i)



#Q11
print('Pattern')
for i in range(0, 5,1):
    print("* "*i)

    
#Q12
print()
list1=[]
list2=[]
a=int(input("Enter No of Values:"))
for i in range(a):
    b=int(input('Enter digit:'))
    list1.append(b)
print(list1)
search=int(input("Enter value to search:"))
list1.remove(search)
print(list1)      
         
         
             
         

#Dictionary


student={
    'NAME':'ACE',
    'BRANCH':'CSE'
    }
student['NAME']
student['BRANCH']
student.items
student.keys()

#type func
a = 1,2,3,4,5
print(type(a)) 


#arithmatic operator
#ADDITION
a=2
b=3
print(a+b)

#subtraction
print(a-b)

#multiplication
print(a*b)

#greater
print(a<b)

#less then
print(a>b)

#bitwise operator
#and
print(a&b)

#or
print(a|b)

#xor
print(a^b)

#identity operator
#is
print(a is b)

#is not
print(a is not b)

#condition operator
#if-else

age=14
if(age>18):
    print("eligibe tro vote")
else:
    print("Not eligible to vote")


 #even or odd
a=5
b=6
if(a%2==0):
    print("even")
else:
    print("odd")    
    

#guess the no    
marks= 99
if(marks>=60):
    print('first devision')
elif(marks<60 & marks>35):
 print('second devision')
else:
 print('fail')



#for loop
for i in range(10):
    print(i)

#dictionary range func
a=[1,2,3,4,5,6]
for n in a:
    print(a)

#dict in func range

student={'name':'ace','branch':'cse'}
for x in student.items():
    print(x)  

 #condition or loop     
lst=[1,2,3,4,5,6]
for i in lst:
    print(lst[i])
    if(lst[i]==6):
        break
    else:
     continue   


 #while loop
count=1
while (count<=6):
    print(count)
    count+=1
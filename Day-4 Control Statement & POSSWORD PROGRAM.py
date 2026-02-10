# 1.Conditional Statement (or) Decison making Statement.....

#  if statement 
a=10
b=20
if a==b:
    print("a==b False")
else:
    print("a==b true")
    
    
    # logical operators
    ''' logical operators are AND,OR, NOT
    --AND operator returns true if both the operands are true
    --OR operator returns true if either of the operands is true
    --NOT operator returns true if the operand is false
    '''
    x=10
    y=20
    if x<y and x<y:      #x<y or x>y:
        
        print("this is if")
    else: 
        print("this is elif") 
        
# elif statement
a=20
b=30 
if a>b:                    
    print("True")
elif a<b:
    print("False")
else:
    print("else")
    
    
# 2. Looping Statement (or) Iterative Statement...
#  for loop :
''' range function (start,satp,skip)'''
for i in range(1,10):    
    print(i)
    
    
    
a="vijay"
for i in a:
    print(i)  
    
L=["a","b","c"]  
for i in L:
    print(i)  


# while loop :
''' this is inifinet looping statement '''
# while True:
#     print("thie is while")  

c=0
while c<3:
    c=c+1
    print("while True")
else:
    print ("False")
    
    
    
#3 Jumping Statement :

'''
pass
break
continue
'''

if True:            # pass- ignore
        pass


for i in "pythonlife":       #break--terminate
    if i=='l':
        break
    print(i)
    
for i in "pythonlife":         #continue--skipn(current iteration)
    if i=="y":
        continue
    print(i)    
    
    
# POSSWORD PROGRAM.......

User="vijay"
PossWord="vijay1432"
User_name=input("Enter the User Name:")
Poss_word=input("Enter the PossWord:")
if User==User_name and PossWord==Poss_word:
    print("Succues")
else:
    print ("try again")
    
    
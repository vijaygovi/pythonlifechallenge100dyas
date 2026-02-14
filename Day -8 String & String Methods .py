# String in python
''' 
Colection of characters
type of declaration 3 types 

1.Single quote ' '
2.Double qoute " "
3.Triple quote '''  '''  

''' 
Suresh='python'
Madhu= "pythonlife"
vijay='''python programming'''
print(type(Suresh),type(Madhu),type(vijay))


# String Methods
'''
1. Count ()
2. Endswith ()
3. Find ()
4. Format()
5.Index found ()
6. Isalnum ()
7. Isalpha ()
8. Join ()
9. lower ()
10.Upper ()
11.Replace ()
12.Split ()
13.Title ()
14.Strip ()
15.IStrip ()
16.RStrip ()
17.Startswith ()
'''

# 1 Count () 
Suresh='python'
print(Suresh.count('3'))

#2.Endswith 
vijay ='pyhtonlife'
print(vijay.endswith('life'))   

#3. Find()
vijay='python programming'
print(vijay.find('kiran')) #if word is not return -1

#4.Format ()
vijay ='hii {} thinna ra ? {} '.format ("vijay","EM chesthunna vu ")
print(vijay)

#5.Index found()
vijay ="my fav hero is vijay"
print(vijay.index("fav"))

#6.Isalnum()
vijay="Srikrishna"
print(vijay.isalnum())

#7.Isalpha()
vijay="12345"
print(vijay.isalpha())

#8.Join()
vijay="this is string"
c=vijay.split()
s=" ".join(c)
print(s)
#9.Strip()
d="this is vijay"
print(len(d))
s=d. strip()

#10.upper()
vijay="this is vijay "
print(vijay.upper())

#11.lower()
vijay="THIS IS VIJAY"
print(vijay.lower())
 
#12.replace()
vijay="this is my book"
a=vijay.replace("book","open")
print(a)

#13.split()
vijay="this is string class"
a=vijay.split()
n=[]
for i in a:
    if i=="is":
        n.append(i)
    else:
        n.append(i)
        print(a)
        
#14.title()
d="this is abhi"
print(d.title())

#15.lstrip()
d="hey abhi em chesthunnv"
print(d.lstrip("hey "))

#16.rstrip()
d="hey abhi em chesthunnv"
print(d.rstrip("unnv"))

#17.startswith()
d="this is vijay"
print(d.startswith("this"))
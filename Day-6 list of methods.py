#list of methods in python
'''
1.append() -add element at the end of the list 
2.insert() - add element at the specific index
3.copy() - copy th list 
4.count() - count the number of times an element appears in the list
5.extend() - add elaments of a list to thr end of the list
6.index () - return the index of the frist element with the specified valu 
7.pop () - remove the elememnt at the specified position
8.remove () - remove the frist item with the specified value
9.reverse () - reverse the order of the list 
10.sort () - sort the list in ascending order
11.clear () - remove all the elements from the list 

'''

#1.append
append =[1,2,3,4,5,6,7,8,9]
append.append(10)
print(append)

#2.insert
insert=[1,2,3,4,5,6,7,8,9,"vijay "]
insert.insert(114,'python')
print(insert)

#3.copy
copy=[1,2,3,4,5,6,7,8,9,"abhishek"]
a=copy.copy()
print(a)

#4.count
aparna=[1,2,3,4,5,6,7,8,9]
print(aparna.count(3))

#5.extend
vijay=[1,2,3,4,5]
vijay.extend([5,6,7,8,9,10])
print(vijay)

#6.index
vijay=[1,2,5,3,8,9]
print(vijay.index(9)) 

#7.pop 
navi=[1,12,45,17,23,1,2]
navi.pop(2)
print(navi)

#8.remove
navii=[12,52,887,758,96,8756]
navii.remove(887)
print(navii)

#9.reverse
abhi=[1,4,33,5,97,567,76,87654,457,788,45]
abhi.reverse()
abhi.append("vijay")
print(abhi)

#10.sort
abhi=[12,124,65,3456,75,56]
abhi.sort()
print(abhi)

#11.clear
vijay=[1,2,3,4,6,7,'python',45,34,762]
vijay.clear()
print(vijay)

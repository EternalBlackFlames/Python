#Creating an empty List
my_list =[]
print(my_list)
#adding Elements into the list
my_list =[1,5,'examle',7]
print(my_list)
my_list.append([6,'one'])
print(my_list)
my_list.extend([10,'why'])
print(my_list)
my_list.insert(0,345)
print(my_list)
#deleting elements into the list
del my_list[1]
print(my_list)
my_list.remove(5)
print(my_list)
a = my_list.pop(3)
print('popped element:', a,'\nremaining list is:',my_list)
#Accessing elements in the List
for i in my_list:
    print(i)
print(my_list)
print(my_list[2])
print(my_list[0:2])
print(my_list[0:])
print(my_list[::-1])
#other functions
mlist2 = [2,5,2,7,5,3,4,9,1,0]
print(mlist2)
print(len(mlist2))
print(mlist2.count(2))
print(mlist2.index(7))
print(sorted(mlist2))
print(mlist2)
mlist2.sort(reverse=False)
print(mlist2)
#Operations on list Completed date:16-0ct

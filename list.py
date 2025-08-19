list=["Rahul","Thej", "Roshani","Yellpaur",12,18,12]
print(type(list))

print(list)

print(list[3])  ##get item by index

print(list[1:4]) ## get by range
print(list[3:])
print(list[:4])  
print("double collon -> jump{list} and",list[::2])

list[4]="Mysuru"
print(list)

list.append("Orange")  #it will item to the end
list.insert(0,"Python") #insert wrt index
print(list)
list.__add__(["Benagaluru"]) #it will append another list


list.remove(12) ##will remove duplicate 

list_second_1 = list.pop() ##delete last object
print(list_second_1)
print(list)

print("index of Rahul ",list.index("Rahul"))  ##print index of the object


list.insert(2,"Rahul")
list.insert(5,"Rahul")

print("count",list.count("Rahul"))  ##count the element

list.remove(18)

list.sort()  ##sort the list
print("sorted list",list)


list.reverse()  ##reverse the list
print("reverse",list)

print("Iterate")
for element in list:
    print(element)


for position,element in enumerate(list):  ##iterate with index
    print(position,element) 


print([x**2 for x in range(5)])  # {experssion , range}
print([num for num in range(10) if num%2==0 ]) ##{expression, range, condidtion}


list1=[1,2,3,4,5]
list2=['a','b','c','d']

pair=[[i,j] for i in list1 for j in list2 ]
print(pair)

words =["rahul","mohan","naik"]
lengths=[len(word) for word in words]
print(lengths)

list.clear()
print("the emphty lis",list)
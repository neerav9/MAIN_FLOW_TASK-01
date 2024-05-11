#creating a list 
list1=[]
print("This list1 contains no elements.")
#creating a list with elements inside it 
list2 = [1,2,3,4,5]
print(list2)

#adding elements to the list 
list1.append(6)
list1.append(7)
list1.append(8)
list1.append(9)
list1.append(10)
print(list1)

#adding elements in the list by taking user inputs
list_new=[]
print("Enter the number of elements you need in the list:")
n=int(input())
for i in range(n):
    list_new.append(int(input()))
print(list_new)

#removing of an element from the list
list_new.remove(2)
print(list_new)

#updating an element from the list
list_new[2]=14
print(list_new)
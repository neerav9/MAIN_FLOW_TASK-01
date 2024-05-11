#creating a set 
set1={1,2,3,4,5}
print(set1)

#adding elements into a set
set1.add(6)
print(set1)

#removing element from the set
set1.remove(5)
print(set1)

#updating the elements in a set
set1.discard(1)
print(set1)

#remove () will raise an error if the element is not present in the set, while discard () will not.
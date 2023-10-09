'''1. Print out “Python Assignment 3”
2. Create a string variable storing any name
3. Type cast the variable in no2 to a set to create a set of characters
4. Create a set of alphabets from a-k
5. Join the two sets in no3 and no4 together
6. Create a set storing 5 states in Nigeria
7. Add two more states to the set in no5 using the correct function
8. Create a list of 5 fruits and add the list to the set in no 6
9. Print the whole elements inside the set in no6'''

#SOLUTIONS
print('Python Assignment 3')
#storing a name
name = 'Helen'
#type casting name to a set datatypes
name_set = set(name)
#creating a set of alphabets a-k
characters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k'}
#joining two preceding sets 
name_set.update(characters)
#creating a set of states
states = {'abia', 'imo', 'enugu', 'ebonyi', 'anambra'}
#updating elements in the set
states2 = {'edo', 'delta'}
states_new = states.union(states2)
#set of 5 fruits
fruits = {'orange', 'mango', 'pear', 'apple', 'banana'}
#combining sets of states and fruits
states_n_fruits = states.union(fruits)
print(states_n_fruits) 
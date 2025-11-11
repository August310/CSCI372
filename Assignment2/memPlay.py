#part a) where we check if two Strings share id if they're the same value
#made a small function to determine if two Strings are equal and have identical ids
def check_id(s1, s2):
    if(s1 == s2):
        if(id(s1) == id(s2)):
            return True
        else:
            return False
    else:
        return False

#used to test if the function above works
print(check_id("Hello", "Hello"))

#part b) where we test out if a list changes id when we change the list's values
l1 = [1, 2, 3]

#we print the list and its id
print("part b) list", l1 , "id:",  id(l1))

#add 5 to the end of the list, then see if the list has a different id
l1.append(5)
print("After the change to list", l1 , "id:", id(l1))


#part c) I made a couple discoveries of my own
#id of integers stays the same if they're the same values
x = 10
y = 10
print(id(x) == id(y))

#even making a number negative completely changes the id values
x = -10000
y = 10000
print(id(x) == id(y))

#two different lists with the same values inside still have different id values
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(id(list1) == id(list2))

#with this tuple I inserted a list in it since tuples themselves aren't able to be changed
tuple1 = (1, [2, 3])

#the id of the tuple before any changes
print("id of the tuple", id(tuple1))

#the id of the inner list which shows the inner list has a different id
print("id of the inner list", id(tuple1[1]))

#add a value to the list inside the tuple
tuple1[1].append(4)

#we find that the tuple is changed but the id stays the same
print(tuple1)
print("id of tuple after changing inner list", id(tuple1))


    


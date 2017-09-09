# Lists and Loops [demonstration]
my_list = [1, 2, 3, "a", "b", "c"]
print("my_list is:", my_list)

print("Looping through a list...")
for item in my_list:
    print("item is", item)

print("The len function is important!")
num_elements = len(my_list)
print("my_list has", num_elements, "elements")

print("A less great way to loop through a list...")
for index in range(len(my_list)):
    item = my_list[index] # accessing an element in a list!
    print("item is", item)

print("Slicing a list from beginning...")
for item in my_list[:3]:
    print("item is", item)

print("Slicing a list to the end...")
for item in my_list[3:]:
    print("item is", item)

print("Slicing a list in the middle...")
for item in my_list[2:4]:
    print("item is", item)

print("Enumerating a list...")
for i, item in enumerate(my_list):
    print("item number", i, "is", item)

print("Another way to enumerate using a list 'method'...")
for item in my_list:
    index = my_list.index(item)
    print("item", item, "has index", index)


user_list = []
new_list = []
print("Enter the number of rotations to do: ")
rotation = int(input())
print("Enter the number of items in the list: ")
no_of_items = int(input())
for i in range(no_of_items):
    print("Enter the {}th item/s: ".format(i+1))
    user_list.append(input())
print("User list is: {} and requires rotation from left for \"{}\" places".format(user_list, rotation))

len_list = len(user_list)
mid_of_list = rotation % len_list

for i in range(len_list):
    index = (mid_of_list + i) % len_list
    element = user_list[index]
    new_list.append(element)
print("New list is: {}".format(new_list))




user_list = []
print("Enter the number of rotations to do: ")
rotation = int(input())
print("Enter the number of items in the list: ")
no_of_items = int(input())
for i in range(no_of_items):
    print("Enter the {}th item/s: ".format(i+1))
    user_list.append(input())
print("User list is: {} and requires rotation from left for \"{}\" places".format(user_list, rotation))

for i in range(rotation):
    item = user_list.pop(0)  # 1 = item
    print(item)
    user_list.append(item)
print("New list is: {}".format(user_list))

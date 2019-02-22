user_list = []
print("Enter the number of rotations to do: ")
rotation = int(input())
print("Enter the number of items in the list: ")
no_of_items = int(input())
for i in range(no_of_items):
    print("Enter the {}th item/s: ".format(i+1))
    user_list.append(input())
print("User list is: {} and requires rotation from left for \"{}\" places".format(user_list, rotation))

chunk_1 = user_list[rotation:]
print(chunk_1)
chunk_2 = user_list[:rotation]
print(chunk_2)
result_list = chunk_1 + chunk_2
print("New list is: {}".format(result_list))

todo_list = ['sacar la basura','barrer la entrada','pasear al toby','regar las plantas']

for todo in todo_list:
    print(todo)

print('---------------------------------------------')

index=0
while index <len(todo_list):
    print(todo_list[index])
    index += 1

print('---------------------------------------------')

[print(todo) for todo in todo_list]
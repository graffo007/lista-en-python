todo_list = ['scar la basura','barrer la entrada','pasear al toby','regar las plantas']

todo_list[0] = "dormir siesta"
todo_list[1:3] = ["comer verduras"," ayudar a cruzar la calle a la abuelita"]
todo_list[1:3] = ['dejar la coca-cola']


print(todo_list)

movies = ['matris','wars star','el viejo de las argollas']
books = ['poemas de baldor','chistes de proschle','horoscopo xino']

movies.extend(books)

print(movies)
print(books)
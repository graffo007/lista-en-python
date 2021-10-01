fruits = ['mango','piña','guinda','guayaba','maracuya']

#fruits.sort()
#print(fruits)
fruits.sort(reverse=True)
print(fruits)

grades = [10,9,8,10,8,8]
grades.sort(reverse=True)
print(grades)


# no elementos diferente
cat_bag = [12,"hola",True]
#cat_bag.sort()
#print(cat_bag)

# cuidado con las mayusculas
veggie_list =  ["Papas","Quinoa","Maiz","choclito","papitas" ]
veggie_list.sort(key = str.lower)
print(veggie_list)



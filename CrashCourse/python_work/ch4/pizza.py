pizzas = ['hawaian', 'meat-lovers', 'cheese']
friend_pizzas = pizzas[:]

pizzas.append('bbq chicken')
friend_pizzas.append('thai one on')

print("My favorite pizzas are:")
for pizza in pizzas:
	print(f"{pizza} pizza")
print("\nMy friends favorite pizzas are:")
for fpizza in friend_pizzas:
	print(f"{fpizza} pizza")

# pets = ['dog', 'cat', 'kowala']
# for pet in pets:
# 	print(f" A {pet} would make a great pet! they are cuddly")
# print("All of these pets are adorable, and would make a great pet!")
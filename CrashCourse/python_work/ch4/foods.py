my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
	print(f"{food}")
# print(my_foods)

print("\nMy friend's favorite foods are:")
for ffood in friend_foods:
	print(f"{ffood}")
# print(friend_foods)
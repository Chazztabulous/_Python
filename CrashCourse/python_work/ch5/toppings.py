available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
# if 'mushrooms' in requested_topping:
# 	print("Adding mushrooms.")
# if 'pepperoni' in requested_topping:
# 	print("Adding pepperoni.")
# if 'extra cheese' in requested_topping:
# 	print("Adding extra cheese.")

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}")
	else:
		print(f"Sorry, we dont have {requested_topping}")

print("\nFinished making your pizza!")
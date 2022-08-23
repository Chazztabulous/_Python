names = ['Hirohiko Araki', 'Oda Nobunaga', 'David Drake', 'Brandon Sanderson', 'Geoff Johns']
print(f"Hello {names[0]}, you've been invited to dinner this evening at 21:00")
print(f"Hello {names[1]}, you've been invited to dinner this evening at 21:00")
print(f"Hello {names[2]}, you've been invited to dinner this evening at 21:00")
print(f"Hello {names[3]}, you've been invited to dinner this evening at 21:00")
print(f"Hello {names[-1]}, you've been invited to dinner this evening at 21:00")

print(f"\nUnfortunately, {names[1]} is unable to attend")

names.remove('Oda Nobunaga')
names.insert(1, 'Chris Hemsworth')
print('\n')
print(f"Hello {names[0]}, you've been invited to dinner this evening at 21:00")
print(f"Hello {names[1]}, you've been invited to dinner this evening at 21:00")
print(f"Hello {names[2]}, you've been invited to dinner this evening at 21:00")
print(f"Hello {names[3]}, you've been invited to dinner this evening at 21:00")
print(f"Hello {names[-1]}, you've been invited to dinner this evening at 21:00")

print("\nIt looks like we found a bigger table; we need to invite 3 more guests")

names.insert(0, 'Rhys Darby')
names.insert(2, 'Fernando Alonso')
names.append('Taika Waitit')
print('\n')
print(f"Hello {names[0]}, you've been invited to dinner this evening at 21:00")
print(f"Hello {names[1]}, you've been invited to dinner this evening at 21:00")
print(f"Hello {names[2]}, you've been invited to dinner this evening at 21:00")
print(f"Hello {names[3]}, you've been invited to dinner this evening at 21:00")
print(f"Hello {names[4]}, you've been invited to dinner this evening at 21:00")
print(f"Hello {names[5]}, you've been invited to dinner this evening at 21:00")
print(f"Hello {names[6]}, you've been invited to dinner this evening at 21:00")
print(f"Hello {names[7]}, you've been invited to dinner this evening at 21:00")

print(f"{len(names)}")

print("\nOur table wont be ready, we only have space for 2 people")

reject_guests = names.pop(1)
print(f"\nI'm sorry {reject_guests}, we dont have room at our table anymore")

reject_guests = names.pop(1)
print(f"\nI'm sorry {reject_guests}, we dont have room at our table anymore")

reject_guests = names.pop(1)
print(f"\nI'm sorry {reject_guests}, we dont have room at our table anymore")

reject_guests = names.pop(-2)
print(f"\nI'm sorry {reject_guests}, we dont have room at our table anymore")

reject_guests = names.pop(-2)
print(f"\nI'm sorry {reject_guests}, we dont have room at our table anymore")

reject_guests = names.pop(1)
print(f"\nI'm sorry {reject_guests}, we dont have room at our table anymore")

print(f"{names[0]} our table is ready! right this way")
print(f"{names[1]} our table is ready! right this way")

del names[0]
del names[0]

print(names)
motocycles = ['honda', 'suzuki', 'triumph']
print(f"Id love to own a {motocycles[2]} motorcycle, but I cant afford it")
print(f"A {motocycles[0]} or a {motocycles[1]} would be more practical")

print(motocycles)

motocycles.append('ducatti')
print(motocycles)

motocycles = ['honda', 'suzuki', 'triumph']
motocycles.insert(0, 'ducatti')
print(motocycles)

del motocycles[0]
print(motocycles)

last_owned = motocycles.pop()
first_owned = motocycles.pop(0)
print(motocycles)
print(f"The last motorcycle I owned was a {last_owned.title()}")
print(f"The first motorcycle I bought was a {first_owned.title()}")

too_expensive = 'ducatti'
motorcycles = ['honda', 'suzuki', 'triumph', 'ducatti']
print(motorcycles)

motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me")
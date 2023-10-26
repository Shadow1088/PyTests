class MyClass:
    pass

x = MyClass()

# Create a dictionary to map objects to their names
objects = globals().copy()
objects.update(locals())
name = [name for name in objects if objects[name] is x][0]

print("Name of variable x:", name)

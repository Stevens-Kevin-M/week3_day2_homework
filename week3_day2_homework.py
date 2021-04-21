# Exercise 1 - Filter out all of the empty strings from the list below

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

new_places_lamb = list(filter(lambda place: True if place.strip() !="" else False, places))
print(new_places_lamb)

# Exercise 2 - Write an anonymous function that sorts this list by the last name...

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]
author.sort(key=lambda x:x.split(" ")[-1].lower())
print(author)

# Exercise 3 - Convert the list below from Celsius to Farhenheit, using the map function with a lambda...

# F = (9/5)*C + 32
# Just for fun!
#places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]
#d = dict(places)
#for key, value in d.items():
#    print(key + " - " + str((9/5)*value + 32))
# Working Lambda Example Below

places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]    
final_places=list(map(lambda x: (x[0], (9/5)*x[1] + 32), places))
 
print(final_places)

# Exercise 4 - Write a recursion function to perform the fibonacci sequence up to the number passed in.

def fibonacci(x):
    if x <= 1:
        return x
    else:
        return(fibonacci(x-1) + fibonacci(x-2))

if i <= 0:
    None
else:
    for i in range(1,7):
        print((f"Iteration {i-1}:") + " " + str(fibonacci(i)))
import random
#choice(seq)
#A random item from a list, tuple, or string.

print(random.choice(range(100)))
print(random.choice([10,25,45,78,45,15,455,454,548,54,54,8,4]))
print(random.choice("hello python"))

#randrange()
# randrang(start, end, step)
#The randrange() method returns a randomly selected
# element from range(start, stop, step).

print("randrange",random.randrange(100))
print("randrange",random.randrange(1, 10,2))

# First random number
print ("random() : ", random.random())
#it always gives 0-1
# Second random number
print ("random() : ", random.random())

#The shuffle() method randomizes the items of a list in place.

list=[10,45,78,95,87,54,1,4,15,5]
random.shuffle(list)
print(random.shuffle(list),"\r",list)

#uniform(x, y)
#The uniform() method returns a random float r,
# such that x is less than or equal to r and r is less than y.
print ("Random Float uniform(5, 10) : ",  random.uniform(5, 10))
print ("Random Float uniform(7, 14) : ",  random.uniform(7, 14))

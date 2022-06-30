sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above

list = []
list = sentence.split(" ")
print(list)
result = {word:len(word) for word in list}

print(result)

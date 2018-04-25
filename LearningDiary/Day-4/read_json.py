import json

green_file = open("green.car")
yellow_file = open("yellow.car")

green = json.load(green_file)
yellow = json.load(yellow_file)

print(green)
print(yellow)
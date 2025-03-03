print("We are learning advanced Git and GitHub")
#data types
#integers
age = 25
#float
height = 5.75
#string
name = "John"
#boolean
is_student = True
#list they are mutable
fruits = ["apple", "banana", "cherry"]
fruits.append("grape")
#tuple they are immutable
coordinates = (25, 75)
#dictionary they store key-value pairs
person = {"name": "John", "age": 25}
#set they are unordered and unindexed and do not allow duplicates
colors = {"red", "green", "blue"}

print("colors are of type",  type(colors))


studentScores = {
    "Denis Ndiritu": 90,
    "John Knox": 80,
    "Kennedy Muriuki": 73,
    "Eric Mwangi": 66
}

for i in fruits:
    print(i)

countdown = 10
while countdown > 0:
    print(countdown)
    countdown -=1
print("Blast off!")
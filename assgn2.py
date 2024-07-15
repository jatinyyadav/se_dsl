n = int(input("enter the total number of students: "))
a = int(input("number of students who play criket: "))
b = int(input("number of students who play badminton: "))
c = int(input("number of students who play football: "))

cricket=[]
badminton=[]
football=[]

for i in range(a):
    cricket.append(int(input("enter cricket student: ")))
for i in range(b):
    badminton.append(int(input("enter badminton student: ")))
for i in range(c):
    football.append(int(input("enter football student: ")))

#list of student who play cricket and badminton both
cricBad=cricket.copy()
for i in badminton:
    if i not in cricBad:
        cricBad.append(i)

#who play  either cricket or badminton but not both
cricBadNot=cricket.copy()
for i in badminton:
    if i in cricBadNot:
        cricBadNot.remove(i)
    if i not in cricBadNot:
        cricBadNot.append(i)

#number of student who play neither cricket not badminton
otherCricBad=n-a-b

#cricket and football not badminton
cricFootNotBad=cricket.copy()
for i in football:
    if i not in cricFootNotBad:
        cricFootNotBad.append(i)
for i in badminton:
    if i in cricFootNotBad:
        cricFootNotBad.remove(i)
cricFootNotBad=len(cricFootNotBad)

#student who not play any game
noGame=n-a-b-c

#atleast one game
atleast=cricket.copy()
for i in badminton:
    if i not in atleast:
        atleast.append(i)
for i in football:
    if i not in atleast:
        atleast.append(i)

#all game
allGame=atleast.copy()
for i in atleast:
    if i not in cricket:
        if i in allGame:
            allGame.remove(i)
    if i not in badminton:
        if i in allGame:
            allGame.remove(i)
    if i not in football:
        if i in allGame:
            allGame.remove(i)

print(f"list of student who play both cricket and badminton: {cricBad}")
print(f"list of student who play either cricket or badminton but not both: {cricBadNot}")
print(f"number of students who play neither cricket nor badminton: {otherCricBad}")
print(f"number of students who play cricket and football but not badminton: {cricFootNotBad}")
print(f"number of students who do not play any game: {noGame}")
print(f"list of student who play atleat one game: {atleast}")
print(f"list of student who play all games: {allGame}")
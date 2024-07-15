marks=[]

while True:
    mark = input("enter the marks of student, if absent type 'ab', if done type 'done': " )
    if mark.lower()=='done':
        break
    elif mark.lower()=='ab':
        marks.append(None)
    else:
        mark=int(mark)
        marks.append(mark)
total= len(marks)
absent = 0
s=0
for mark in marks:
    if mark==None:
        absent+=1
        marks.remove(mark)
    else: s+=mark
present = total-absent
average=s/present

maxi=0
mini=0
fail=0
for mark in marks:
    if mark<12: fail+=1
    if mark>maxi: maxi=mark
    if mark<mini: mini=mark

passed = present-fail
percent_pass=(passed/total)*100
percent_fail = (fail/total)*100

freq={}
for mark in marks:
    if mark is not None:
        if mark not in freq:
            freq[mark]=0
        freq[mark]+=1

if freq:
    max_occ=max(freq.values())
    most_common_elements=[key for key, value in freq.items() if value == max_occ]
else:
    most_common_elements=[]

print(f"total students: {total}")
print(f"number of absentees: {absent}")
print(f"number of student present: {present}")
print(f"average marks: {average}")
print(f"highest marks: {maxi}")
print(f"lowest marks: {mini}")
print(f"number of students failed: {fail}")
print(f"percent of student passed: {percent_pass}%")
print(f"percent of student failed: {percent_fail}%")
print(f"most common marks: {most_common_elements}")
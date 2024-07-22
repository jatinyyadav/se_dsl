def inputt():
    ls = []
    n = int(input("Enter the number of students: "))  
    print("Enter the list elements separated by spaces:")
    elements = input().split() 
    ls = [int(elem) for elem in elements]  
    return ls

def linear_search(ls,index):
    com=0
    for i in range(len(ls)):
        if ls[i]==index:
            return f"element found at {i} through linear seach, and comparisons done are {com}"
        com+=1
    return f"element not found ,comparisons done are {com}"

def binary_search(key,ls):
    ls.sort()
    low=0
    hi=len(ls)-1
    com=0
    while low<=hi:
        mid=(low+hi)//2
        if key==ls[mid]:
            return f"found at index {mid} through binary search and number of comparisons done are {com}"
        elif key<ls[mid]:
            hi=mid-1
            com+=1
        elif key>ls[mid]:
            low=mid+1
            com+=1
    return f"element not found ,comparisons done are {com}"

ls=inputt()
index = int(input("enter the element to found: "))
print(f"found at index {linear_search(ls,index)} through linear search")
print(binary_search(index,ls))
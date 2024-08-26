def insertion_sort(marks):
    print("Performing Insertion Sort...")
    n = len(marks)
    for i in range(1, n):
        key = marks[i]
        j = i - 1
        while j >= 0 and marks[j] > key:
            marks[j + 1] = marks[j]
            j -= 1
        marks[j + 1] = key
        print(f"Step {i}: {marks}")
    print("Marks after Insertion Sort:", marks)
                                                                  
def shell_sort(marks):
    print("Performing Shell Sort...")
    n = len(marks)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = marks[i]
            j = i
            while j >= gap and marks[j - gap] > temp:
                marks[j] = marks[j - gap]
                j -= gap
            marks[j] = temp
        print(f"After gap size {gap}: {marks}")
        gap //= 2
    print("Marks after Shell Sort:", marks)

def selection_sort(marks):
    print("Performing Selection Sort...")
    n = len(marks)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if marks[min_idx] > marks[j]:
                min_idx = j
        marks[i], marks[min_idx] = marks[min_idx], marks[i]
        print(f"Step {i + 1}: {marks}")
    print("Marks after Selection Sort:", marks)

def bubble_sort(marks):
    print("Performing Bubble Sort...")
    n = len(marks)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if marks[j] > marks[j + 1]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]
                swapped = True
        if not swapped:
            break
        print(f"Step {i + 1}: {marks}")
    print("Marks after Bubble Sort:", marks)

def top_five_marks(marks):
    top_marks = sorted(marks, reverse=True)[:5]
    print("Top Five Marks are:")
    for mark in top_marks:
        print(mark)

def main():
    marks = []
    n = int(input("Enter number of students whose marks are to be displayed: "))
    print(f"Enter marks for {n} students (Press ENTER after each student's mark):")
    for i in range(n):
        ele = float(input())
        marks.append(ele)

    print("The marks of the students are:")
    print(marks)

    flag = 1
    while flag == 1:
        print("\n---------------MENU---------------")
        print("1. Selection Sort of the marks")
        print("2. Bubble Sort of the marks")
        print("3. Insertion Sort of the marks")
        print("4. Shell Sort of the marks")
        print("5. Exit")
        ch = int(input("\nEnter your choice (from 1 to 5): "))

        if ch == 1:
            selection_sort(marks)
        elif ch == 2:
            bubble_sort(marks)
        elif ch == 3:
            insertion_sort(marks)
        elif ch == 4:
            shell_sort(marks)
        elif ch == 5:
            print("\nThanks for using this program!!")
            flag = 0
            continue
        else:
            print("\nEnter a valid choice!!")
            continue

        a = input("\nDo you want to display top five marks from the list (yes/no): ").strip().lower()
        if a == 'yes':
            top_five_marks(marks)
        else:
            print("\nThanks for using this program!")

if __name__ == "__main__":
    main()

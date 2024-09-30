#include <iostream>
#include <string>

using namespace std;

struct Node {
    string name;
    long prn;
    Node* next;

    Node() : prn(0), next(nullptr) {}
};

class List {
private:
    Node* head;
    Node* tail;
    int count;

public:
    List() : head(nullptr), tail(nullptr), count(0) {}

    void addMember() {
        int n;
        cout << "How many members to add? ";
        cin >> n;

        for (int i = 0; i < n; i++) {
            Node* newNode = new Node;
            cout << "Enter Member name: ";
            cin >> newNode->name;
            cout << "Enter PRN of Member: ";
            cin >> newNode->prn;

            if (!head || newNode->prn < head->prn) {
                newNode->next = head;
                head = newNode;
                if (!tail) tail = newNode; // Update tail if list is empty
            } else if (!tail || newNode->prn > tail->prn) {
                tail->next = newNode;
                tail = newNode;
            } else {
                Node* current = head;
                while (current->next && current->next->prn < newNode->prn) {
                    current = current->next;
                }
                newNode->next = current->next;
                current->next = newNode;
                if (!newNode->next) tail = newNode; // Update tail if new node is last
            }
            count++;
        }
    }

    void remove() {
        if (!head) {
            cout << "Error, Underflow!" << endl;
            return;
        }

        long prn;
        cout << "Enter PRN of member to remove: ";
        cin >> prn;

        if (head->prn == prn) {
            Node* temp = head;
            head = head->next;
            if (!head) tail = nullptr; // Update tail if list becomes empty
            delete temp;
        } else {
            Node* current = head;
            while (current->next && current->next->prn != prn) {
                current = current->next;
            }
            if (current->next) {
                Node* temp = current->next;
                current->next = current->next->next;
                if (!current->next) tail = current; // Update tail if removed node was last
                delete temp;
            } else {
                cout << "Member not found!" << endl;
            }
        }
        count--;
    }

    void displayList() {
        Node* current = head;
        while (current) {
            cout << "Name: " << current->name << ", PRN: " << current->prn << endl;
            current = current->next;
        }
    }

    void displayReverse(Node* node) {
        if (!node) return;
        displayReverse(node->next);
        cout << "Name: " << node->name << ", PRN: " << node->prn << endl;
    }

    void displayReverse() {
        if (!head) {
            cout << "List is empty!" << endl;
            return;
        }
        displayReverse(head);
    }

    void concatenate(List& other) {
        if (!other.head) return; // If the other list is empty, do nothing

        if (!head) { // If the current list is empty
            head = other.head;
            tail = other.tail;
        } else {
            tail->next = other.head; // Link the end of current list to the start of the other
            tail = other.tail; // Update the tail to the tail of the other list
        }
        count += other.count; // Update the count
        other.head = nullptr; // Clear the other list
        other.tail = nullptr;
        other.count = 0; // Reset the count of the other list
    }

    ~List() {
        while (head) {
            Node* temp = head;
            head = head->next;
            delete temp;
        }
    }
};

int main() {
    List list1, list2;
    int choice;
    do {
        cout << "1. Add Member to List 1\n2. Remove Member from List 1\n3. Display List 1\n4. Display Reverse of List 1\n5. Add Member to List 2\n6. Concatenate List 2 to List 1\n7. Display List 1\n8. Exit\n";
        cin >> choice;

        // Input validation
        while (cin.fail() || choice < 1 || choice > 8) {
            cout << "Invalid input. Please enter a number between 1 and 8: ";
            cin.clear(); // Clear the error flag
            cin.ignore(10000, '\n'); // Discard invalid input
            cin >> choice;
        }

        switch (choice) {
            case 1: list1.addMember(); break;
            case 2: list1.remove(); break;
            case 3: list1.displayList(); break;
            case 4: list1.displayReverse(); break;
            case 5: list2.addMember(); break;
            case 6: list1.concatenate(list2); break;
            case 7: list1.displayList(); break;
            case 8: break;
        }
    } while (choice != 8);

    return 0;
}

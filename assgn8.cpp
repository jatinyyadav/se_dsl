#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* prev;
    Node* next;
};

// Function to append data to the list
void append(Node*& head, int data) {
    Node* newNode = new Node();
    newNode->data = data;
    newNode->next = nullptr;

    if (head == nullptr) {
        newNode->prev = nullptr;
        head = newNode;
        return;
    }

    Node* temp = head;
    while (temp->next != nullptr) {
        temp = temp->next;
    }
    temp->next = newNode;
    newNode->prev = temp;
}

// Function to display the list
void display(Node* head) {
    while (head != nullptr) {
        cout << head->data;
        head = head->next;
    }
    cout << endl;
}

// Function to compute 1's complement
void onesComplement(Node* head) {
    Node* temp = head;
    while (temp != nullptr) {
        temp->data = (temp->data == 0) ? 1 : 0;
        temp = temp->next;
    }
}

// Function to compute 2's complement
void twosComplement(Node* head) {
    onesComplement(head);

    Node* temp = head;
    while (temp->next != nullptr) {
        temp = temp->next;
    }

    int carry = 1;
    while (temp != nullptr && carry) {
        int sum = temp->data + carry;
        temp->data = sum % 2;
        carry = sum / 2;
        temp = temp->prev;
    }
}

// Function to add two binary numbers
Node* addBinary(Node* head1, Node* head2) {
    Node* result = nullptr;
    Node* temp1 = head1;
    Node* temp2 = head2;

    // Move to the end of both lists
    while (temp1->next != nullptr) temp1 = temp1->next;
    while (temp2->next != nullptr) temp2 = temp2->next;

    int carry = 0;
    while (temp1 != nullptr || temp2 != nullptr || carry) {
        int sum = carry;
        if (temp1 != nullptr) {
            sum += temp1->data;
            temp1 = temp1->prev;
        }
        if (temp2 != nullptr) {
            sum += temp2->data;
            temp2 = temp2->prev;
        }

        append(result, sum % 2);
        carry = sum / 2;
    }

    // Reverse result to correct order
    Node* prev = nullptr;
    Node* current = result;
    Node* next = nullptr;
    while (current != nullptr) {
        next = current->next;
        current->next = prev;
        current->prev = next;
        prev = current;
        current = next;
    }
    return prev;
}

int main() {
    Node* binary1 = nullptr;
    Node* binary2 = nullptr;

    int n;
    cout << "Enter the number of bits for the binary number: ";
    cin >> n;

    cout << "Enter the binary number 1: ";
    for (int i = 0; i < n; i++) {
        int bit;
        cin >> bit;
        append(binary1, bit);
    }

    cout << "Enter the binary number 2: ";
    for (int i = 0; i < n; i++) {
        int bit;
        cin >> bit;
        append(binary2, bit);
    }

    cout << "Binary number 1: ";
    display(binary1);
    cout << "Binary number 2: ";
    display(binary2);

    cout << "1's complement of binary 1: ";
    onesComplement(binary1);
    display(binary1);

    cout << "2's complement of binary 1: ";
    twosComplement(binary1);
    display(binary1);

    cout << "Sum of binary numbers: ";
    Node* sum = addBinary(binary1, binary2);
    display(sum);

    return 0;
}

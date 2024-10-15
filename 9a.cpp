#include <iostream>
#include <stack>
#include <cctype>
using namespace std;

// Function to reverse string using stack
void reverseString(string str) {
    stack<char> s;
    for (char ch : str) {
        if (isalnum(ch)) { // Push letters and digits to the stack
            s.push(tolower(ch));
        }
    }

    cout << "Reversed String: ";
    while (!s.empty()) {
        cout << s.top();
        s.pop();
    }
    cout << endl;
}

// Function to check if a string is a palindrome
bool isPalindrome(string str) {
    stack<char> s;
    string cleanedStr = "";

    // Push characters to stack and build cleaned string
    for (char ch : str) {
        if (isalnum(ch)) {
            s.push(tolower(ch));
            cleanedStr += tolower(ch);
        }
    }

    string reversedStr = "";
    while (!s.empty()) {
        reversedStr += s.top();
        s.pop();
    }

    return cleanedStr == reversedStr;
}

int main() {
    string input;
    cout << "Enter a string: ";
    getline(cin, input);

    reverseString(input);

    if (isPalindrome(input)) {
        cout << "The string is a palindrome." << endl;
    } else {
        cout << "The string is not a palindrome." << endl;
    }

    return 0;
}

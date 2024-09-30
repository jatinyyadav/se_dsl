#include <iostream>
#include <string>

using namespace std;

struct MemberNode {
    string memberName;
    long memberPRN;
    MemberNode* nextMember;

    MemberNode() : memberPRN(0), nextMember(nullptr) {}
};

class MemberList {
private:
    MemberNode* headNode;
    MemberNode* tailNode;
    int memberCount;

public:
    MemberList() : headNode(nullptr), tailNode(nullptr), memberCount(0) {}

    void addNewMember() {
        int numMembers;
        cout << "Enter number of members to add: ";
        cin >> numMembers;

        for (int i = 0; i < numMembers; i++) {
            MemberNode* newMember = new MemberNode;
            cout << "Enter Member Name: ";
            cin >> newMember->memberName;
            cout << "Enter PRN of Member: ";
            cin >> newMember->memberPRN;

            if (!headNode || newMember->memberPRN < headNode->memberPRN) {
                newMember->nextMember = headNode;
                headNode = newMember;
                if (!tailNode) tailNode = newMember; // Update tail if list is empty
            } else if (!tailNode || newMember->memberPRN > tailNode->memberPRN) {
                tailNode->nextMember = newMember;
                tailNode = newMember;
            } else {
                MemberNode* currentNode = headNode;
                while (currentNode->nextMember && currentNode->nextMember->memberPRN < newMember->memberPRN) {
                    currentNode = currentNode->nextMember;
                }
                newMember->nextMember = currentNode->nextMember;
                currentNode->nextMember = newMember;
                if (!newMember->nextMember) tailNode = newMember; // Update tail if new member is last
            }
            memberCount++;
        }
    }

    void removeMember() {
        if (!headNode) {
            cout << "Error: List is empty!" << endl;
            return;
        }

        long prnToRemove;
        cout << "Enter PRN of member to remove: ";
        cin >> prnToRemove;

        if (headNode->memberPRN == prnToRemove) {
            MemberNode* tempNode = headNode;
            headNode = headNode->nextMember;
            if (!headNode) tailNode = nullptr; // Update tail if list becomes empty
            delete tempNode;
        } else {
            MemberNode* currentNode = headNode;
            while (currentNode->nextMember && currentNode->nextMember->memberPRN != prnToRemove) {
                currentNode = currentNode->nextMember;
            }
            if (currentNode->nextMember) {
                MemberNode* tempNode = currentNode->nextMember;
                currentNode->nextMember = currentNode->nextMember->nextMember;
                if (!currentNode->nextMember) tailNode = currentNode; // Update tail if removed node was last
                delete tempNode;
            } else {
                cout << "Member not found!" << endl;
            }
        }
        memberCount--;
    }

    void showList() {
        MemberNode* currentNode = headNode;
        while (currentNode) {
            cout << "Name: " << currentNode->memberName << ", PRN: " << currentNode->memberPRN << endl;
            currentNode = currentNode->nextMember;
        }
    }

    void reverseDisplay(MemberNode* node) {
        if (!node) return;
        reverseDisplay(node->nextMember);
        cout << "Name: " << node->memberName << ", PRN: " << node->memberPRN << endl;
    }

    void showReverse() {
        if (!headNode) {
            cout << "The list is empty!" << endl;
            return;
        }
        reverseDisplay(headNode);
    }

    void mergeLists(MemberList& otherList) {
        if (!otherList.headNode) return; // If the other list is empty

        if (!headNode) { // If the current list is empty
            headNode = otherList.headNode;
            tailNode = otherList.tailNode;
        } else {
            tailNode->nextMember = otherList.headNode; // Link the end of current list to the start of the other
            tailNode = otherList.tailNode; // Update the tail to the tail of the other list
        }
        memberCount += otherList.memberCount; // Update the count
        otherList.headNode = nullptr; // Clear the other list
        otherList.tailNode = nullptr;
        otherList.memberCount = 0; // Reset the count of the other list
    }

    ~MemberList() {
        while (headNode) {
            MemberNode* tempNode = headNode;
            headNode = headNode->nextMember;
            delete tempNode;
        }
    }
};

int main() {
    MemberList listA, listB;
    int userChoice;
    do {
        cout << "1. Add Member to List A\n2. Remove Member from List A\n3. Display List A\n4. Display Reverse of List A\n5. Add Member to List B\n6. Merge List B into List A\n7. Display List A\n8. Exit\n";
        cin >> userChoice;

        switch (userChoice) {
            case 1: listA.addNewMember(); break;
            case 2: listA.removeMember(); break;
            case 3: listA.showList(); break;
            case 4: listA.showReverse(); break;
            case 5: listB.addNewMember(); break;
            case 6: listA.mergeLists(listB); break;
            case 7: listA.showList(); break;
            case 8: break;
        }
    } while (userChoice != 8);

    return 0;
}

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head) {
            return head;
        }

        ListNode* curr = head;
        ListNode* newHead = new ListNode;
        newHead->val = head->val;
        int previousValue = head->val;
        ListNode* save = newHead;
        while (curr) {
            if (curr->val != previousValue) {
                cout << previousValue;
                cout << " " << curr->val<<endl;
                previousValue = curr->val;
                ListNode* newNode = new ListNode;
                newNode->val = curr->val;
                newHead->next = newNode;
                newHead = newHead->next;
            }
            curr = curr->next;
        }
        return save;
    }
};
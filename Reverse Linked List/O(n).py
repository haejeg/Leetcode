class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        temp = head
        while temp.next:
            right = temp.next
            temp.next = right.next
            right.next = head
            head = right    
        return head

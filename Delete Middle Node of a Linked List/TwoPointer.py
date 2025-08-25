# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        normal = head
        double = head
        previous = None
        while double and double.next:
            previous = normal
            normal = normal.next
            double = double.next.next
        # print(previous, normal, double)
        if normal == double:
            # print("Returning Blank")
            return None
        previous.next = normal.next
        # print("PRINTING HEAD")
        # print(head)
        return head
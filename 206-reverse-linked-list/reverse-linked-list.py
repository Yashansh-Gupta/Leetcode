# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        t=head
        c=0
        while t:
            c+=1
            t=t.next
        if head is not None:
            temp=head.next
            prev=head.next
            head.next=None
            for i in range(c):
                if temp is not None:
                    if temp.next is not None:
                        temp=temp.next
                        prev.next=head
                        head=prev
                        prev=temp
                    else:
                        temp.next=head
                
        return head
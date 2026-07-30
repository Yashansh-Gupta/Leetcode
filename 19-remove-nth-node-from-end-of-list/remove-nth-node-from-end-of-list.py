# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        temp=head
        prev=head
        c=0
        if head.next==None and n==1:
            return None
        while temp:
            c+=1
            temp=temp.next
        temp=head
        q=c-n+1
        f=1
        if q==1:
            head=head.next
            return head

        while temp and f<q:
            f+=1
            prev=temp
            temp=temp.next
        if temp:
            prev.next=temp.next

        return head



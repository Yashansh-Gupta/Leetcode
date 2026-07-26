# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        c = 0
        temp = head

        while temp:
            c += 1
            temp = temp.next

        count=(c//2)+1
        t=1
        tp=head
        while tp  and t<count:
            t+=1
            tp=tp.next
        return tp
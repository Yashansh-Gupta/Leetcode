# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        c1=0
        temp1=headA
        while temp1:
            c1 += 1
            temp1 = temp1.next
        temp1=headA
        c2=0
        temp2=headB
        while temp2:
            c2+=1
            temp2=temp2.next
            
        temp2=headB
        if c1>c2:
            q=c1-c2
            for i in range(q):
                    temp1=temp1.next
        else:
            q=c2-c1
            for i in range(q):
                    temp2=temp2.next

        while temp1 and temp2:
            if temp1==temp2:
                return temp1
            else:
                temp1=temp1.next
                temp2=temp2.next
        return None
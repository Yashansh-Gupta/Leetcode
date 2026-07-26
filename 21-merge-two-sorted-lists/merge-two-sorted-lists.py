# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1=[]
        temp1=list1
        while temp1:
            l1.append(temp1.val)
            temp1=temp1.next

        l2=[]
        temp2=list2
        while temp2:
            l2.append(temp2.val)
            temp2=temp2.next
        
        q=l1+l2
        q.sort()
        
        if len(q)==0:
            return None

        head=ListNode(q[0])
        qw=head
        for i in range(1,len(q)):
            qw.next=ListNode(q[i])
            qw=qw.next

        return head
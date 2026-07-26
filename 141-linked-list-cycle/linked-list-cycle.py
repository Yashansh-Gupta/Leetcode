# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        q=set()
        temp=head
        found=False
        while temp and temp.next:
            q.add(temp)
            temp=temp.next
            if temp in q:
                return True
            else:
                found=False
        return found

            
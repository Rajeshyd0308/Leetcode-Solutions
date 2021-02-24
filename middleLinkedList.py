# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i = 0
        head_cpy = head
        while(head_cpy!=None):
            head_cpy = head_cpy.next
            # print(head_cpy.val)
            # print(head.val)
            i+=1
        # print(i)
        i=i//2
        j=0
        
        while(j<=i):
            if j==i:
                return head
            else:
                head = head.next
                j+=1
        

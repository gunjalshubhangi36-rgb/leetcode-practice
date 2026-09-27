# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

    

        while True:
            kth = prev

            for i in range(k):
                kth = kth.next


                if kth is None:
                    return dummy.next
        
            group_next = kth.next

            previous = group_next
            current = prev.next


            while current != group_next:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node

            
            temp = prev.next
            prev.next = kth
            prev = temp


        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        
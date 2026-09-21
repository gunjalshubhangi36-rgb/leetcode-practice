# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):

        if not lists:
            return None
        
        result = lists[0]

        for i in range(1, len(lists)):
            result = self.mergeTwoList(result, lists[i])

        return result
        
    def mergeTwoList(self, list1, list2):
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:

            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
        
            current = current.next
        
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        return dummy.next

        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        
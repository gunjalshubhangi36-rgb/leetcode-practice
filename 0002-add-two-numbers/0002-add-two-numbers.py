# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Create a dummy node to simplify result list construction
        dummy = ListNode()

        # Pointer to build the new linked list
        current = dummy

        # Initialize carry
        carry = 0

        # Traverse both linked lists until both are exhausted
        # and there is no carry left
        while l1 or l2 or carry:

            # Get current values (0 if list has ended)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate total
            total = val1 + val2 + carry

            # Update carry
            carry = total // 10

            # Digit to store in current node
            digit = total % 10

            # Create new node and attach it
            current.next = ListNode(digit)

            # Move current pointer
            current = current.next

            # Move l1 to next node if available
            if l1:
                l1 = l1.next

            # Move l2 to next node if available
            if l2:
                l2 = l2.next

        # Return the head of the new linked list
        return dummy.next
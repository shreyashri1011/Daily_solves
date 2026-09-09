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
        # Step 1: Convert l1 into a string
        num1 = ""
        current = l1

        while current:
            num1 += str(current.val)
            current = current.next

        # Reverse the string
        num1 = num1[::-1]

        # Step 2: Convert l2 into a string
        num2 = ""
        current = l2

        while current:
            num2 += str(current.val)
            current = current.next

        # Reverse the string
        num2 = num2[::-1]

        # Step 3: Convert to integers and add
        total = int(num1) + int(num2)

        # Step 4: Convert answer to string
        total = str(total)

        # Step 5: Reverse it because linked list
        # stores digits in reverse order
        total = total[::-1]

        # Step 6: Build the result linked list
        dummy = ListNode(0)
        current = dummy

        for digit in total:
            current.next = ListNode(int(digit))
            current = current.next

        return dummy.next
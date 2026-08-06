class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy_head=ListNode(-1,head)
        left_prev,current_node=dummy_head,head
        for i in range(left -1):
            left_prev,current_node=current_node,current_node.next
        prev=None
        for i in range(right-left+1):
            next_pointer=current_node.next
            current_node.next=prev
            prev,current_node=current_node,next_pointer
        left_prev.next.next=current_node
        left_prev.next=prev
        return dummy_head.next
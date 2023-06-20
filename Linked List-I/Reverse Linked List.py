class Solution:
    def reverseList(self, head):
        new_head = None
        while head is not None:
            next_node = head.next
            head.next = new_head
            new_head = head
            head = next_node
        return new_head
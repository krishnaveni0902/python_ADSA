'''
Circular linked list: last node connects to the first node
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1

def traverse():
    curr = node1
    while curr:
        print(curr.data, end = " -> ")
        curr = curr.next
        if curr == node1:
            break
    print("HEAD")
traverse()

#leet code - 206
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        
        prev = None
        curr = head 
        while curr:
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp
        return prev 
        """

        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head 
        head.next = None 
        return new_head


#leetcode - 141
class Solution(object):
    def hasCycle(self, head):
        '''
        slow = head 
        fast = head 
        while fast is not None and fast.next is not None:
            slow = slow.next 
            fast = fast.next.next
            if slow == fast:
                return True 
        return False '''
        a = set()
        curr = head 
        while curr:
            if curr in a:
                return True
            a.add(curr)
            curr = curr.next
        return False
        
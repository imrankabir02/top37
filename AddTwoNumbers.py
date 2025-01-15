# Add Two Numbers

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def recursion(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
        if not l1 and not l2 and carry == 0:
            return None

        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        
        carry, val = divmod(v1 + v2 + carry, 10)
        
        next_node = self.recursion(
            l1.next if l1 else None,
            l2.next if l2 else None,
            carry
        )
        return ListNode(val, next_node)
    
    def addWithRecursion(self, l1:Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.recursion(l1, l2, 0)
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode])-> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            value = v1 + v2 + carry
            carry = value // 10
            value %= 10
            current.next = ListNode(value)
            
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next        
    
def listToLinkedList(list):
    dummy = ListNode()
    current = dummy
    for val in list:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linkedListToList(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
    
solution = Solution()

l1 = listToLinkedList([1,2,3])
l2 = listToLinkedList([4,3,2])

print(f"Input: l1={linkedListToList(l1)}, l2={linkedListToList(l2)}")
result = solution.addWithRecursion(l1, l2)
print(f"Output with recursion: {linkedListToList(result)}")

# Iterative method
l3 = listToLinkedList([3, 3, 1, 4])
l4 = listToLinkedList([1, 5, 4])

print(f"Input: l3={linkedListToList(l3)}, l4={linkedListToList(l4)}")
result_iterative = solution.addTwoNumbers(l3, l4)
print(f"Output using iteration: {linkedListToList(result_iterative)}")
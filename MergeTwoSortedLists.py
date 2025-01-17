# Merge two sorted lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
    
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

sol = Solution()

list1 = [1,3,4]
list2 = [1,2,5]

l1 = listToLinkedList(list1)
l2 = listToLinkedList(list2)

res = sol.mergeTwoLists(l1, l2)

print(linkedListToList(res))

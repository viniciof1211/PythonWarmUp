# Single Linked List node and pointers/ref implementations + methods to traverse it, search, sort, etc ...

class SingleLLNode(object):
    def __init__(self, value):
        self.value = value
        self.next= None
    def __str__(self):
        output = "{"
        node = self
        while node is not None:
            output += str(node.value)
            if node.next is not None:
                next_node = node.next
                output += ", "
            node = node.next
        return output + "}"

    def reverse(self):
        prev = None
        curr = self
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev # Return the new head of the reversed single linked list

# Helper Methods
def build_sll(values):
    if not values:
        return None
    head = SingleLLNode(values)
    current = head
    for value in values[1:]:   # ignore the head to avoid duplication
        current.next = SingleLLNode(value)
        current = current.next
    return head
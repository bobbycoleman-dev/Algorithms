# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class List:
    def __init__(self, head=None):
        self.head = head

    def insert(self, val):
        new_node = ListNode(val)

        if self.head == None:
            self.head = new_node
            return self

        r = self.head
        while r.next != None:
            r = r.next

        r.next = new_node

        return self

    def insertMany(self, vals):
        for val in vals:
            self.insert(val)

        return self

    def printList(self):
        arr = []
        r = self.head

        while r != None:
            arr.append(r.val)
            r = r.next

        return arr


# l1 = List().insertMany([2, 4, 3])
# l2 = List().insertMany([5, 6, 4])

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))


def addTwoNumbers(l1, l2):
    dummyHead = ListNode(0)
    tail = dummyHead
    carry = 0

    while l1 is not None or l2 is not None or carry != 0:
        digit1 = l1.val if l1 is not None else 0
        digit2 = l2.val if l2 is not None else 0

        sum = digit1 + digit2 + carry
        digit = sum % 10
        carry = sum // 10

        newNode = ListNode(digit)
        tail.next = newNode
        tail = tail.next

        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None

    result = dummyHead.next
    dummyHead.next = None
    return result


print(addTwoNumbers(l1, l2))

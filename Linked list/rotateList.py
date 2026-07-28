def rotate_right(head,k):
    if not head or not head.next or k==0:
        return head
    
    tail=head
    length=1
    while tail.next!=None:
        tail=tail.next
        length+=1


    k%=length
    if k==0:
        return head
    tail.next=head
    new_tail=head
    steps=length-k-1
    for _ in range(steps):
        new_tail=new_tail.next

    new_head=new_tail.next
    
    new_tail.next=None

    return new_head


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(arr):
    dummy = ListNode()
    current = dummy

    for num in arr:
        current.next = ListNode(num)
        current = current.next

    return dummy.next


def print_linked_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()
print(rotate_right(head,2))

head = create_linked_list([1,2,3,4,5])

new_head = rotate_right(head, 2)

print_linked_list(new_head)
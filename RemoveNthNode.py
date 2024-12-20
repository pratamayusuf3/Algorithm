'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    # Dummy node untuk menangani edge case ketika node pertama dihapus
    dummy = ListNode(0, head)
    first = dummy
    second = dummy

    # Geser pointer 'first' sejauh n + 1 langkah
    for _ in range(n + 1):
        first = first.next

    # Geser 'first' dan 'second' bersama-sama sampai 'first' mencapai akhir
    while first is not None:
        first = first.next
        second = second.next

    # Hapus node ke-n dari belakang
    second.next = second.next.next

    # Kembalikan kepala linked list yang baru
    return dummy.next


def removeNthFromEnd2(head: ListNode, n: int) -> ListNode:
    fast, slow = head, head
    for _ in range(n): 
        fast = fast.next
    if not fast: 
        return head.next
    while fast.next: 
        fast, slow = fast.next, slow.next
    slow.next = slow.next.next
    return head


# Fungsi untuk membuat linked list dari list Python
def create_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


# Fungsi untuk mencetak linked list
def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)


# Contoh Input
head = create_linked_list([1, 2, 3, 4, 5])
n = 2

# Hapus node ke-n dari akhir
new_head = removeNthFromEnd(head, n)

# Cetak hasil
print_linked_list(new_head)  # Output: [1, 2, 3, 5]

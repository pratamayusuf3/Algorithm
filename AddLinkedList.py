class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addLinkedList(l1,l2):
    dummy_head = ListNode(0)
    tail = dummy_head
    carry = 0
    
    while l1 is not None or l2 is not None or carry != 0:
        digit1 = l1.val if l1 is not None else 0
        digit2 = l2.val if l2 is not None else 0
        
        total = digit1 + digit2 + carry
        carry = total // 10
        new_digit = total % 10
        
        tail.next = ListNode(new_digit)
        tail = tail.next
         
        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None
        
    return dummy_head.next


def printLinkedList(head):
    current = head
    while current is not None:
        print(current.val, end=" -> ")
        current = current.next
    print("null")


if __name__ == "__main__":
    print("Program Dimulai")
    
    # Membuat 2 linked list
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    
    # Menghitung hasil penjumlahan dua linked list
    result = addLinkedList(l1,l2)
    
    # Mencetak Hasil
    print("Hasil :")
    printLinkedList(result)
    
    print("Program Selesai")
        
        
'''    
# Menggunakan metode Class
    
class AddLinkedList:
    
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode(0)
        tail = dummy_head
        carry = 0
        
        while l1 is not None or l2 is not None or carry != 0: 
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0
        
            total = digit1 + digit2 + carry
            digit = total % 10
            carry = total // 10
            
            tail.next = ListNode(digit)
            tail = tail.next
            
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            
        return dummy_head.next
    
    @staticmethod
    def print_linked_list(head):
        current = head
        while current is not None:
            print(f"{current.val} -> ", end="")
            current = current.next
        print("null")
       
        
if __name__ == "__main__":
    print("Program dimulai")
    
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    # Panggil program utama
    solution = AddLinkedList()
    result = solution.addTwoNumbers(l1, l2)
    #result = AddLinkedList.addTwoNumbers

    # Print hasil
    print("Hasil: ", end="")
    solution.print_linked_list(result)         # line code ini bisa jalan / opsi 1
    #AddLinkedList.print_linked_list(result)  # bisa panggil menggunakan alternatif static method / opsi 2

    print("Program selesai")
'''
    
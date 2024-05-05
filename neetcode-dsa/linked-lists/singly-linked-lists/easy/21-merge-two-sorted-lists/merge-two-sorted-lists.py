class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:  # Ensure to compare correctly, it seems you have the condition reversed
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next  # Corrected here, no more `tail.tail`

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
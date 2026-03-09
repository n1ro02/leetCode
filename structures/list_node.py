class ListNode:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next

    def build_list(self,arr):
        dummy = ListNode()
        cur = dummy

        for v in arr:
            cur.next = ListNode(v)
            cur = cur.next

        return dummy.next

    def print_list(self,head):
        cur = head
        res = []

        while cur:
            res.append(cur.val)
            cur = cur.next
        print(res)

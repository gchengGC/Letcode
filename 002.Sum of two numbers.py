class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = 0
        result = ListNode(val=0, next=None)
        iter1 = result
        while 1:
            val = (l1.val + l2.val + ret) % 10
            ret = (l1.val + l2.val + ret) // 10

            iter1.next = ListNode(val=val, next=None)
            iter1 = iter1.next
            l1 = l1.next or ListNode(val=0, next=None)
            l2 = l2.next or ListNode(val=0, next=None)
            if (
                l1.next is None
                and l2.next is None
                and l1.val == 0
                and l2.val == 0
                and not ret
            ):
                break
        return result.next

if __name__ == '__main__':
    a = Solution()
    nums = [1,1,4,5,6,7,14]
    nums2 = [2,5,9,8,7]

    print(a.addTwoNumbers(nums,nums2))
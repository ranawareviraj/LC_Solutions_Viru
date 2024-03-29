/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode dummy = new ListNode(-1);
        ListNode prev = dummy;
        ListNode curr = head;
        
        while(curr != null && curr.next != null){
            if(curr.val != curr.next.val){
                prev.next = curr;
                prev = curr;
            }
            curr = curr.next;
        }
        
        prev.next = curr;
        return dummy.next;
    }
}
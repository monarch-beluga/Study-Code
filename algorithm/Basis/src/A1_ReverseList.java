public class A1_ReverseList {
    static class ListNode{
        int data;
        ListNode next;

        public ListNode(int data, ListNode next) {
            this.data = data;
            this.next = next;
        }
    }
    public static void main(String[] args) {
        // 链表
        ListNode node5 = new ListNode(5, null);
        ListNode node4 = new ListNode(4, node5);
        ListNode node3 = new ListNode(3, node4);
        ListNode node2 = new ListNode(2, node3);
        ListNode node1 = new ListNode(1, node2);

        System.out.println("原链表：");
        for(ListNode i = node1; i != null; i = i.next){
            System.out.print(i.data+"->");
        }

        ListNode prev = iteration(node1);
        System.out.println("\n迭代反转后的链表：");
        for(ListNode i = prev; i != null; i = i.next){
            System.out.print(i.data+"->");
        }

        ListNode new_head = recursion(prev);
        System.out.println("\n递归再次反转后的链表：");
        for(ListNode i = new_head; i != null; i = i.next){
            System.out.print(i.data+"->");
        }
    }
    // 迭代
    public static ListNode iteration(ListNode head){
        ListNode next, prev = null;
        ListNode curr = head;
        while (curr != null){
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
    // 递归
    public static ListNode recursion(ListNode head){
        if (head == null || head.next == null){
            return head;
        }else {
            ListNode new_head = recursion(head.next);
            head.next.next = head;
            head.next = null;
            return new_head;
        }
    }
}

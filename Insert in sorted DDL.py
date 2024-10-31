class Solution:
    #Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
    #code here
        newnode=Node(x)
        if newnode.data<=head.data:
            newnode.next=head
            head=newnode
            return head
        cur=head
        while cur.next!=None and cur.next.data<=x:
            cur=cur.next
        if cur.next==None:
            cur.next=newnode
        else:
            newnode.next=cur.next
            cur.next=newnode
        return head
class Node:
    def __init__(self,data):
        self.info=data
        self.link=None
class singlyLL:
    def __init__(self):
        self.start=None
    def create(self):
        data=input("Enter the data:")
        newnode=Node(data)
        if self.start is None:
            self.start=newnode
        else:
            q=self.start
            while q.link is not None:
                q=q.link
            q.link=newnode
    def add_begin(self):
        data=input("Enter the data at begin")
        newnode=Node(data)
        if self.start is None:
            self.start=newnode
        else:
            newnode.link=self.start
            self.start=newnode
    def del_begin(self):
        if self.start is None:
            print("Linked list is empty")
        else:
            self.start=self.start.link
    def display(self):
        if self.start is None:
            print("Linked list is empty")
        else:
            print("Linked list elements are:",end=" ")
            q=self.start
            while q is not None:
                print(q.info,end=" ")
                q=q.link
            print("")
    def count(self):
        if self.start is None:
            print("List is empty")
        else:
            q=self.start
            cnt=0
            while q is not None:
                cnt=cnt+1
                q=q.link
            print("Nof nodes are ",cnt)
            if cnt%2==0:
                mid=cnt//2
            else:
                mid=(cnt//2)+1
            i=1
            q=self.start
            while i<mid:
                q=q.link
                i=i+1
            if cnt%2!=0:
                print(q.info)
            else:
                print(q.info," ",q.link.info)
    def del_last(self):
        if self.start is None:
            print("Linked list is empty")
        if self.start.link is None:
            print("Only one node in linked list")
            self.start=None
        q=self.start
        while q.link.link is not None:
            q=q.link
        q.link=None
        s.display()
s=singlyLL()
while True:
    print("")
    print("1.Create a node\n2.Display\n3.Add node at begin\n4.Delete node at begin\n5.find_mid\n6.Delete at end\n7.Exit\n")
    choice=int(input("Enter your choice"))
    match choice:
        case 1:
            s.create()
        case 2:
            s.display()
        case 3:
            s.add_begin()
        case 4:
            s.del_begin()
        case 5:
            s.count()
        case 6:
            s.del_last()
        case 7:
            break
        case _:
            print("Invalid choice")
class Node:
    def __init__(self,data):
        self.info=data
        self.link=None
class SLL:
    def __init__(self):
        self.start=None
    def create(self):
        data=int(input("Enter the data:"))
        newnode=Node(data)
        if self.start is None:
            self.start=newnode
        else:
            q=self.start
            while q.link is not None:
                q=q.link
            q.link=newnode
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
    def union(self,s1):
        print(" ")
        print("Union")
        q=self.start
        while q.link is not None:
            j=q.link
            while j is not None:
                if q.info==j.info:
                    j.info=None
                j=j.link
            q=q.link
        q=self.start
        while q is not None:
            if q.info is not None:
                print(q.info,end=" ")
            q=q.link

        q=s1.start
        while q.link is not None:
            j=q.link
            while j is not None:
                if q.info==j.info:
                    j.info=None
                j=j.link
            q=q.link

        q=s1.start
        while q is not None:
            if q.info is not None:
                q1=self.start
                flag=True
                while q1 is not None:
                    if q1.info==q.info:
                        flag==False
                        break
                    q1=q1.link
                if flag:
                    print(q.info,end=" ")
                q=q.link
        print("")
    def intersection(self,s1):
        print("")
        print("intersection ")
        q=self.start
        while q is not None:
            if q.info is not None:
                q1=s1.start
                while q1 is not None:
                    if q1.info==q.info:
                        print(q.info,end="")
                        break
                    q1=q1.link
            q=q.link
        print("")
s=SLL()
s1=SLL()
while True:
    print("")
    print("1.Create a node for SLL1\n2.Display SLL1\n")
    print("3.Create a node for SLL2\n4.Display SLL2\n")
    print("5.Union and intersection of two SLL\n6.Exit\n")
    choice=int(input("Enter your choice"))
    match choice:
        case 1:
            s.create()
        case 2:
            s.display()
        case 3:
            s1.create()
        case 4:
            s1.display()
        case 5:
            s.union(s1)
            s.intersection(s1)
        case 6:
            s.del_last()
        case 7:
            break
        case _:
            print("Invalid choice")
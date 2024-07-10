class Stack:
    def __init__(self,size):
        self.items=[]
        self.top=-1
        self.size=size
    def is_empty(self):
        return top==-1
    def push(self,item):
            if self.size -1 ==self.top:
                print("Stack overflow")
            else:
                self.top +=1
                self.size+=1 
                self.items[self.top]=item
    def pop(self):
        if self.is_empty():
            print("Stack underflow")
        else:
            print(self.items.pop())
            self.top-=1
            self.size-=1
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            #print("Elements are:",self.items)
            for i in self.items:
                print(i,end=" ")
            print("")
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Peek element is",self.items[-1])
size=int(input("Enter size:"))
s=Stack(size)
while True:
    print("")
    print("1:Push\n2:Pop\n3:Display\n4:Peek\n5:Exit\n")
    choice=input("Enter your choice")
    match choice:
        case '1':
            item=int(input("Enter the element to push:"))
            s.push(item)
        case '2':
            s.pop()
        case '3':
            s.display()
        case '4':
            s.peek()
        case '5':
            print("Exit")
            break
        case _:
            print("Invalid choice")
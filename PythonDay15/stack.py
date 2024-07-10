class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,item):
            self.items.append(item)
    def pop(self):
        if self.is_empty():
            print("Stack underflow")
        else:
            print(self.items.pop())
            self.display()
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
s=Stack()
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
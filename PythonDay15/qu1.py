class Queue:
    def __init__(self):
        self.items=[]
        self.front=-1
        self.rear=-1
        self.size=size
    def enqueue(item):
        if self.rear==self.size-1:
            print("Queue is full")
        else:
            if self.front==-1:
                front=0
                self.rear+=1
                #self.items.append(item)
                self.queue[self.rear]=item
                self.size+=1
    def dequeue(item):
        if front ==-1 or front>rear:
            print("Queue is empty")
        else:
            print(self.items.pop(0))
            self.front-=1
    def is_empty():
        if(front==-1 or front>rear):
            print("Queue is empty")
    def peek(self):
        if is_empty():
            print("Queue is empty")
        else:
            print("Peek element is",self.items[0])
    def display():
        if is_empty:
            print("Queue is empty")
        else:
            for i in self.items:
                print(i,end="")
size=int(input("Enter size"))
q=Queue()
while True:
    print("")
    print("1:Enqueue\n2:Dequeue\n3:Display\n4:Peek\n5:Exit\n")
    choice=input("Enter your choice")
    match choice:
        case '1':
            item=int(input("Enter the element to push:"))
            q.enqueue(item)
        case '2':
            q.dequeue()
        case '3':
            q.display()
        case '4':
            q.peek()
        case '5':
            print("Exit")
            break
        case _:
            print("Invalid choice")
        
class Node:
    def __init__(self,data):
        self.lchild=None
        self.info=data
        self.rchild=None
class BST:
    def __init__(self):
        self.root=None
    def create(self,data):
        if self.root is None:
            self.root=Node(data)
        else:
            self.insert(self.root,data)
    def insert(self,node,data):
        if data == node.info:
            print("duplicate element")
        elif data<node.info:
            if node.lchild is None:
                node.lchild=Node(data)
            else:
                self.insert(node.lchild,data)
        else:
            if node.rchild is None:
                node.rchild=Node(data)
            else:
                self.insert(node.rchild,data)
    def inorder(self,node):
        if node:
            self.inorder(node.lchild)
            print(node.info)
            self.inorder(node.rchild)
    def preorder(self,node):
        if node:
            print(node.info)
            self.preorder(node.lchild)
            self.preorder(node.rchild)
    def postorder(self,node):
        if node:
            self.postorder(node.lchild)
            self.postorder(node.rchild)
            print(node.info)
    def search(self,root,target):
        if root is None or root.info==target:
            return root
        if target<root.info:
            return self.search(root.lchild,target)
        return self.search(root.rchild,target)
obj=BST()
while True:
    print("\n1:create\n2:Inorder\n3:Preorder\n4:Postorder\n5:Search\n6:Exit\n")
    choice=int(input("Enter your choice"))
    match choice:
        case 1:
            data=int(input("Enter data"))
            obj.create(data)
        case 2:
            obj.inorder(obj.root)
        case 3:
            obj.preorder(obj.root)
        case 4:
            obj.postorder(obj.root)
        case 5:
            target=int(input("Enter target value"))
            result=obj.search(obj.root,target)
            if result:
                print("Node found")
            else:
                print("Not found")
        case 6:
            break
        case _:
            print("Invalid choice")
    
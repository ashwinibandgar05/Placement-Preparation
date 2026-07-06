from hashlib import new


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
class BST:
    def __init__(self):
        self.root=None

    def insert(self,root,key):
        if root==None:
            return Node(key)
        if key<root.data:
            root.left=self.insert(root.left,key)
        elif key>root.data:
            root.right=self.insert(root.right,key)
        return root
    
    def search(self,root,key):
        if root is None or root.data==key:
            return root
        
        if key<root.data:
            return self.search(root.left,key)
        else:
            return self.search(root.right,key)
        

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)    

    def preorder(self,root):
        if root:
            print(root.data ,end=" ")   
            self.preorder(root.left)
            self.preorder(root.right)
        

    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data ,end=" ") 

    def delete(self, root, key):
        # Tree is empty
        if root is None:
            return root

        # Search in left subtree
        if key < root.data:
            root.left = self.delete(root.left, key)

        # Search in right subtree
        elif key > root.data:
            root.right = self.delete(root.right, key)

        # Node found
        else:
            # Case 1 & 2: One child or no child

            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

            # Case 3: Two children
            temp = self.find_min(root.right)

            # Copy inorder successor
            root.data = temp.data

            # Delete inorder successor
            root.right = self.delete(root.right, temp.data)

        return root


bst=BST()

values=[30,50,20,60,10,80,70,90]

for value in values:
    bst.root=bst.insert(bst.root,value)
    

key=60
if bst.search(bst.root,key):
    print(f"{key} is found")

else:
    print("not found")

print("inorder")
bst.inorder(bst.root)
print("\npreorder")
bst.preorder(bst.root)

print("\nPostorder")
bst.postorder(bst.root)


bst.delete(bst.root, 60)
print("\nAfter deleting 60, inorder traversal:")

bst.inorder(bst.root)




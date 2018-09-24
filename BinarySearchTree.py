class Node():
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    def add(self, value):
        if value < self.data:
            if self.left is None:
                self.left = Node(value)
                return 
            else:
                return self.left.add(value)
        elif value > self.data:
            if self.right is None:
                self.right = Node(value)
                return
            else:
                return self.right.add(value)
        else:
            return None
    
    #return values from high to low
    def getValuesHTL(self):
        if self.right is not None:
            self.right.getValuesHTL()
        print(self.data, end=" ")
        if self.left is not None:
            self.left.getValuesHTL()
    
    #return values from low to high
    def getValuesLTH(self):
        if self.left is not None:
            self.left.getValuesLTH()
        print(self.data, end=" ")
        if self.right is not None:
            self.right.getValuesLTH()

    def findValue(self, value):
        if value == self.data:
            print("Found", value)
            return
        elif value < self.data:
            if self.left is not None:
                self.left.findValue(value)
        elif value > self.data:
            if self.right is not None:
                self.right.findValue(value)
        else:
            print("Not Found")
            return

class Tree():
    def __init__(self):
        self.head = None

    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            self.head.add(value)

    def traverseHTL(self):
        self.head.getValuesHTL()

    def traverseLTH(self):
        self.head.getValuesLTH()

    def search(self, value):
        self.head.findValue(value)
        
import random
def main():         
    tree = Tree()
    for i in range(100):
        tree.insert(random.randint(0, 100))
    tree.traverseHTL()
    tree.traverseLTH()
    tree.search(5)


if __name__ == '__main__':
    main()
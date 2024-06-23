from Node import Node
#implemeting maxheap using an array
class maxHeap():
    #capacity is max num of elements to store in heap
    def __init__(self, capacity):
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def getParent(self, index):
        return (index-1) // 2
    
    def getLeftChild(self, index):
        return (2 * index) + 1
    
    def getRightChild(self, index):
        return (2 * index) + 2
    
    def hasParent(self, index):
        return self.getParent(index) >= 0
    
    def hasLeftChild(self, index):
        return self.getLeftChild(index) < self.size
    
    def hasRightChild(self, index):
        return self.getRightChild(index) < self.size
    
    def parent(self, index):
        return (self.storage[self.getParent(index)]).data
    
    
    def leftChild(self, index):
        return self.storage[self.getLeftChild(index)].data
    
    def rightChild(self, index):
        return self.storage[self.getRightChild(index)].data
    
    def isFull(self):
        return self.size == self.capacity
    
    def swap(self, i1, i2):
        temp = self.storage[i1]
        self.storage[i1] = self.storage[i2]
        self.storage[i2] = temp

    def insert(self, data, path):
        if(self.isFull()):
            raise("Heap is Full")
        self.storage[self.size] = Node(data, path)
        self.size += 1
        self.heapifyUp(self.size - 1)

    def heapifyUp(self, index):
        if self.hasParent(index) and self.parent(index) < (self.storage[index]).data:
            self.swap(self.getParent(index), index)
            self.heapifyUp(self.getParent(index))
    
    def removeMax(self):
        if(self.size == 0):
            raise("Empty Heap")
        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapifyDown(0)
        return data
    
    def heapifyDown(self, index):
        biggest = index
        if (self.hasLeftChild(index) and self.storage[biggest].data < self.leftChild(index)):
            biggest = self.getLeftChild(index)
        if (self.hasRightChild(index) and self.storage[biggest].data < self.rightChild(index)):
            biggest = self.getRightChild(index)
        if (biggest != index):
            self.swap(index, biggest)
            self.heapifyDown(biggest)

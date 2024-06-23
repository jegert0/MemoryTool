class Node:
    def __init__(self, data, path) -> None:
        self.data = data
        self.path = path
    
    def getData(self):
        return self.data
    
    def getPath(self):
        return self.path
    
class DataFilesNode:
    def __init__(self, fileName = None, IP = 0, portNum = 0):
        self.fileName = fileName
        self.IP = IP
        self.portNum = portNum
        self.next = None
        self.prev = None

class doublyLinkedList:
    def __init__(self):
        self.start_node = None

    def insertToEmptyList(self, fileName, IP, portNum):
        if self.start_node is None:
            new_node = DataFilesNode(fileName, IP, portNum)
            self.start_node = new_node
        else:
            print("The list is empty")

    def insertToEnd(self, fileName, IP, portNum):
        if self.start_node is None:
            new_node = DataFilesNode(fileName, IP, portNum)
            self.start_node = new_node
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        new_node = DataFilesNode(fileName, IP, portNum)
        n.next = new_node
        new_node.prev = n

    def deleteAtStart(self):
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_prev = None

    def delete_at_end(self):
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None

    def Display(self):
        if self.start_node is None:
            print("The list is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print("Element is:", n.fileName, " ", n.IP, " ", n.portNum)
                n = n.next
        print("\n")

'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

class Node:
    def __init__(self,dataVal):
        self.dataVal = dataVal
        self.nextVal = None
        
class ALinkedList:
    def __init__(self):
        self.headVal = None
    
    def listPrint(self):
        printVal = self.headVal
        while printVal is not None:
            print(printVal.dataVal)
            printVal=printVal.nextVal
            
    def atBeginning(self,newData):
        NewNode = Node(newData)
        NewNode.nextVal = self.headVal
        self.headVal = NewNode
        
    def atEnd(self,newData):
        NewNode = Node(newData)
        if self.headVal is None:
            self.headVal = NewNode
            return
        laste = self.headVal
        while(laste.nextVal):
            laste=laste.nextVal
        laste.nextVal=NewNode
        
    def inBetween(self,middle_node,newData):
        if middle_node is None:
            print("the node is absent")
            
        NewNode = Node("Sat")
        NewNode.nextVal = middle_node.nextVal
        middle_node.nextVal = NewNode
        
list1 = ALinkedList()
list1.headVal = Node("Mon")
e2=Node("Tue")
e3=Node("Wed")

list1.headVal.nextVal = e2
e2.nextVal = e3

list1.atBeginning("Sun")
list1.atEnd("Fri")
list1.inBetween(list1.headVal.nextVal,"Sat")
list1.listPrint()

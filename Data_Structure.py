class Node(object):
    #初始化结点函数
    def __init__(self, data):
        self.data = data
        self.next = None
    
    #初始化头结点函数
        self.head = Node(None)

    def CreateSingleLinkedList(self):
        print("********************")
        cNode = self.head
        Element = input("输入：")
        while Element != 'q':
            nNode = Node(int(Element))
            cNode.next = nNode
            cNode = cNode.next
            Element = input("输入：")

    #尾端插入元素函数
    def InsertElementInTail(self):
        Element = input("输入：")
        if Element == 'q':
            return
        cNode = self.head
        nNode = Node(int(Element))
        while cNode.next != None:
            cNode = cNode.next
        cNode.next = nNode



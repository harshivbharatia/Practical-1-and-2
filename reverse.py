class Node:
    def __init__(self,value):
        self.value = value
        self.nextnode = None


    def traverse(head):
        temp = head
        while temp!= None:
            print(str(temp.value)+'')
            temp = temp.nextnode
'''
traverse(a)
'''


    def reverse(head):
        current = head
        Next = None
        prev = None
        while current:
            Next = current.nextnode
            current.nextnode= prev
            prev = current
            current = Next
        return prev
        '''
reverse(a)

traverse(d)
'''

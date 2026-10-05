'''
push -> insert 

'''
class Stack:
    def __init__(self):
        self.items = []
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is Empty"
    def peak(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is Empty"
    def is_empty(self):
        return len(self.items) == 0 
s = Stack()
s.push(10)
print(s.item())
print(s.pop)
print(s.peak)
print(s.is_empty())

#Using linked list:
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 
class Stack:
    def __init__(self):
        self.top = None 
    def push(self,data):
        new_node = Node(data)

#    def pop(self):
#       if not self.is_empty():
            




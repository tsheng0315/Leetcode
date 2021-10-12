"""
create linked list and stack calss;

linked list: append at the end , insert and delete at the first;

Stack: push and pop (return popped item)
"""
class Element(object):
    def __init__(self,value):
        self.value = value
        self.next = None

class Linked_list(object):
    def __init__(self, head = None):
        self.head = head

    def appand(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element            
        else: 
            self.head = new_element
    def insert_first(self, new_element):
        new_element.next =self.head
        self.head =new_element

    def delete_first(self):
        if self.head:
            delete_element = self.head
            self.head = delete_element.next
            return delete_element            
        else: 
            return None

class Stack(object):
    def __init__(self, top=None):
        self.ll = Linked_list(top) # top = head??
    
    def push(self,new_element):
        self.ll.insert_first(new_element)

    def pop(self):
        return self.ll.delete_first()         



    


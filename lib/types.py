

class Node(object):

    LAST_ADDED = None
    
    parent = None
    children = None
    value = None

    def __init__(self, value=None, parent=None):
        self.children = []
        self.parent = parent
        if value is not None:
            self.value = value.strip()
                
        Node.LAST_ADDED = self
    
    def add_child(self, value):
        child = Node(value=value, parent=self)
        self.children.append(child)
        
        return child
    
    def __str__(self):
        return '<Node(%s)' % self.value

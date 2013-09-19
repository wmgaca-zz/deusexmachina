import re

class Node(object):

    LAST_ADDED = None
    
    parent = None
    children = None
    value = None

    object_ = None
    
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


class State(object):

    STATES = {}

    def __init__(self, data):
        assert isinstance(data, basestring)
        assert data.startswith('state.')
        
        self.name = data.split('.')[1]
   
        assert self.name not in State.STATES
        
        State.STATES[self.name] = self

    def __str__(self):
        return '<State(%s)>' % self.name

PATTERNS = {
    r'^state\.[a-zA-Z][a-zA-Z0-9_-]*$': State
}

def get_object(data):
    if not isinstance(data, basestring):
        return None

    for pattern, cls in PATTERNS.items():
        if re.match(pattern, data):
            return cls(data)
    return None

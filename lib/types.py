import re


class Node(object):

    _last_added = None
    
    parent = None
    children = None
    value = None

    object_ = None

    def __init__(self, value=None, parent=None, indent=0):
        self.children = []
        self.parent = parent
        self.indent = indent

        if value is not None:
            self.value = value.strip()
                
        Node._last_added = self
    
    def add_child(self, value, indent):
        child = Node(value=value, parent=self, indent=0)
        self.children.append(child)
        
        return child
    
    def __str__(self):
        return '<Node(%s)>' % self.value
        return '<Node(%s,%s,%s)' % (self.value, self.parent, self.indent)


class _BaseType(object):

    VERBOSE = ('name',)

    def __init__(self, data):
        assert isinstance(data, basestring)
        data = data.strip()
        self.setup(data)

    def _to_string(self):
        attrs = ['%s=%s' % (attr_name, getattr(self, attr_name)) for attr_name in self.VERBOSE]
        return '<%s(%s)>' % (self.__class__.__name__, ','.join(attrs))

    def __str__(self):
        return self._to_string()

    def __repr__(self):
        return self._to_string()


class State(_BaseType):
    """State."""

    STATES = {}

    def setup(self, data):
        self.name = data.split('.')[1]
        assert self.name not in State.STATES
        State.STATES[self.name] = self


class StateVariable(_BaseType):
    """State variable."""
    
    VERBOSE = ('name', 'type_')

    def setup(self, data):
        self.name = data.split(':')[0].split()[-1]
        self.type_ = _VariableType.create(data.split(':')[1])


class _VariableType(_BaseType):

    VERBOSE = ('value',)

    value = None

    @property
    def combinations(self):
        raise NotImplementedError

    @classmethod
    def create(self, data):
        data = data.strip()
        print 'VariableType --> [%s]' % data

        return Bool()


class Bool(_VariableType):
    """Boolean variable."""

    def __init__(self, value=False):
        self.value = value


class Integer(_VariableType):
    """Integer variable."""

    def __init__(self, value=0):
        self.value = value


class String(_VariableType):
    """String variable."""

    def __init__(self, value=""):
        self.value = value


IDENTIFIER = r'[a-zA-Z][a-zA-Z0-9_]*'

PATTERNS = {
    r'^state\.[a-zA-Z][a-zA-Z0-9_-]*$': State,
    r'^var\s+[a-zA-Z][a-zA-Z0-9_]*\s*:\s*[a-z]+$': StateVariable,
    r'^assert\s+[a-zA-Z._]+\s*%(OPERATOR)s\s*%(VALUE)s': object()
}

def get_object(data):
    if not isinstance(data, basestring):
        return None

    for pattern, cls in PATTERNS.items():
        if re.match(pattern, data):
            return cls(data)
    return None

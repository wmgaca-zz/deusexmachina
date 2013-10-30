import copy

__author__ = 'wmgaca'


class Context(object):

    data = {
        'user': object(),
        'register': object(),
        'registered': object(),
        'place_an_ad': object(),
        'enter_details': object()
    }

    def get(self, name):
        return self.data[name]

    def get_copy(self):
        return copy.deepcopy(self)


class Node(object):

    context = None
    node_object = None

    def __init__(self, node_object, context):
        self.node_object = node_object
        self.context = context

    def process(self):
        pass


nodes = [Node(Context.get('register'), Context.get_copy()),
         Node(Context.get('registered'), Context.get_copy())]

while len(nodes):




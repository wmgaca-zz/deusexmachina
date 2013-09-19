from lib.walk import bfs
from lib import types


def _build_node(node):

    node.object_ = types.get_object(node.value)
    
    if node.object_ is not None:
        print '+ Build %s -> %s' % (node, node.object_)
    else:
        print '- Build %s' % node

def build(root):
    """Build TheArt objects from nodes.

    :param root Root node.
    :type root lib.types.Node
    """

    bfs(root, _build_node)

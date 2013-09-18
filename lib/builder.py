from lib.walk import bfs


def _build_node(node):
    print 'Build %s' % node


def build(root):
    """Build TheArt objects from nodes.

    :param root Root node.
    :type root lib.types.Node
    """

    bfs(root, _build_node)

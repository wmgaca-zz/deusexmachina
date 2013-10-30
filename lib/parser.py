import re
from lib import Node


def _line_empty(line):
    return not line.strip()


def _get_indent(line):
    return len(line) - len(line.lstrip())


def parse(fpath):
    """Parse the data and return the root node.
    
    :param fpath: Path to the scenario file
    :type fpath: basestring

    :return Root element of the parse tree.
    :rtype lib.types.Node
    """

    try:
        with open(fpath) as f:
            lines = f.readlines()
    except IOError:
        print 'Cannot open %s' % fpath
        exit()

    root = Node('root', None, 0)
    parent = root

    for line in lines:
        line = line.rstrip()

        if _line_empty(line):
            continue

        indent = _get_indent(line)

        if indent == parent.indent:
            if parent is root:
                root.add_child(line, indent)
        if indent == previous.indent:
            previous.parent.add_child(line, indent)
        if indent > previous.indent:
            previous.add_child(line, indent)

        print '%s%s%s' % (line, (40 - len(line)) * ' ', indent if indent else "")

    for child in root.children:
        print child

    return root

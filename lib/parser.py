import re
from lib import quit, Node

def _line_empty(line):
    return re.match(r'^\s+$', line)


def _get_indent(line):
    return len(line) - len(line.lstrip())


def parse(fpath):
    """Parse the data and return the root node.
    
    :param fpath: Path to the scenario file
    :type fpath: basestring

    :return Root element of the parse tree.
    :rtype lib.types.Node
    """

    with open(fpath) as f:
        lines = f.readlines()

    prev_indent = 0
    root = Node()
    current = root
    
    for line in lines:
        if _line_empty(line):
            continue

        indent = _get_indent(line)

        if indent == prev_indent:
            current.add_child(line)
        elif indent > prev_indent:
            current = current.children[-1]
            current.add_child(line)
        elif indent < prev_indent:
            current = current.parent
            current.add_child(line)

        prev_indent = indent

        print '>', line.rstrip(), _get_indent(line), Node.LAST_ADDED.parent

    for child in root.children:
        print child

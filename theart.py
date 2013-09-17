#!/usr/bin/env python

import sys
import re

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
        
def empty_line(line):
    return re.match(r'^\s+$', line)


def get_indent(line):
    return len(line) - len(line.lstrip())


def main(fpath):
    data = open(fpath).readlines()

    prev_indent = 0
    root = Node()
    current = root
    
    for line in data:
        if empty_line(line):
            continue

        indent = get_indent(line)

        if indent == prev_indent:
            current.add_child(line)
        elif indent > prev_indent:
            current = current.children[-1]
            current.add_child(line)
        elif indent < prev_indent:
            current = current.parent
            current.add_child(line)

        prev_indent = indent

        print '>', line.rstrip(), get_indent(line), Node.LAST_ADDED.parent

    for child in root.children:
        print child

if __name__ == '__main__':
    main(sys.argv[1])

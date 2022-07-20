import logging
import sys


class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.v:
            return node
        elif (val < node.v and node.l is not None):
            return self._find(val, node.l)
        elif (val > node.v and node.r is not None):
            return self._find(val, node.r)

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)


# Iterative method to find height of Binary Tree
def treeHeight(root):
    # Base Case
    if root is None:
        return 0

    # Create a empty queue for level order traversal
    q = []

    # Enqueue Root and Initialize Height
    q.append(root)
    height = 0

    while (True):

        # nodeCount(queue size) indicates number of nodes
        # at current level
        nodeCount = len(q)
        if nodeCount == 0:
            return height

        height += 1

        # Dequeue all nodes of current level and Enqueue
        # all nodes of next level
        while (nodeCount > 0):
            node = q[0]
            q.pop(0)
            if node.l is not None:
                q.append(node.l)
            if node.r is not None:
                q.append(node.r)

            nodeCount -= 1

logging.basicConfig(stream=sys.stderr, level=logging.CRITICAL)  # DEBUG, CRITICAL

with open('input_f1.txt', 'r') as f:
    lines = f.readlines()
f.close()
n = 0
a_list = []

for k in range(len(lines)):
    # logging.info(lines[k].strip("\n"))
    workstr = lines[k].strip()
    if k == 0:
        nstr = workstr.strip("\n")
        n = int(nstr)
        logging.info("n = {}".format(n))
    if k == 1:
        astr_list = workstr.strip("\n").split(" ", int(n))
        a_list = list(map(int, astr_list))
        logging.info("a_list = {}".format(a_list))

tree = Tree()
for e in a_list:
    tree.add(e)
# tree.printTree()
print(treeHeight(tree.getRoot()))
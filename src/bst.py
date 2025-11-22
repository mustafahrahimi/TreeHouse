#!/usr/bin/env python3

import bt
import sys
import logging

log = logging.getLogger(__name__)

class BST(bt.BT):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a root with the
        specified `value` and two empty children.
        '''
        self.set_value(value)
        if not self.is_empty():
            self.cons(BST(), BST())

    def is_member(self, v):
        '''
        Returns true if the value `v` is a member of the tree.
        '''
        if self.is_empty():
            return False
        if v == self.get_value():
            return True
        elif v < self.get_value():
            return self.get_lc().is_member(v)
        elif v > self.get_value():
            return self.get_rc().is_member(v)
        return False
    
    def size(self):
        '''
        Returns the number of nodes in the tree.
        '''
        if self.is_empty():
            return 0
        left_size = self.get_lc().size() 
        right_size = self.get_rc().size()
        return 1 + left_size + right_size

    def height(self):
        '''
        Returns the height of the tree.
        '''
        if self.is_empty():
            return 0
        left_height = self.get_lc().height()
        right_height = self.get_rc().height()
        return max(left_height, right_height) + 1
        
    def preorder(self):
        '''                                 
        Returns a list of all members in preorder.
        '''
        if self.is_empty():
            return []
        return [self.get_value()] + self.get_lc().preorder() + self.get_rc().preorder()

    def inorder(self):
        '''
        Returns a list of all members in inorder.
        '''
        if self.is_empty():
            return []
        return self.get_lc().inorder() + [self.get_value()] + self.get_rc().inorder()

    def postorder(self):
        '''
        Returns a list of all members in postorder.
        '''
        if self.is_empty():
            return []
        return self.get_lc().postorder() + self.get_rc().postorder() + [self.get_value()]

# ---------------------------------------------------------------------------------------
    def _bfs(self, array, i):
        factor = 2
        if not self.is_empty():
            array[i - 1] = self.get_value()
            self.get_lc()._bfs(array, factor * i)
            self.get_rc()._bfs(array, factor * i + 1)

    def bfs_order_star(self):
        '''
        Returns a list of all members in breadth-first search* order, which
        means that empty nodes are denoted by "stars" (here the value None).

        For example, consider the following tree `t`:
                    10
              5           15
           *     *     *     20

        The output of t.bfs_order_star() should be:
        [ 10, 5, 15, None, None, None, 20 ]
        '''
        size = pow(2, self.height()) - 1
        nodes = [None] * size
        self._bfs(nodes, 1)
        return nodes
    
# ---------------------------------------------------------------------------------------
    def add(self, v):
        '''
        Adds the value `v` and returns the new (updated) tree.  If `v` is
        already a member, the same tree is returned without any modification.
        '''
        if self.is_empty():
            self.__init__(value=v)
            return self
        if v < self.get_value():
            return self.cons(self.get_lc().add(v), self.get_rc())
        if v > self.get_value():
            return self.cons(self.get_lc(), self.get_rc().add(v))
        return self
    
# ---------------------------------------------------------------------------------------
    def right_subtree_smallest(self):
        if not self.get_lc().is_empty():
            return self.get_lc().right_subtree_smallest()
        return self.get_value()
    
    def left_subtree_largest(self):
        if not self.get_rc().is_empty():
            return self.get_rc().left_subtree_largest()
        return self.get_value()

    def remove_with_twoChildren(self):
        left_height = self.get_lc().height()
        right_height = self.get_rc().height()
        
        if left_height < right_height:
            newroot = self.get_rc().right_subtree_smallest()
            self.set_value(newroot)
            self.set_rc(self.get_rc().delete(newroot))
        else:
            newroot = self.get_lc().left_subtree_largest()
            self.set_value(newroot)
            self.set_lc(self.get_lc().delete(newroot))
        return self

    def remove_root(self):
        if self.get_lc().is_empty():
            return self.get_rc()
        if self.get_rc().is_empty():
            return self.get_lc()
        return self.remove_with_twoChildren()

    def delete(self, v):
        '''
        Removes the value `v` from the tree and returns the new (updated) tree.
        If `v` is a non-member, the same tree is returned without modification.
        '''
        if not self.is_member(v):
            return self
        if v < self.get_value():
            return self.cons(self.get_lc().delete(v), self.get_rc())
        if v > self.get_value():
            return self.cons(self.get_lc(), self.get_rc().delete(v))
        return self.remove_root()

if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)

'''
Magic nums?
Diff for testing?
'''

#!/usr/bin/env python3

import sys
import bst
import logging

log = logging.getLogger(__name__)

class AVL(bst.BST):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a root with the
        specified `value` and two empty children.
        '''
        self.set_value(value)
        if not self.is_empty():
            self.cons(AVL(), AVL())

    def add(self, v):
        '''
        Example which shows how to override and call parent methods. You
        may remove this function and overide something else if you'd like.
        '''
        super().add(v)
        return self.balance()
    
    def delete(self, v):
        deletion = super().delete(v)
        return deletion.balance()

# ---------------------------------------------------------------------------------------
    def balance_factor(self):
        return self.get_lc().height() - self.get_rc().height()
        
    def balance(self):
        '''
        AVL-balances around the node rooted at `self`. In other words, this
        method applies one of the following if necessary: slr, srr, dlr, drr.
        '''
        if self.is_empty():
            return self
        
        # Right heavy
        if self.balance_factor() <= -2:
            if self.get_rc().balance_factor() >= 1:
                return self.dlr()
            return self.slr()
        
        # Left heavy
        if self.balance_factor() >= 2:
            if self.get_lc().balance_factor() <= -1:
                return self.drr()
            return self.srr()
    
        return self

# ---------------------------------------------------------------------------------------
    def slr(self):
        '''
        Performs a single-left rotate around the node rooted at `self`.
        '''
        newroot = self.get_rc()
        self.set_rc(newroot.get_lc())
        newroot.set_lc(self)
        return newroot

    def srr(self):
        '''
        Performs a single-right rotate around the node rooted at `self`.
        '''
        newroot = self.get_lc()
        self.set_lc(newroot.get_rc())
        newroot.set_rc(self)
        return newroot
        
    def dlr(self):
        '''
        Performs a double-left rotate around the node rooted at `self`.
        '''
        self.set_rc(self.get_rc().srr())
        return self.slr()

    def drr(self):
        '''
        Performs a double-right rotate around the node rooted at `self`.
        '''
        self.set_lc(self.get_lc().slr())
        return self.srr()

if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
 
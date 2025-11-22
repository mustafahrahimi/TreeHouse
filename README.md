# Binary Search Tree & AVL Tree Implementation

A Python implementation of Binary Search Trees (BST) and AVL Trees with a terminal-based user interface for interactive tree operations and visualization.

## 🌳 Project Overview

This project implements two fundamental tree data structures:
- **Binary Search Tree (BST)**: A basic binary tree with search, insertion, and deletion operations
- **AVL Tree**: A self-balancing binary search tree that maintains height balance through rotations

## 🚀 Features

### Tree Operations
- **Add values**: Insert new nodes while maintaining tree properties
- **Delete values**: Remove nodes with proper tree restructuring
- **Search**: Check membership of values in the tree
- **Tree traversals**: Inorder, preorder, postorder, and breadth-first search
- **Tree metrics**: Calculate size and height
- **Visual display**: 2D tree visualization in terminal

### AVL-Specific Features
- **Automatic balancing**: Self-balancing through rotations
- **Single rotations**: Left and right rotations
- **Double rotations**: Left-right and right-left rotations
- **Balance factor calculation**: Monitors tree balance

## 🖥️ Usage

### Command Line Interface

```bash
$ ./bin/main --help
usage: Terminal-based UI for BST/AVL trees [-h] [--log-level LOG_LEVEL]
                                           [--mode MODE] [--echo]

optional arguments:
  -h, --help            show this help message and exit
  --log-level LOG_LEVEL, -l LOG_LEVEL
                        Minimum verbosity for logging. Available in ascending
                        order: debug, info, warning, error, crirical.
  --mode MODE, -m MODE  Tree mode. Available options: bst, avl.
  --echo, -e            Echo input. Useful if redirecting input from file
```

### Running the Application

**Interactive Mode:**
```bash
# Run in BST mode (default)
./bin/main

# Run in AVL mode
./bin/main -m avl
```

**Batch Mode with Input Files:**
```bash
# Run BST with input file
./bin/main -m bst -e < bst_input.txt

# Run AVL with input file
./bin/main -m avl -e < avl_input.txt
```

**Debug Mode:**
```bash
# Show all logging statements
./bin/main -l debug

# Show info and above
./bin/main -l info

# Show only warnings, errors, and critical messages
./bin/main -l warning
```

### Interactive Menu

Once the program starts, you'll see a menu with the following options:

```
********************************
    m: menu
    t: display tree
    
    a: add value
    d: delete value
    f: test membership
    
    q: quit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

**Menu Commands:**
- `m` - Display the menu again
- `t` - Show tree structure, size, height, and traversals
- `a` - Add a value to the tree
- `d` - Delete a value from the tree
- `f` - Test if a value exists in the tree
- `q` - Quit the program

## 🔧 Implementation Details

### Binary Tree (bt.py)
Base class providing:
- Node structure with value and left/right children
- Basic tree operations (constructors, getters, setters)
- Empty tree checking

### Binary Search Tree (bst.py)
Extends Binary Tree with:
- **Search**: O(log n) average, O(n) worst case
- **Insertion**: O(log n) average, O(n) worst case
- **Deletion**: O(log n) average, O(n) worst case
- **Traversals**: Inorder (sorted), preorder, postorder, BFS
- **Tree metrics**: Size and height calculation

### AVL Tree (avl.py)
Extends BST with:
- **Automatic balancing**: Maintains height balance after operations
- **Rotations**: Single and double rotations to restore balance
- **Guaranteed performance**: O(log n) for all operations
- **Balance factor**: Tracks the height difference between subtrees

## 📊 Example Usage

### Sample Session
```
menu> a
Enter value to be added> 10
menu> a
Enter value to be added> 5
menu> a
Enter value to be added> 15
menu> t

        10
    5       15
  *   *   *   *

Size:      3
Height:    2
Inorder:   [5, 10, 15]
Preorder:  [10, 5, 15]
Postorder: [5, 15, 10]
BFS star:  [10, 5, 15, *, *, *, *]
```

## 🧪 Testing

The project includes test input files:
- `bst_input.txt` - Commands for testing BST functionality
- `avl_input.txt` - Commands for testing AVL functionality
- `bst.txt` - Expected output for BST tests
- `avl.txt` - Expected output for AVL tests

Run tests and compare output:
```bash
./bin/main -m bst -e < bst_input.txt > my_bst_output.txt
diff --color bst.txt my_bst_output.txt

./bin/main -m avl -e < avl_input.txt > my_avl_output.txt
diff --color avl.txt my_avl_output.txt
```

## 🔍 Debugging

The project uses Python's logging module for debugging:
- `log.debug()` - Detailed debugging information
- `log.info()` - General information about program flow
- `log.warning()` - Warning messages
- `log.error()` - Error conditions
- `log.critical()` - Critical errors

Use the `-l` flag to control logging verbosity during development and testing.

## 📚 Educational Value

This implementation demonstrates:
- **Object-oriented programming**: Class inheritance and method overriding
- **Data structures**: Binary trees, search trees, and self-balancing trees
- **Algorithms**: Tree traversals, rotations, and balancing
- **Software design**: Modular architecture and separation of concerns
- **Testing**: Automated testing with input/output comparison

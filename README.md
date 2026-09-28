# LeetCode 314 - Binary Tree Vertical Order Traversal

## Problem Statement

Given the root of a binary tree, return the **vertical order traversal** of its nodes' values.

Nodes are grouped by their vertical column from left to right. Within the same column, nodes are returned from top to bottom.

## Example 1

### Input

```text
root = [3,9,20,null,null,15,7]
```

### Output

```text
[[9],[3,15],[20],[7]]
```

## Example 2

### Input

```text
root = [3,9,8,4,0,1,7]
```

### Output

```text
[[4],[9],[3,0,1],[8],[7]]
```

## Approach

Use **Breadth-First Search (BFS)** and assign a column number to every node.

The root is placed at column `0`. The left child moves to `column - 1`, and the right child moves to `column + 1`.

A dictionary stores the nodes belonging to each column.

## Algorithm

1. If the tree is empty, return an empty list.
2. Use a queue to perform BFS.
3. Store each node together with its column number.
4. Add the node value to the corresponding column.
5. Add the left child with `column - 1`.
6. Add the right child with `column + 1`.
7. Sort the column numbers from left to right.
8. Return the values stored in each column.

## Time Complexity

`O(n log n)`

## Space Complexity

`O(n)`

## Key Concepts

* Binary Tree
* BFS
* Queue
* Hash Map
* Column Indexing
* Tree Traversal

## Language

Python

## LeetCode Details

* **Problem:** 314
* **Title:** Binary Tree Vertical Order Traversal
* **Difficulty:** Medium

## Author

**T. Nandhini Reddy**

GitHub: `242t605119-dotcom`

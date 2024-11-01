from __future__ import annotations

from typing import List, Tuple, TypeVar

from data_structures.bst import BinarySearchTree
from algorithms.mergesort import mergesort
from data_structures.node import TreeNode

K = TypeVar('K')
I = TypeVar('I')


class BetterBST(BinarySearchTree[K, I]):
    def __init__(self, elements: List[Tuple[K, I]]) -> None:
        """
        Initialiser for the BetterBST class.
        We assume that the all the elements that will be inserted
        into the tree are contained within the elements list.

        As such you can assume the length of elements to be non-zero.
        The elements list will contain tuples of key, item pairs.

        First sort the elements list and then build a balanced tree from the sorted elements
        using the corresponding methods below.

        Args:
            elements(List[tuple[K, I]]): The elements to be inserted into the tree.

        Complexity:
            Best Case Complexity: O(nlogn), n is the number of elements in the list
            Worst Case Complexity: O(nlogn), n is the number of elements in the list
        """
        super().__init__()
        new_elements: List[Tuple[K, I]] = self.__sort_elements(elements)
        self.__build_balanced_tree(new_elements)

    def __sort_elements(self, elements: List[Tuple[K, I]]) -> List[Tuple[K, I]]:
        """
        Recall one of the drawbacks to using a binary search tree is that it can become unbalanced.
        If we know the elements ahead of time, we can sort them and then build a balanced tree.
        This will help us maintain the O(log n) complexity for searching, inserting, and deleting elements.

        Args:
            elements (List[Tuple[K, I]]): The elements we wish to sort.

        Returns:
            list(Tuple[K, I]]) - elements after being sorted.

        Complexity:
            Best Case Complexity: O(nlogn), n is the number of elements in the list
            Worst Case Complexity: O(nlogn), n is the number of elements in the list
        """
        
        sorted_elements = mergesort(elements, lambda x: elements[0])
        return sorted_elements

    def __build_balanced_tree(self, elements: List[Tuple[K, I]]) -> None:
        """
        This method will build a balanced binary search tree from the sorted elements.

        Args:
            elements (List[Tuple[K, I]]): The elements we wish to use to build our balanced tree.

        Returns:
            None

        Complexity:
            (This is the actual complexity of your code, 
            remember to define all variables used.)
            Best Case Complexity: O(nlogn), n is the number of elements in the list
            Worst Case Complexity: O(nlogn), n is the number of elements in the list

        Justification:
            - The method constructs a balanced binary search tree by recursively dividing 
            the list of elements into two halves at each level of recursion 
            - Each level processes all elements, contributing to a linear time cost per level
            - Since the depth of recursion is o(logn) due to the halving process 
            the overall complexity is o(nlogn) for both the best and worst cases, where n is the number of elements in the list.

        Complexity requirements for full marks:
            Best Case Complexity: O(n * log(n))
            Worst Case Complexity: O(n * log(n))
            where n is the number of elements in the list.
        """
        self.root = self.__build_balanced_tree_aux(elements, 1)

    def __build_balanced_tree_aux(self, elements: List[Tuple[K,I]], depth):
        if not elements:
            return None
        
        mid = len(elements) // 2
        key, item = elements[mid]
        node = TreeNode(key, item, depth)
        self.length += 1

        node.left = self.__build_balanced_tree_aux(elements[:mid], depth + 1)
        node.right = self.__build_balanced_tree_aux(elements[mid + 1:], depth + 1)

        return node
        
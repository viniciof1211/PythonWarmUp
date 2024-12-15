# PythonWarmUp

### General Usual + Some Unusual Algorithms in Python

This repository contains a collection of Python algorithms, implemented in the simplest and most concise manner, designed to help you **warm up** for coding challenges or interviews. These implementations span **common algorithms**, **problem-solving patterns**, and some **unique exercises**, all useful for solidifying your skills.

---

## **Challenges Overview**

### **1. Usual Python Challenges**
- **Palindrome Checker:** Determine if a string or number is a palindrome.
- **Anagram Checker:** Verify if two strings are anagrams.
- **Sorting Algorithms:** Implement Bubble Sort, Quick Sort, or Merge Sort.
- **Factorial Calculator:** Calculate factorials using recursive and iterative methods.
- **Find the Second Largest Number:** Identify the second largest number in a list.
- **Prime Number Generator:** Use the Sieve of Eratosthenes to generate primes.
- **Binary Search:** Perform binary search on a sorted list.
- **Two Sum Problem:** Find two numbers in a list that add up to a target.
- **Reverse a Linked List:** Reverse a singly linked list.
- **Harmony Sort:** Parallelized sorting algorithm that partitions an array into harmonic buckets, sorts them independently, and merges them harmoniously, achieving __𝑂(𝑛 log 𝑘)__ complexity when 𝑘 partitions are processed in parallel.

### **2. Unusual Python Coding Challenges**
- **Data Pipeline Simulation:** Simulate an ETL pipeline with basic transformations.
- **Custom Decorator:** Log the execution time of a function.
- **Custom Data Structure:** Implement structures like a Min-Heap, Trie, or LRU Cache.
- **File System Simulation:** Simulate a simple file system with commands like `mkdir`, `ls`, and `cd`.
- **Concurrency Challenge:** Use `asyncio` or threading to manage tasks concurrently.
- **Text Justification:** Justify a paragraph of text to a specific line width.
- **Sudoku Solver:** Solve Sudoku puzzles using backtracking.
- **Matrix Manipulation:** Perform matrix operations like transposition and rotation.
- **JSON to CSV Converter:** Convert JSON data to a CSV file.
- **URL Shortener:** Create a simple URL shortening service.
- **Stock Market Analyzer:** Analyze stock price trends from data.
- **Command-Line Calculator:** Build a CLI calculator for basic operations.
- **Log File Analyzer:** Parse log files for insights like frequent IPs or errors.
- **Image Manipulation:** Use the Pillow library for basic image transformations.
- **Regex-Based Parser:** Extract patterns like emails or phone numbers using regex.
- **Graph Traversal:** Implement DFS and BFS for a graph.
- **Snake Game:** Create a terminal-based Snake game using the `curses` library.
- **Blockchain Simulation:** Simulate a blockchain with basic functionalities.
- **Circular Buffer:** Implement a circular buffer for data handling.
- **Text Autocomplete:** Build a system to suggest completions for input prefixes.

---

## **Getting Started**

### **Prerequisites**
- Python 3.8 or above
- Basic knowledge of Python and common libraries (`time`, `heapq`, `asyncio`, `csv`, `json`, etc.)

### **Installation**
Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/yourusername/PythonWarmUp.git
cd PythonWarmUp
```

### **Usage**
- Run a Challenge
- Each challenge is implemented as an individual Python function or script. For example, to run the Palindrome Checker:

```python
from challenges.palindrome_checker import is_palindrome

print(is_palindrome("radar"))  # Output: True
print(is_palindrome(12321))   # Output: True
print(is_palindrome("python"))  # Output: False
```
#### For more examples and usage details, see the examples/ folder.
# Week 1 Coding Challenges

Leet coding challenge solutions provided using Jupyter Notebooks using (<b>Python3.7, Java 11, Go 1.14</b>).

## Single Number Challenge

Given an array with pairs of numbers, identify which number does not have a coresponding counterpart.

EXAMPLE:
```
Input: [3,3,2,2,1]
Output: 1
```

## Happy Number Challenge

Given a single integer, determine if the sum of it's digits squared, can ever equal 1.

EXAMPLE:
```java
Input: 19
Output: true
Logic: 19 -> [1, 9] -> (1^2)+(9^2)

Explanation:
(1^2) + (9^2) = 82
(8^2) + (2^2) = 68
(6^2) + (8^2) = 100
(1^2) + (0^2) + (0**2) = 1

Answer: 1
```

Becasue the sum of 100s digits squared equalled 1, `19`, the original number inputted, is considered happy.

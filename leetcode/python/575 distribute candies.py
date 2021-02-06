## 题目描述

```
给定一个偶数长度的数组，其中不同的数字代表着不同种类的糖果，每一个数字代表一个糖果。你需要把这些糖果平均分给一个弟弟和一个妹妹。返回妹妹可以获得的最大糖果的种类数。

示例 1:

输入: candies = [1,1,2,2,3,3]
输出: 3
解析: 一共有三种种类的糖果，每一种都有两个。
     最优分配方案：妹妹获得[1,2,3],弟弟也获得[1,2,3]。这样使妹妹获得糖果的种类数最多。
示例 2 :

输入: candies = [1,1,2,3]
输出: 2
解析: 妹妹获得糖果[2,3],弟弟获得糖果[1,1]，妹妹有两种不同的糖果，弟弟只有一种。这样使得妹妹可以获得的糖果种类数最多。
注意:

数组的长度为[2, 10,000]，并且确定为偶数。
数组中数字的大小在范围[-100,000, 100,000]内。

```

## 前置知识

- [数组](https://github.com/azl397985856/leetcode/blob/master/thinkings/basic-data-structure.md)


- 如果糖果种类大于n / 2（糖果种类数为n），妹妹最多可以获得的糖果种类应该是`n / 2`(因为妹妹只有n / 2个糖).
- 糖果种类数小于n / 2, 妹妹能够得到的糖果种类可以是糖果的种类数（糖果种类本身就这么多）.

因此我们发现，妹妹能够获得的糖果种类的制约因素其实是糖果种类数。

Python Code:

```python
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        return min(len(set(candies)), len(candies) >> 1)
```
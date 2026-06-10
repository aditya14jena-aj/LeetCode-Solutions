# 1. Two Sum

## My First Attempt (With a Mistake)

My first idea was to check every possible pair using two nested loops.

```python
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

### Mistake I Found

The problem is that `i` and `j` can be the same index.

Example:

```python
nums = [3, 2, 4]
target = 6
```

When:

```python
i = 0
j = 0
```

The calculation becomes:

```python
nums[0] + nums[0]
= 3 + 3
= 6
```

The code returns:

```python
[0, 0]
```

However, the problem states that we cannot use the same element twice.

---

## Corrected Brute Force Solution

To fix this, I changed the inner loop.

Instead of:

```python
for j in range(len(nums)):
```

I used:

```python
for j in range(i + 1, len(nums)):
```

### Correct Code

```python
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

### What Changed?

* We never compare an element with itself.
* We avoid checking duplicate pairs.
* The solution now works correctly.

### Complexity

* Time Complexity: `O(n²)`
* Space Complexity: `O(1)`

---

## Better Optimized Solution (Hash Map)

After solving the problem using brute force, I noticed that checking every pair takes quadratic time.

I realized that if I already know a number I've seen before, I can immediately check whether its complement exists.

### Idea

For each number:

```python
diff = target - current_number
```

If `diff` has already been seen, then I've found the answer.

### Code

```python
class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in seen:
                return [seen[diff], i]

            seen[nums[i]] = i
```

---

## Dry Run

Example:

```python
nums = [2, 7, 11, 15]
target = 9
```

### Iteration 1

```python
i = 0
num = 2
diff = 7
```

`7` is not in `seen`.

```python
seen = {2: 0}
```

### Iteration 2

```python
i = 1
num = 7
diff = 2
```

`2` is already in `seen`.

Therefore:

```python
return [0, 1]
```

---

## Complexity Analysis

### Time Complexity

`O(n)`

Each element is processed once.

### Space Complexity

`O(n)`

The hash map may store up to `n` elements.

---

## Lessons Learned

* Always check whether the same index can be used accidentally.
* Brute force solutions are useful for understanding the problem.
* Hash maps can often reduce nested loop problems from `O(n²)` to `O(n)`.
* Thinking in terms of complements (`target - current_number`) leads to a much more efficient solution.

```
```

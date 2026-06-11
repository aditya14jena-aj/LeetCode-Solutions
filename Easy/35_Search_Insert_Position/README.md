# 35. Search Insert Position

## My First Attempt (With a Mistake)

My initial idea was to check whether the target already existed in the array.

If it did, I would simply return its index.

```python
class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
```

If the target was not present, I tried to determine its insertion position by checking nearby values.

```python
class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            if (target - 1) in nums:
                return nums.index(target) + 1
            else:
                return nums.index(target) - 1
```

---

## Mistake I Found

The biggest issue was this line:

```python
nums.index(target)
```

The code enters the `else` block only when:

```python
target not in nums
```

Therefore calling:

```python
nums.index(target)
```

immediately causes an error because the target does not exist in the list.

### Example

```python
nums = [1, 3, 5, 6]
target = 2
```

Since `2` is not in the list:

```python
target in nums
```

returns:

```python
False
```

The code enters the `else` block and tries:

```python
nums.index(2)
```

which raises an exception.

---

## Another Problem

Even if the code did not crash, checking only:

```python
target - 1
```

or

```python
target + 1
```

is not reliable.

Example:

```python
nums = [1, 3, 5, 6]
target = 4
```

The correct insertion position is:

```python
2
```

because:

```python
[1, 3, 4, 5, 6]
```

maintains sorted order.

Trying to guess the position based on neighboring values becomes complicated and fails for larger gaps.

---

## Better Approach: Binary Search

The problem requires an efficient solution.

Since the array is already sorted, Binary Search is a perfect fit.

Instead of checking every element, we repeatedly cut the search space in half.

### Idea

Maintain two pointers:

```python
left = 0
right = len(nums) - 1
```

Calculate:

```python
mid = (left + right) // 2
```

Then:

* If `nums[mid] == target`, return `mid`.
* If `nums[mid] < target`, search the right half.
* If `nums[mid] > target`, search the left half.

If the target is not found, the `left` pointer will end up exactly where the target should be inserted.

---

## Final Solution

```python
class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return left
```

---

## Dry Run

Example:

```python
nums = [1, 3, 5, 6]
target = 2
```

### Iteration 1

```python
left = 0
right = 3
mid = 1
```

```python
nums[mid] = 3
```

Since:

```python
3 > 2
```

move left:

```python
right = mid - 1
right = 0
```

### Iteration 2

```python
left = 0
right = 0
mid = 0
```

```python
nums[mid] = 1
```

Since:

```python
1 < 2
```

move right:

```python
left = mid + 1
left = 1
```

The loop ends.

Return:

```python
left
```

which is:

```python
1
```

Correct answer.

---

## Why This Works

The key observation is that after Binary Search finishes:

* Every index before `left` contains values smaller than the target.
* Every index after `left` contains values greater than the target.

Therefore `left` is exactly the position where the target should be inserted.

---

## Complexity Analysis

### Time Complexity

`O(log n)`

Binary Search halves the search space in every iteration.

### Space Complexity

`O(1)`

Only a few variables are used regardless of input size.

---

## Lessons Learned

* Never call `.index()` on a value that may not exist.
* Trying to infer insertion positions manually becomes messy.
* When a sorted array and `O(log n)` complexity are mentioned, Binary Search is usually the right tool.
* A useful Binary Search trick is that the final value of `left` often represents the insertion position when the target is not found.

```
```
#Time Taken 
*00:11:45

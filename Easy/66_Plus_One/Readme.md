# 66. Plus One

## My First Attempt

At first, I thought the problem was much simpler than it actually was.

My idea was:

* If the last digit is less than `9`, simply add `1`.
* If the last digit is `9`, change it and append a new digit.

Something like:

```python
if digits[len(digits) - 1] < 9:
    digits[len(digits) - 1] += 1
else:
    digits[len(digits) - 1] = 1
    digits.append(0)
```

It seemed reasonable at first.

Until I tried a few test cases.

---

## The Problem

Consider:

```python
digits = [1, 9]
```

Adding one should give:

```python
[2, 0]
```

But my approach produced:

```python
[1, 1, 0]
```

which is completely wrong.

Then I started adding more conditions.

---

## My Overengineering Phase 😭

I even wrote a helper function:

```python
def all_elements_same(arr):
    if not arr:
        return True
    return all(x == arr[0] for x in arr)
```

The idea was to detect cases like:

```python
[9]
[9,9]
[9,9,9]
```

and handle them separately.

Then I added more conditions:

```python
elif self.all_elements_same(digits):
```

and more special cases.

And somehow a problem called **"Plus One"** was turning into **"Plus Twenty Conditions"** 😂.

The more cases I added, the more edge cases appeared.

---

## The Realization

Instead of treating every situation separately, I realized I should think about how addition actually works.

When adding one:

* Start from the last digit.
* If the digit is less than `9`, increase it and stop.
* If the digit is `9`, it becomes `0` and carries over to the previous digit.
* Continue moving left until no carry remains.

This is exactly how we do addition on paper.

---

## Better Approach

Traverse the array from right to left.

### Case 1

If:

```python
digits[i] < 9
```

simply:

```python
digits[i] += 1
```

and return.

### Case 2

If:

```python
digits[i] == 9
```

then:

```python
digits[i] = 0
```

and continue carrying.

### Final Case

If every digit was `9`:

```python
[9]
[9,9]
[9,9,9]
```

the loop turns everything into:

```python
[0]
[0,0]
[0,0,0]
```

and we simply place a `1` in front.

---

## Final Solution

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):

            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        return [1] + digits
```

---

## Dry Run

Example:

```python
digits = [1, 2, 9]
```

Start from the end:

```python
9 -> 0
```

Array becomes:

```python
[1, 2, 0]
```

Move left:

```python
2 -> 3
```

Array becomes:

```python
[1, 3, 0]
```

Return:

```python
[1, 3, 0]
```

Correct.

---

### Another Example

```python
digits = [9, 9, 9]
```

Step 1:

```python
[9, 9, 0]
```

Step 2:

```python
[9, 0, 0]
```

Step 3:

```python
[0, 0, 0]
```

Loop finishes.

Return:

```python
[1] + [0,0,0]
```

Result:

```python
[1,0,0,0]
```

Correct.

---

## Complexity Analysis

### Time Complexity

`O(n)`

In the worst case we traverse all digits once.

### Space Complexity

`O(1)`

Ignoring the output array, we only use a few variables.

---

## Lessons Learned

* When a problem involves digits, think about how arithmetic is performed manually.
* Adding more conditions is not always the answer.
* If you find yourself creating helper functions for a problem called **"Plus One"**, it may be time to rethink the approach 😂.
* Carry propagation is the key observation in this problem.

```
```

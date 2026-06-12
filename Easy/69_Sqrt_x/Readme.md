# 69. Sqrt(x)

## My First Thought

When I first saw the problem, my immediate idea was:

> Keep checking numbers starting from 1 until I find a number whose square is greater than `x`.

Something like:

```python
i = 1

while i * i <= x:
    i += 1

return i - 1
```

This works, but it isn't very efficient.

For small numbers it's fine.

For very large numbers, we're checking far too many values.

---

## The Hint Was Hidden in the Constraints

The moment I noticed that the input can be very large, I started thinking:

> "Do I really need to check every number?"

The answer is no.

The numbers are naturally ordered:

```text
1² < 2² < 3² < 4² < ...
```

That means Binary Search can be used.

---

## Key Observation

Suppose:

```python
mid = 10
```

Then:

```python
mid * mid = 100
```

Three situations can occur:

### Case 1

```python
mid * mid == x
```

Perfect square found.

Return `mid`.

---

### Case 2

```python
mid * mid < x
```

The answer is either:

```python
mid
```

or somewhere to the right.

Move:

```python
left = mid + 1
```

---

### Case 3

```python
mid * mid > x
```

The answer must be smaller.

Move:

```python
right = mid - 1
```

---

## The Tricky Part

The problem doesn't ask for the exact square root.

It asks for:

```text
⌊ √x ⌋
```

which means:

```text
Return the integer part only.
```

Example:

```python
x = 8
```

Actual square root:

```text
2.828...
```

Answer:

```text
2
```

Because we only keep the integer portion.

---

## How I Handled This

Whenever:

```python
mid * mid < x
```

I know that `mid` is currently a valid answer.

So I store it:

```python
ans = mid
```

Then continue searching to see whether a larger valid answer exists.

This guarantees that if an exact square root doesn't exist, I still return the closest smaller integer.

---

## Dry Run

Example:

```python
x = 8
```

Initial:

```python
left = 1
right = 8
```

---

### Iteration 1

```python
mid = 4
```

```python
4 * 4 = 16
```

Too large.

```python
right = 3
```

---

### Iteration 2

```python
mid = 2
```

```python
2 * 2 = 4
```

Valid answer.

```python
ans = 2
left = 3
```

---

### Iteration 3

```python
mid = 3
```

```python
3 * 3 = 9
```

Too large.

```python
right = 2
```

Loop ends.

Return:

```python
ans = 2
```

Correct.

---

## Final Solution

```python
class Solution:
    def mySqrt(self, x: int):

        if x < 2:
            return x

        left, right = 1, x
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid

            elif square < x:
                ans = mid
                left = mid + 1

            else:
                right = mid - 1

        return ans
```

---

## Why This Works

Binary Search continuously eliminates half of the remaining search space.

Instead of checking:

```text
1, 2, 3, 4, 5, ...
```

one by one,

we jump directly to the middle and decide which half can be discarded.

This reduces the number of operations dramatically.

---

## Complexity Analysis

### Time Complexity

`O(log x)`

Each iteration cuts the search range in half.

---

### Space Complexity

`O(1)`

Only a few variables are used.

---

## Lessons Learned

* If values are ordered, Binary Search is often a good candidate.
* The problem wasn't really asking for the square root; it was asking for the largest integer whose square is less than or equal to `x`.
* Keeping track of the last valid answer (`ans`) is a useful Binary Search pattern.
* A brute-force solution may work, but Binary Search turns a potentially huge search into just a handful of operations.

```
```

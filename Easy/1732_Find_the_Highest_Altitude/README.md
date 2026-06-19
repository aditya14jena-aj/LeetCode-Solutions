# 1732. Find the Highest Altitude

## My First Thought

When I read the problem, I imagined myself tracking a cyclist's journey.

The cyclist starts at altitude:

```text
0
```

and each value in `gain` tells us how much the altitude changes compared to the previous point.

For example:

```python
gain = [-5, 1, 5, 0, -7]
```

means:

```text
Start: 0

0 + (-5) = -5
-5 + 1 = -4
-4 + 5 = 1
1 + 0 = 1
1 + (-7) = -6
```

The altitudes become:

```text
[0, -5, -4, 1, 1, -6]
```

The answer is simply:

```text
1
```

because it is the highest altitude reached.

---

## Approach

I decided to explicitly build all altitudes.

First, create an array containing the starting altitude:

```python
arr = [0]
```

Then for every gain value:

```python
new_altitude = previous_altitude + gain
```

and append it to the array.

After processing all gains, return:

```python
max(arr)
```

which represents the highest altitude reached during the trip.

---

## Dry Run

Example:

```python
gain = [-5, 1, 5, 0, -7]
```

Initial:

```python
arr = [0]
```

Process `-5`:

```python
arr = [0, -5]
```

Process `1`:

```python
arr = [0, -5, -4]
```

Process `5`:

```python
arr = [0, -5, -4, 1]
```

Process `0`:

```python
arr = [0, -5, -4, 1, 1]
```

Process `-7`:

```python
arr = [0, -5, -4, 1, 1, -6]
```

Highest altitude:

```python
max(arr) = 1
```

Answer:

```python
1
```

---

## Final Solution

```python
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arr = [0]

        for a in gain:
            arr.append(arr[-1] + a)

        return max(arr)
```

---

## Why This Works

The problem gives altitude changes, not actual altitudes.

By continuously adding each gain to the previous altitude, we reconstruct every altitude reached during the trip.

Once all altitudes are known, finding the highest one is simply:

```python
max(arr)
```

---

## Complexity Analysis

### Time Complexity

`O(n)`

We iterate through the gain array once.

### Space Complexity

`O(n)`

We store all altitudes in the array.

---

## Possible Optimization

While solving, I realized that we don't actually need to store every altitude.

We only need:

- Current altitude
- Highest altitude seen so far

This reduces the space complexity to:

```text
O(1)
```

Optimized version:

```python
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        highest = 0

        for g in gain:
            current += g
            highest = max(highest, current)

        return highest
```

---

## Lessons Learned

- The gain array does not represent altitudes directly; it represents changes in altitude.
- Building a running sum is often the easiest way to reconstruct values from differences.
- Sometimes a solution can be simplified further by tracking only the information we actually need.
- This problem is a nice introduction to the concept of **prefix sums**.

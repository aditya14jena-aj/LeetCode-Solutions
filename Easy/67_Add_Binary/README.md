# 67. Add Binary

## First Thought

When I first saw this problem, my immediate thought was:

> "This is basically normal addition, except we're working with binary digits instead of decimal digits."

When we add numbers on paper, we start from the rightmost digit and move left while carrying any overflow to the next position.

Binary addition works exactly the same way.

The only difference is:

```text
0 + 0 = 0
0 + 1 = 1
1 + 1 = 10
1 + 1 + 1 = 11
```

which means the carry can only be `0` or `1`.

---

## Approach

I decided to simulate how manual addition works.

### Step 1

Start from the last characters of both strings.

```python
i = len(a) - 1
j = len(b) - 1
```

---

### Step 2

Maintain a carry value.

```python
carry = 0
```

---

### Step 3

While there are still digits left to process (or a carry remains):

```python
while i >= 0 or j >= 0 or carry:
```

add:

* current digit from `a`
* current digit from `b`
* current carry

into a variable called `total`.

---

### Step 4

The current binary digit is:

```python
total % 2
```

because:

```text
0 -> 0
1 -> 1
2 -> 0 (carry 1)
3 -> 1 (carry 1)
```

---

### Step 5

Update the carry:

```python
carry = total // 2
```

---

### Step 6

Since we are building the answer from right to left, store digits in a list and reverse them at the end.

---

## Dry Run

Example:

```python
a = "11"
b = "1"
```

### Iteration 1

```python
1 + 1 + carry(0)
```

```python
total = 2
```

Digit:

```python
2 % 2 = 0
```

Carry:

```python
2 // 2 = 1
```

Result:

```python
["0"]
```

---

### Iteration 2

```python
1 + carry(1)
```

```python
total = 2
```

Digit:

```python
0
```

Carry:

```python
1
```

Result:

```python
["0", "0"]
```

---

### Iteration 3

No digits remain, but carry still exists.

```python
total = 1
```

Digit:

```python
1
```

Carry:

```python
0
```

Result:

```python
["0", "0", "1"]
```

Reverse:

```python
"100"
```

Correct answer.

---

## Final Solution

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0

        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))

            carry = total // 2

        return "".join(reversed(result))
```

---

## Why This Works

The algorithm mimics the exact process used for handwritten addition.

At every step:

* We compute the current digit.
* We compute the carry for the next position.
* We continue until every digit and carry have been processed.

---

## Complexity Analysis

### Time Complexity

`O(max(n, m))`

where:

* `n = len(a)`
* `m = len(b)`

We process each binary digit exactly once.

### Space Complexity

`O(max(n, m))`

The result list stores the final binary number.

---

## Lessons Learned

* Many string problems become easier when treated as simulations.
* Binary addition follows the same principles as decimal addition.
* The carry is the most important part of the problem.
* Building the answer in reverse and reversing once at the end is often cleaner than inserting at the front of a list.
* Sometimes the best solution is simply translating a real-world process into code.

```
```

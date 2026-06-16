# 3612. Process String With Special Operations

## First Thought

When I read the problem, I noticed that every special character directly modifies the string that has already been built.

The operations were:

| Character | Operation |
|-----------|-----------|
| `*` | Remove the last character |
| `#` | Duplicate the current string |
| `%` | Reverse the current string |

This immediately suggested a simulation approach.

Instead of trying to predict the final string, I could simply process the characters one by one and apply the required operation whenever a special character appeared.

---

## Approach

Maintain a string called `result`.

For each character in the input:

### Normal Character

Append it to the current result.

```python
result += char
```

### `*`

Delete the last character.

```python
result = result[:-1]
```

### `#`

Duplicate the entire current string.

```python
result += result
```

### `%`

Reverse the current string.

```python
result = result[::-1]
```

After processing all characters, return the final string.

---

## Example

Input:

```python
s = "ab#c%"
```

### Step 1

```python
result = "a"
```

### Step 2

```python
result = "ab"
```

### Step 3 (`#`)

```python
result = "abab"
```

### Step 4

```python
result = "ababc"
```

### Step 5 (`%`)

```python
result = "cbaba"
```

Output:

```python
"cbaba"
```

---

## Why I Liked This Problem

At first glance it looked like a string manipulation problem with lots of possible cases.

But after breaking it down, every operation simply modifies the current state of the string.

Once I realized that, the solution became a straightforward simulation.

It's one of those problems where understanding the process is more important than finding a clever trick.

---

## Final Solution

```python
class Solution:
    def processStr(self, s: str) -> str:
        result = ""

        for i in s:
            if i == "*":
                result = result[:-1]

            elif i == "#":
                result += result

            elif i == "%":
                result = result[::-1]

            else:
                result += i

        return result
```

---

## Complexity Analysis

### Time Complexity

Worst Case: `O(n²)`

Operations like:

```python
result += result
```

and

```python
result[::-1]
```

can copy large portions of the string.

---

### Space Complexity

`O(n)`

The result string stores the processed output.

---

## Lessons Learned

- Simulation is often the cleanest solution for operation-based problems.
- Processing characters from left to right mirrors the problem statement exactly.
- Python slicing makes deletion and reversal extremely convenient.
- Sometimes the best solution is simply implementing the rules as written.

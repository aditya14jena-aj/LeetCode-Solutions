# 1189. Maximum Number of Balloons

## My First Thought

When I saw the problem, I immediately thought:

> "Let's count how many times I can build the word 'balloon'."

The word contains:

```text
b → 1
a → 1
l → 2
o → 2
n → 1
```

So my first idea was to count the required characters and repeatedly remove them until it was no longer possible to form another `"balloon"`.

---

## My First Attempt

I counted each required character:

```python
b = text.count("b")
a = text.count("a")
l = text.count("l")
o = text.count("o")
n = text.count("n")
```

Then I planned to repeatedly consume characters:

```python
while True:
    if b > 0 and a > 0 and l >= 2 and o >= 2 and n > 0:
        c += 1
        b -= 1
        a -= 1
        l -= 2
        o -= 2
        n -= 1
    else:
        return c
```

This works because every iteration creates exactly one `"balloon"`.

---

## The Realization

After staring at the counts for a while, I noticed something:

I don't actually need to simulate building each word.

The limiting factor is simply the character that runs out first.

For example:

```python
text = "loonbalxballpoon"
```

Character counts:

```text
b = 2
a = 2
l = 4
o = 4
n = 2
```

Since:

```text
"l" is needed twice
"o" is needed twice
```

their effective counts are:

```text
l = 4 // 2 = 2
o = 4 // 2 = 2
```

Now we compare:

```text
b = 2
a = 2
l = 2
o = 2
n = 2
```

The smallest value is:

```text
2
```

which means we can form `"balloon"` exactly 2 times.

🤯 No loop needed.

---

## Better Approach

Count each required letter.

Since:

```text
balloon
```

contains:

```text
l twice
o twice
```

adjust their counts:

```python
l // 2
o // 2
```

Then return the smallest available count.

```python
min(b, a, l // 2, o // 2, n)
```

The smallest count determines how many complete `"balloon"` words can be formed.

---

## Dry Run

Example:

```python
text = "balloonballoon"
```

Counts:

```text
b = 2
a = 2
l = 4
o = 4
n = 2
```

Adjusted:

```text
l // 2 = 2
o // 2 = 2
```

Now:

```text
min(2, 2, 2, 2, 2)
```

Result:

```text
2
```

Answer:

```python
2
```

---

## Final Solution

```python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = text.count("b")
        a = text.count("a")
        l = text.count("l")
        o = text.count("o")
        n = text.count("n")

        return min(b, a, l // 2, o // 2, n)
```

---

## Why This Works

To form one `"balloon"` we need:

```text
1 b
1 a
2 l
2 o
1 n
```

The number of complete words we can build is limited by the character that becomes unavailable first.

Taking the minimum of the adjusted counts directly gives the answer.

---

## Complexity Analysis

### Time Complexity

`O(n)`

Each `count()` scans the string.

Since there are only a few fixed letters, the overall complexity remains linear.

### Space Complexity

`O(1)`

Only a handful of variables are used.

---

## Lessons Learned

- My first instinct was simulation.
- Sometimes counting is enough; we don't need to actually perform the process.
- Whenever a problem asks "How many complete groups can be formed?", think about the limiting resource.
- The answer often comes from finding the minimum available count after adjusting for required frequencies.
- Seeing `l` and `o` appear twice in `"balloon"` was the key observation.

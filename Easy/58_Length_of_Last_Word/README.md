# 58. Length of Last Word

## My First Attempt (Massive Overkill 😭)

The funny thing about this problem is that the final solution ended up being only **two lines**, but before reaching that point I somehow spent almost half an hour trying to manually handle every possible case.

I started by reversing the string and then trying to locate spaces to determine where the last word ended.

Something along the lines of:

```python
rt = s[::-1]
```

Then:

```python
rt.index(" ")
```
just look at the code yourselves youll say what a fool he is 
```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
#FIRST ATTEMPT
        # if (len(s) <= 1) and (" " not in s):
        #     return len(s)
        # else:
        #     rt = s[::-1]
        #     if (" " in rt) and (rt.index(" ") > 0):
        #         i = rt.index(" ")
        #         rt = rt[0:i]
        #         #print(rt)
        #         return len(rt)
        #     else:
        #         f = 0
        #         for j in rt:
        #             if j != " ":
        #                 break
        #             else:
        #                 f+=1
        #         #print(f)
        #         i = rt.index(" ",f)
        #         rt = rt[0:i]
        #         #print(rt)
        #         return len(rt) - f

#SECOND ATTEMPT
        # if (len(s) <= 1) and (" " not in s):
        #     return len(s)
        # else:
        #     rt = s[::-1]
        #     if (" " in rt) and (rt.index(" ") > 0):
        #         i = rt.index(" ")
        #         rt = rt[0:i]
        #         #print(rt)
        #         return len(rt)
        #     else:
        #         f = 0
        #         for j in rt:
        #             if j != " ":
        #                 break
        #             else:
        #                 f+=1
        #         print(f)
        #         if f > 1:
        #             i = rt.index(" ",f)
        #             rt = rt[0:i]
        #             #print(rt)
        #             return len(rt) - f
        #         else:
        #             return f
## FINAL WISDOM UNLOCKED ######
        r_l = s.split()
        return len(r_l[len(r_l) - 1])
```
Then counting leading spaces.

Then handling strings with trailing spaces.

Then handling strings without trailing spaces.

Then handling strings with only one word.

Then handling strings with multiple spaces.

And before I knew it, a problem that should have taken a few minutes had turned into a mini project 😂.

---

## Why My Approach Wasn't Ideal

Although it worked for many cases, the code became:

* Long
* Hard to read
* Full of special cases
* Easy to break when a new edge case appeared

I was spending more time handling spaces than actually solving the problem.

---

## The Realization

After staring at the problem for way longer than I should have, I remembered something:

```python
s.split()
```

Python automatically:

* Removes extra spaces
* Removes trailing spaces
* Splits the string into words

For example:

```python
s = "   fly me   to   the moon  "
```

```python
s.split()
```

becomes:

```python
["fly", "me", "to", "the", "moon"]
```

The last word is simply:

```python
r_l[-1]
```

and its length is:

```python
len(r_l[-1])
```

That's it.

Half an hour of overthinking replaced by two lines of code 😭😂.

---

## Final Solution

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r_l = s.split()
        return len(r_l[-1])
```

---

## Dry Run

Example:

```python
s = "Hello World"
```

After:

```python
s.split()
```

we get:

```python
["Hello", "World"]
```

Last word:

```python
"World"
```

Length:

```python
5
```

Answer:

```python
5
```

---

## Complexity Analysis

### Time Complexity

`O(n)`

The string is scanned once during the split operation.

### Space Complexity

`O(n)`

A list containing the words is created.

---

## Lessons Learned

* Don't start handling edge cases manually before checking whether Python already provides a built-in solution.
* Sometimes the cleanest solution is also the shortest.
* Just because a problem looks simple doesn't mean I won't somehow find a way to overengineer it 😂.
* `split()` is much smarter than I initially gave it credit for.

```
```

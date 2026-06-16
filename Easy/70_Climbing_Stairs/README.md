# 70. Climbing Stairs

## My First Thought

When I first saw the problem, I immediately started thinking about combinations and factorials.

I even wrote a factorial helper function:

```python
def fact(n):
    r = n

    if r == 0:
        return 1

    while n > 1:
        n -= 1
        r *= n

    return r
```

My idea was that climbing stairs is similar to arranging steps of size 1 and 2, so maybe I could use combinations to count the possible ways.

I experimented with formulas like:

```python
fact(n) // (fact(2) * fact(n - 2))
```

But very quickly I realized something was wrong.

The number of ways is not determined by a single combination formula because different numbers of 1-step and 2-step moves are possible.

I was trying to force a mathematical formula onto a problem that had a much simpler pattern.

😂 Sometimes the hardest part is realizing you're solving the wrong problem.

---

## The Key Observation

Suppose I'm standing at stair `n`.

How could I have reached it?

There are only two possibilities:

### Option 1

I came from stair:

```text
n - 1
```

and took one step.

### Option 2

I came from stair:

```text
n - 2
```

and took two steps.

Therefore:

- Ways to reach `n - 1`
- Plus ways to reach `n - 2`

must equal the total ways to reach `n`.

This gives the recurrence:

```
ways(n) = ways(n - 1) + ways(n - 2)
```

At that moment I realized:

> Wait a second... this is just the Fibonacci sequence in disguise!

🤯

---

## Recursive Solution

Using the recurrence relation:

```python
class Solution:
    def climbStairs(self, n: int):

        if n == 0 or n == 1:
            return 1

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
```

---

## Dry Run

Example:

```python
n = 4
```

The recursion becomes:

```text
climbStairs(4)
= climbStairs(3) + climbStairs(2)

climbStairs(3)
= climbStairs(2) + climbStairs(1)

climbStairs(2)
= climbStairs(1) + climbStairs(0)
```

Eventually:

```text
climbStairs(4)
= 5
```

Possible paths:

```text
1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
```

---

## The Problem With This Solution

Although the recursion is elegant, it repeats the same calculations many times.

For example:

```text
climbStairs(5)
├── climbStairs(4)
│   └── climbStairs(3)
└── climbStairs(3)
```

Notice that:

```text
climbStairs(3)
```

is computed multiple times.

As `n` grows, the number of repeated calculations explodes.

This causes a Time Limit Exceeded (TLE) error for large inputs.

---

## Better Approach (Dynamic Programming)

Since the same subproblems are solved repeatedly, we can store previous results.

```python
class Solution:
    def climbStairs(self, n: int):

        if n <= 1:
            return 1

        a, b = 1, 1

        for _ in range(2, n + 1):
            a, b = b, a + b

        return b
```

---

## Why This Works

Instead of recomputing:

```text
climbStairs(3)
climbStairs(4)
climbStairs(5)
```

again and again,

we build the answers from smaller values upward.

This follows the same recurrence:

```text
ways(n) = ways(n-1) + ways(n-2)
```

but computes each value only once.

---

## Complexity Analysis

### Recursive Version

Time Complexity:

```text
O(2^n)
```

Space Complexity:

```text
O(n)
```

(due to recursion stack)

---

### Optimized DP Version

Time Complexity:

```text
O(n)
```

Space Complexity:

```text
O(1)
```

---

## Lessons Learned

- My first instinct was combinations and factorials.
- The problem is actually a Fibonacci pattern.
- Recursion makes the relationship easy to see.
- Dynamic Programming makes it efficient.
- Whenever a problem can be expressed as:

```text
f(n) = f(n-1) + f(n-2)
```

it's usually worth thinking about Fibonacci-style solutions.

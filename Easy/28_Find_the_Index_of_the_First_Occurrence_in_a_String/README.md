# 28. Find the Index of the First Occurrence in a String

## Intuition

My first idea was to find the first occurrence of the first character of `needle` and manually build a substring for comparison. However, this approach became complicated due to index handling and missed cases.

I then realized Python slicing provides a much cleaner solution. Instead of building strings character by character, I can directly compare substrings of the required length.

## Approach

1. If `needle` is longer than `haystack`, return `-1`.
2. Iterate through all valid starting positions.
3. Extract a substring using slicing.
4. Compare it with `needle`.
5. Return the index if matched, otherwise return `-1`.

## Complexity

- Time Complexity: `O((n - m + 1) * m)`
- Space Complexity: `O(m)`

## Code

See `solution.py`.

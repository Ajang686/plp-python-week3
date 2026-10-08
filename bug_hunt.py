```python
count = 1
total = 0

# BUG: The while condition was missing a colon.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: The original condition was count < 5, which stopped the loop before adding 5.
# Fixed by changing < 5 to <= 5.

# BUG: The original print statement tried to join a string and an integer.
# Fixed by using an f-string.
print(f"Sum of 1 to 5 is: {total}")
```



# I coordinates of A(x1, y1) and B(x2, y2)
# O: reflection point (x, 0)

# Step 1: Read input
x1, y1 = map(float, input().split())   # Point A
x2, y2 = map(float, input().split())   # Point B

#
# Formula: x = x1 + (y1 * (x2 - x1)) / (y1 + y2)
# y is always 0 because reflection point lies on x-axis
x = x1 + (y1 * (x2 - x1)) / (y1 + y2)
y = 0.0

# Step 3: Print result with 10 decimal places
print(f"{x:.10f} {y:.10f}")

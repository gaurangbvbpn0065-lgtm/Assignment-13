import numpy as np
import matplotlib.pyplot as plt

# =====================================================
# 1. Replace NaN with 0 and interchange rows & columns
# =====================================================

print("1. Replace NaN with 0 and Transpose")

arr = np.array([
    [6, -8, 73, -110],
    [np.nan, -8, 0, 94]
])

arr = np.nan_to_num(arr, nan=0)

print("Array after replacing NaN with 0:")
print(arr)

print("\nTranspose of Array:")
print(arr.T)

# =====================================================
# 2. Move axes of 3D array to new positions
# =====================================================

print("\n2. Move Axes of 3D Array")

array3d = np.arange(24).reshape(2, 3, 4)

print("Original Shape:", array3d.shape)

new_array = np.moveaxis(array3d, 0, 2)

print("New Shape:", new_array.shape)

# =====================================================
# 3. Replace NaN values with average of columns
# =====================================================

print("\n3. Replace NaN with Column Average")

data = np.array([
    [10, np.nan, 30],
    [20, 25, np.nan],
    [30, 35, 40]
])

col_mean = np.nanmean(data, axis=0)

indices = np.where(np.isnan(data))

data[indices] = np.take(col_mean, indices[1])

print(data)

# =====================================================
# 4. Replace negative values with zero
# =====================================================

print("\n4. Replace Negative Values with Zero")

arr2 = np.array([5, -10, 20, -15, 8, -3])

arr2 = np.where(arr2 < 0, 0, arr2)

print(arr2)

# =====================================================
# 5. Average, Mean, Median, Mode of two 2D arrays
# =====================================================

print("\n5. Average, Mean, Median and Mode")

arr1 = np.array([
    [2, 4],
    [6, 8]
])

arr2 = np.array([
    [1, 3],
    [5, 7]
])

average = (arr1 + arr2) / 2

print("Average Array:")
print(average)

combined = np.concatenate((arr1.flatten(), arr2.flatten()))

mean = np.mean(combined)
median = np.median(combined)

values, counts = np.unique(combined, return_counts=True)
mode = values[np.argmax(counts)]

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)

# =====================================================
# 6. Solve Linear Equations using Inverse Matrix
# =====================================================

print("\n6. Solve Linear Equations")

A = np.array([
    [1, -2, 3],
    [-1, 3, -1],
    [2, -5, 5]
])

B = np.array([
    [9],
    [-6],
    [17]
])

A_inv = np.linalg.inv(A)

solution = np.dot(A_inv, B)

print("x =", solution[0][0])
print("y =", solution[1][0])
print("z =", solution[2][0])

# =====================================================
# 7. Compare Two Semester Results using Matplotlib
# =====================================================

subjects = ["Math", "Python", "DBMS", "OS", "CN"]

semester1 = [78, 82, 75, 80, 85]
semester2 = [85, 88, 80, 84, 90]

plt.figure(figsize=(8,5))

plt.plot(subjects, semester1,
         marker='o',
         linewidth=2,
         label="Semester 1")

plt.plot(subjects, semester2,
         marker='s',
         linewidth=2,
         label="Semester 2")

plt.title("Semester Result Comparison")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid(True)
plt.legend()

plt.show()
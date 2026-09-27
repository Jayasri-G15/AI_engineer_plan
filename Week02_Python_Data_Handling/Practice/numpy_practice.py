import numpy as np

marks = np.array([
    78, 85, 92, 67, 88,
    76, 95, 81, 73, 90
])

print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("Total:", np.sum(marks))
print("Shape:", marks.shape)
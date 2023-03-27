# Assignment 1 Threshold-Based Classifier
import numpy as np
import matplotlib.pyplot as plt


# Function Definition
def accuracy(x, y):
    correct = 0
    for (index, (i, j)) in enumerate(zip(cx, cy)):
        if i > x and j > y:
            if label[index] == 0:
                correct += 1
        else:
            if label[index] == 1:
                correct += 1
    return correct * 100 / label.size


def best_threshold():
    all_accuracy = []
    all_xy = []
    x = 1
    y = 1
    for i in range(73):
        all_accuracy.append(accuracy(x, y))
        all_xy.append((x, y))
        if x == 3 and y == 3:
            break
        elif y == 3:
            x += 0.25
            y = 1
            all_accuracy.append(accuracy(x, y))
            all_xy.append((x, y))
        y += 0.25
    m = all_accuracy[0]
    index = 0
    for j in range(1, len(all_accuracy)):
        if all_accuracy[j] > m:
            m = all_accuracy[j]
            index = j
    print("Best Set of suitable threshold with highest possible accuracy: ", all_xy[index])
    print("Maximum Accuracy:", max(all_accuracy), "%")


# Plot
cx = np.array([1, 3, 2, 1, 2, 2])
cy = np.array([1, 2, 3, 2, 2, 1])
label = np.array([0, 0, 0, 1, 1, 1])
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(cx[:3], cy[:3], s=50, c='r', marker="s", label='first')
ax1.scatter(cx[3:], cy[3:], s=50, c='g', marker="^", label='second')
plt.xlabel("x: Feature 1")
plt.ylabel("y: Feature 2")
plt.legend(["Class1", "Class2"], loc="best")
plt.show()

# Main
for count in range(3):
    thx = float(input("Enter the threshold on feature 1: "))
    thy = float(input("Enter the threshold on feature 2: "))
    print("The Classification Accuracy : ", accuracy(thx, thy), "%")
best_threshold()

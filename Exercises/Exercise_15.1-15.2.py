import matplotlib.pyplot as plt

x_values = list(range(1, 5000))
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=3)

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

plt.show()
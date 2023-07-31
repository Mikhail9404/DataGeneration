from random import choice
import matplotlib.pyplot as plt

class RandomWalk():
    """Класс для генерирования случайных блужданий."""

    def __init__(self, num_points=5000):
        """Инициализирует атрибуты блуждания."""
        self.num_points = num_points

        # Блуждение начинается с точки (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        x_step = self.get_step()
        y_step = self.get_step()


    def get_step(self):
        """Вычесляет все точки блуждания."""

        # Шаги генерируются до достижения нужной длины.
        while len(self.x_values) < self.num_points:

            # Определение направления и длины перемещения.
            x_direction = choice([-1, 1])
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            y_step = y_direction * y_distance

            # Отклонение нулевых перемещений.
            if x_step == 0 and y_step == 0:
                continue

            # Вычесление следующих значений x и y.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)


while True:
    # Построение случайного блуждения.
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Нанесение точек на диаграмму.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=3)

    # Выделение первой и последней точек.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Удаление осей.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Построить другой путь? (y/n):")
    if keep_running == 'n':
        break
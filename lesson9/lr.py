import numpy as np
import plotly.graph_objects as go
from sklearn.linear_model import LogisticRegression

n = 100
cluster_1_x = []
cluster_1_y = []
cluster_1_z = []
cluster_2_x = []
cluster_2_y = []
cluster_2_z = []


# генерируем точки случайно
def generate_points():
    x = np.random.randint(0, 100, n)
    y = np.random.randint(0, 100, n)
    z = np.random.randint(0, 100, n)
    points = []
    for i in range(100):
        points.append((x[i], y[i], z[i]))
    return points


# генерируем тестовую плоскость, которая разобьет точки по кластерам (фиктивная кластеризация)
# Ax + By + Cz + d = 0
# d = 0
def generate_test_plane():
    a = np.random.random() * 0.5
    b = np.random.random() * 0.5
    c = - np.random.random() * 0.9
    return a, b, c


# на основе случайной плоскости определяем точки в кластеры
def assign_points_to_cluster(points, a, b, c):
    clusters = []
    for i in range(100):
        x_i = points[i][0]
        y_i = points[i][1]
        z_i = points[i][2]
        if a * x_i + b * y_i + c * z_i < 0:
            clusters.append(0)
            cluster_1_x.append(x_i)
            cluster_1_y.append(y_i)
            cluster_1_z.append(z_i)
        else:
            cluster_2_x.append(x_i)
            cluster_2_y.append(y_i)
            cluster_2_z.append(z_i)
            clusters.append(1)
    return clusters


# поиск весов с помощью логистической регрессии
def find_weights_for_dividing_plane(points, clusters):
    lr = LogisticRegression()
    model = lr.fit(points, clusters)
    return model


# поиск точек разделяющей плоскости с помощью найденных весов для построения
def find_points_for_dividing_plane(model):
    plane_z = np.ones((100, 100))
    for i in range(0, 100):
        for j in range(0, 100):
            plane_z[i][j] = (-model.coef_[0][0] * i - model.coef_[0][1] * j - model.intercept_) / model.coef_[0][2]
    return plane_z


# визуализация плоскости и точек
def draw(plane_z):
    fig = go.Figure(data=[
        go.Scatter3d(x=cluster_1_x, y=cluster_1_y, z=cluster_1_z, mode="markers", name="-1"),
        go.Scatter3d(x=cluster_2_x, y=cluster_2_y, z=cluster_2_z, mode="markers", name="1"),
        go.Surface(z=plane_z)
    ])
    fig.show()


def logistic_regression_with_dividing_plane():
    points = generate_points()
    a, b, c = generate_test_plane()
    clusters = assign_points_to_cluster(points, a, b, c)
    model = find_weights_for_dividing_plane(points, clusters)
    plane_z = find_points_for_dividing_plane(model)
    draw(plane_z)


logistic_regression_with_dividing_plane()

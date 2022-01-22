"""
COMS 4733: Computational Aspects of Robotics
HW1 Problem 5.1
Convex Hull Algorithm
"""
import scipy
import numpy as np
from scipy.spatial import ConvexHull, convex_hull_plot_2d
import matplotlib.pyplot as plt


def plot_before(rob: list, obs: list) -> None:
    x, y = np.array(rob).T
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.fill_between(x, y)
    x, y = np.array(obs).T
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.fill_between(x, y)
    plt.show()


def plot_c_space(vertices: list) -> None:
    x, y = np.array(vertices).T
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.fill_between(x, y)
    plt.show()


def minkowski(rob_list: list, obs_list: list) -> list:
    reference_point = rob_list[0]
    rob_vertices = rob_list[1:]
    graph_rob = rob_vertices
    graph_rob.append(rob_vertices[0])
    graph_obs = obs_list
    graph_obs.append(obs_list[0])
    plot_before(graph_rob, graph_obs)
    # translation indicates the movement each vertex has to perform to move with
    # the reference point to the origin --> the negation of the reference point
    translation = [-x for x in reference_point]
    translated = []
    for vertex in rob_vertices:
        t_vertex = [vertex[0] + translation[0], vertex[1] + translation[1]]
        translated.append(t_vertex)
    reflected = np.array(translated)
    reflected *= -1
    mink = []
    for vertex in obs_list:
        for v in reflected:
            v = [v[0] + vertex[0], v[1] + vertex[1]]
            mink.append(v)
    np_mink = np.array(mink)
    hull = ConvexHull(np_mink)
    c_space_obs = []
    for i in hull.vertices:
        c_space_obs.append(np_mink[i])
    print(c_space_obs)
    c_space_obs.append(c_space_obs[0])
    plot_c_space(c_space_obs)


if __name__ == "__main__":
    example_1_rob = [[0, 0], [0, 0], [1, -1], [0, -2], [-1, -1]]
    example_1_obs = [[2, 4], [3, 2], [2, 0], [-2, 0], [-3, 2], [-2, 4]]
    minkowski(example_1_rob, example_1_obs)

    example_2_rob = [[0, -4], [-1, -1], [-3, -1], [-4, -4], [0, -4]]
    example_2_obs = [[0, 0], [-3, 4], [3, 4]]
    minkowski(example_2_rob, example_2_obs)

    example_3_rob = [[0, 2], [0, 0], [4, 2], [-4, 2]]
    example_3_obs = [[0, -1], [-2, -4], [2, -4]]
    minkowski(example_3_rob, example_3_obs)

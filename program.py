
import math
import sys

import numpy as npr

import drawer
import helper

def calc_eucl_dist(point_one, point_two):
    return math.sqrt((point_two[0]-point_one[0])**2 + (point_two[1]-point_one[1])**2)

def find_max_distant_point(center, points):
    max_distance = 0
    for point in points:
        distance = calc_eucl_dist(center, point)
        if distance > max_distance:
            max_distance = distance
            distant_point = point
    return distant_point

def find_max_distant_point_in_center(centers, points_in_clusters):
    max_distances = []
    for center in centers:
        max_distance = 0
        for point_in_cluster in points_in_clusters[centers.index(center)]:
            distance = calc_eucl_dist(center, point_in_cluster)
            if distance > max_distance:
                max_distance = distance
        max_distances.append(max_distance)
    return max(max_distances), max_distances.index(max(max_distances))

def finding_average_distance_between_centers(centers):
    distance = 0
    len_of_centers = len(centers)
    for index in range(len_of_centers - 1):
        distance += calc_eucl_dist(centers[index], centers[index + 1])
    return distance / len_of_centers

def create_empty_list(dimension):
    array = []
    for i in range(len(dimension)):
        array.append([])
    return array

def search_center_for_points(centers, points):
    array = create_empty_list(centers)
    for point in points:
        prev_distance = 1000
        for center in centers:
            curr_distance = calc_eucl_dist(center, point)
            if curr_distance < prev_distance:
                prev_distance = curr_distance
                index_of_cluster = centers.index(center)
        array[index_of_cluster].append(point)
    return array

def add_point_to_centers(list_of_centers, point):
    list_of_centers.append(point)

def create_list_of_points(matrix_of_coord):
    list_of_points = []
    for index in range(len(matrix_of_coord[0])):
        point = [matrix_of_coord[0][index], matrix_of_coord[1][index]]
        list_of_points.append(point)
    return list_of_points

def create_empty_list_x_y(number_of_centers):
    array = []
    for i in range(number_of_centers):
        array.append([[], []])
    return array

def create_points_x_y(points_in_clusters, number_of_clusters):
    array = create_empty_list_x_y(number_of_clusters)
    for points in points_in_clusters:
        for point in points:
            array[points_in_clusters.index(points)][0].append(point[0])
            array[points_in_clusters.index(points)][1].append(point[1])
    return array

if __name__ == "__main__":
    COUNT_OF_IMAGES = helper.read_data_command_line(sys.argv[1:])
    MRX_OF_COORDS_IMAGES = npr.random.random_sample((2, COUNT_OF_IMAGES))

    POINTS = create_list_of_points(MRX_OF_COORDS_IMAGES)

    centers = []
    add_point_to_centers(centers, POINTS[0])
    add_point_to_centers(centers, find_max_distant_point(centers[0], POINTS))
    points_in_clusters = search_center_for_points(centers, POINTS)

    max_distance_from_center, index_of_center = find_max_distant_point_in_center(centers, points_in_clusters)
    average_distance = finding_average_distance_between_centers(centers)

    while max_distance_from_center > average_distance / 2:
        add_point_to_centers(centers, find_max_distant_point(centers[index_of_center], points_in_clusters[index_of_center]))
        points_in_clusters = search_center_for_points(centers, POINTS)
        max_distance_from_center, index_of_center = find_max_distant_point_in_center(centers, points_in_clusters)
        average_distance = finding_average_distance_between_centers(centers)

    points_in_clusters_x_y = create_points_x_y(points_in_clusters, len(centers))

    print('max distance: ', max_distance_from_center)
    print('average distance: ', average_distance)

    drawer.draw_graph(centers, points_in_clusters_x_y)

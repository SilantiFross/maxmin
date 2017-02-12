
import sys
import getopt

def read_data_command_line(argv):
    count_of_images = 1000
    try:
        opts, args = getopt.getopt(argv, "hi:")
    except getopt.GetoptError:
        print('program.py -i <count_of_images>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('program.py -i <count_of_images>')
            sys.exit()
        elif opt == '-i':
            count_of_images = arg
    return int(count_of_images)

def conversation_to_matrix(points):
    matrix = [[], []]
    for point in points:
        matrix[0].append(point[0])
        matrix[1].append(point[1])
    return matrix

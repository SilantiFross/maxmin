
import helper

import matplotlib.pyplot as plt

def draw_graph(centers, points):
    mtrx_of_centers = helper.conversation_to_matrix(centers)
    array_of_color = ['#FF0000', '#00FF00', '#00FFFF', '#7FAFD4', '#8A2BE2',
                      '#A52A2A', '#DC143C', '#A9A9A9', '#006400', '#8B008B',
                      '#FF8C00', '#228B22', '#DCDCDC', '#ADFF2F', '#7CFC00',
                      '#FFFACD', '#F08080', '#B0C4DE', '#FFA07A', '#20B2AA']

    index_clr = 0
    for point in points:
        plt.plot(point[0], point[1], 'o', color=array_of_color[index_clr], markersize=3)
        index_clr += 1

    plt.plot(mtrx_of_centers[0], mtrx_of_centers[1], 's', color='blue', markersize=5)

    plt.title('Result of alghoritm maxmin')
    plt.xticks(())
    plt.yticks(())
    plt.show()

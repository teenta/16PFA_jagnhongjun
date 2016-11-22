# -*- coding: utf8 -*-
# 위에껀 한글표시
# 2011111031 장홍준
# 주석 추가
import random

import pylab

import gauss_jordan as gj
import matrix

random.seed()


def least_square_first_order(vec_x, vec_y):
    """
    x 와 y 사이에
    y = a x + b
    와 같은 관계가 있을 것으로 가정하고 a, b 를 찾으려고 함
    :param vec_x: List[float]
    :param vec_y: List[float]
    :return:
    """
    # 에를 들어 data point 의 갯수를 n 이라 할 때
    mat_x_t = [vec_x,
               [1] * len(vec_x)]
    mat_x = matrix.transpose_mat(mat_x_t)
    mat_y_measured = matrix.transpose_mat([vec_y])
    mat_w_estimated = mul_left_inverse(mat_x, mat_y_measured)
    return mat_w_estimated


def mul_left_inverse(mat_x, mat_y):
    """
    행령 X 의 좌 역행렬 Left Inverse Matrix 를 찾아서 y 행렬과 곱함
    예를 들어 X 의 행의 갯수는 data point 갯수와 같고.
              X 의 열의 갯수는 추정하고자 하는 매개변수의 수와 같다
    :param mat_x: List[List[float]]
    :param mat_y: List[List[Float]]
    :return: List[List[float]]
    """
    mat_x_left_inverse = get_left_inverse(mat_x)
    mat_w_estimated = matrix.mul_mat(mat_x_left_inverse, mat_y)

    del mat_x_left_inverse[:]
    del mat_x_left_inverse
    return mat_w_estimated


if __name__ == '__main__':
    def get_left_inverse(mat_x):
        """
        :param mat_x: List[List[float]]
        :return: List[List[float]]
        """
        # 예를들어 data point 의 갯수를 n
        #          매개변수의 갯수를 m 이라 할 때
        mat_x_t = matrix.transpose_mat(mat_x)
        mat_xt_x = matrix.mul_mat(mat_x, mat_x)
        mat_xt_x_inv = gj.gauss_jordan(mat_xt_x)
        mat_x_left_inverse = matrix.mul_mat(mat_xt_x_inv, mat_x_t)
        return mat_x_left_inverse

def contaminate(vec_y, standard_deviation=0.5):
    vec_y_measured = [yi + random.gauss(0.0, standard_deviation) for yi in vec_y]
    return vec_y_measured


def visualize_least_square_first_order(a_hat, b_hat, vec_x, vec_y, vec_y_measured):
    pylab.plot(vec_x, [a_hat * xi + b_hat for xi in vec_x], label='estimated')
    pylab.plot(vec_x, vec_y_measured,'.', label='measured')
    pylab.plot(vec_x, vec_y, 'r', label='truth')
    pylab.grid(True)
    pylab.legend(loc=0)
    pylab.show()


def main():
    n_data = 100

    a = 0.5
    b = 1.0

    vec_x = [i * 0.1 for i in range(0, n_data)]
    vec_y = [a * xi + b for xi in vec_x]

    vec_y_measured = contaminate(vec_y)

    mat_w = [[a], [b]]

    mat_w_estimated = least_square_first_order(vec_x, vec_y_measured)
    a_hat = mat_w_estimated[0][0]
    b_hat = mat_w_estimated[1][0]

    matrix.show_mat(mat_w, '%g')
    matrix.show_mat(mat_w_estimated, '%g')

    visualize_least_square_first_order(a_hat, b_hat, vec_x, vec_y, vec_y_measured)


if __name__ == '__main__':
    main()
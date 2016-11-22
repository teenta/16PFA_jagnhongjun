# -*- coding: utf8 -*-
# 2011111031 장홍준
# 각 행의 자세한 주석을 추가하시오
"""
 고유 해석 모듈
 python의 list 을 이용하는 행렬로 구현함
"""

import math

import gauss_jordan as gj
import matrix

def power_method(mat_a, epilon=1e-9, b_verbose=False):
    # 행렬의 크기
    n = len(mat_a)

    # 가장 큰 고유치를 담게 될 변수
    lambda_k = 0.0
    lambda_k1 = 1.0
    # 위 고유치의 고유 벡터를 저장할 장소
    zk = [1.0] * n


    counter = 0
    # k : 반복횟수
    # i : i번째 고유치. 고유 벡터
    while True:
        # 행렬 곱셈
        # k가 큰 값이라면 z_k 는 첫번째 고유벡터와 거의 같은 방향이므로
        # y_k+1 = mat_a z_k = lambda_1 z_k
        # z_k 의 가장 큰 요소는 1 이었으므로
        # y_k+1 의 가장큰 요소가 lambda_1 인 것이라고 볼 수 있다
        yk1 = matrix.mul_mat_vec(mat_a, zk)

        # yk1 벡터에서 절대값이 가장 큰 요소를 찾음
        lambda_k1 = abs(yk1[0])
        for yk1_i in yk1[1:]:
            if abs(yk1_i) > abs(lambda_k1):
                lambda_k1 = yk1_i

        # 위에서 찾은 값으로 yk1 모든 요소를 나누어서 zk 벡터에 저장
        # "위에서 찾은 값으로 yk1 을 normalize 한다"
        # zk 의 가장 큰 요소는 1이됨
        for i in range(n):
            zk[i] = yk1[i] / lambda_k1

        # 이전 단계의 가장 큰 요소와 비교
        if abs(lambda_k1 - lambda_k) < epsilon:
            break
        lambda_k = lambda_k1

        # 사용이 완료된 y1 벡터의 메모리 공간을 반환
        del yk1
        counter += 1

    if b_verbose:
        print ("power method counter = %d" % counter)

    return lambda_k1, zk

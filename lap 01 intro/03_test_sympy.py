# -*- coding: utf8 -*-
# sybolic prosessor 기능을 가진 sympy 를 불러 들어 sp 라는 이름과 연결시킴
import sympy as sp

# sympy 의 symbols 기능을 이용해 기호 x y를 정함
x, y = sp.symbols('x y')

# 기호 x y 를 이용해 기호 z 를 정함
z = x + 2 * y

# 기호 z 를 화면에 표시함
print ('z = %s' % z)

# SymPy Tutorial, http://docs.sympy.org/latest/tutorial/index.html

z_iy = sp. integrate(z, y)
print ('z_iy = %s' % z_iy)

z_ix = sp. integrate(z, x)
print ('z_ix = %s' % z_ix)

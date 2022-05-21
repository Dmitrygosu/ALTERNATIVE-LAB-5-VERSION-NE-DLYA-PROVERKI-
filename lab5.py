"""30.   Формируется матрица F следующим образом: скопировать в нее А и  если в В количество простых чисел в нечетных столбцах, чем произведение чисел по периметру С,
 то поменять местами  С и В симметрично, иначе С и В поменять местами несимметрично. 
При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов матрицы F, то вычисляется выражение: AAT – K F,
 иначе вычисляется выражение (A*-1 +G-F*-1)*K,
 где G-нижняя треугольная матрица, полученная из А. Выводятся по мере формирования А, F и все матричные операции последовательно."""

import numpy as np
 
def prime(num):
    if num<2:
        return False
    d = 2
    while d*d <= num:
        if not num%d:
            return False
        d += 1
    return True
 
 
k, n = 5, 6
m = n//2
 
b = np.random.randint(-10,10,(m,m))
print(b,'\n')
c = np.random.randint(-10,10,(m,m))
print(c,'\n')
d = np.random.randint(-10,10,(m,m))
print(d,'\n')
e = np.random.randint(-10,10,(m,m))
print(e,'\n')
 
A = np.vstack((np.hstack((e,b)), np.hstack((d,c))))
print(A,'\n')
 
vec = np.frompyfunc(prime,1,1)
prime_b = vec(b[:,::2]).sum()
 
c[1:-1,1:-1] = 1
prod_c = np.prod(c)
 
F = A.copy()
if prime_b > prod_c:
    F[:,m:] = F[::-1,m:]
else:
    F[:,m:] = np.vstack((F[m:,m:],F[:m,m:]))
print(F,'\n')
 
if np.linalg.det(A) > np.diag(F).sum():
    AT = A.T
    res = A*AT - k*F
else:
    A1 = np.linalg.inv(A)
    F1 = np.linalg.inv(F)
    G = np.tril(A, k=-1)
    res = (A*-1 + G - F*-1)*k
print(res)
print('end')

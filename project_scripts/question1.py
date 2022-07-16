"""
A. Given an array A of N integers, write a function missing_int(A) that returns the smallest
positive integer (greater than 0) that does not occur in A.
● A = [1, 3, 6, 4, 1, 2] should return 5
● A = [1, 2, 3] should return 4
● A = [-1, -1, -1, -5] should return 1
● A = [1, 3, 6, 4, 1, 7, 8, 10] should return 2
"""

def missing_int(A):
    
    arr_len = len(A)
    N = set(range(1, arr_len+2))
    return min(N - set(A))

if __name__ == '__main__':
    A = [1, 3, 6, 4, 1, 2]
    B = [1, 2, 3]
    C = [-1, -1, -1, -5]
    D = [1, 3, 6, 4, 1, 7, 8, 10]
    print(missing_int(D))
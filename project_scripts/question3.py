"""
C. Write a rotate(A, k) function which returns a rotated array A, k times; that is, each
element of A will be shifted to the right k times
● rotate([3, 8, 9, 7, 6], 3) returns [9, 7, 6, 3, 8]
● rotate([0, 0, 0], 1) returns [0, 0, 0]
● rotate([1, 2, 3, 4], 4) returns [1, 2, 3, 4]
"""
import collections

def rotate(A, k):

    dequeue_object = collections.deque()
    #print (A)
    for item in A:
        dequeue_object.append(item)

    dequeue_object.rotate(k)

    return list(dequeue_object)

if __name__ == '__main__':

    print(rotate([3, 8, 9, 7, 6], 3))
    print(rotate([0, 0, 0], 1))
    print(rotate([1, 2, 3, 4], 4))
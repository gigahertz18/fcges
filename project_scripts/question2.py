"""
B. Write a function find_divisible(a, b, k) that accepts three integers: a, b and k, and returns
the total count of the numbers between a and b (inclusive) that are divisible by k
● find_divisible(6,11,2) should return 3. 6, 8, and 10 are all divisible by 2.
● find_divisible(0,12,3) should return 5. 0, 3,6, 9, and 12 are all divisible by 3.
"""

def find_divisible(a, b, k):
    ret_list = []
    count = 0
    for i in range(a, b + 1):
        if i%k == 0:
            ret_list.append(i)
            count += 1
    print (ret_list)
    return count

if __name__ == '__main__':

    print(find_divisible(6, 11, 2))
    print(find_divisible(0, 12,3))

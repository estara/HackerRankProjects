# You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n.
# Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i + j + k is not equal to n.
#
# Input Format
# Four integers x, y, z and n, each on a separate line.
#
# Constraints
#
# Print the list in lexicographic increasing order.
#
# Sample Input 0
#
# 1
# 1
# 1
# 2
# Sample Output 0
#
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
# Explanation 0
#
# Each variable x, y and z will have values of 0 or 1. All permutations of lists in the
# form [i, j, k] = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]].
# Remove all arrays that sum to n=2 to leave only the valid permutations.


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

def ijk(x, y, z, n):
    results = ([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1)])
    print([t for t in results if sum(t) != n])

ijk(x, y, z, n)
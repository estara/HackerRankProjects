# You are given a function f(X) = X^2.  You are also given k lists.  The Ith list consists of Ni elements.
#
# You have to pick one element from each list so that the value from the equation below is maximized:
#
# S = (f(X1) + f(X2) + ... + f(Xk))%m
#
# Xi denotes the element picked from the Ith list .  Find the maximized value Smax obtained.
#
# % denotes the modulo operator.
#
# Note that you need to take exactly one element from each list, not necessarily the largest element.  You add the
# squares of the chosen elements and perform the modulo operation.  The maximum value that you can obtain, will be the
# answer to the problem.
#
# Input Format
#
# The first line contains 2 space separated integers k and m.
# The next k lines each contains an integer Ni, denoting the number of elements in the Ith list, followed by Ni space
# separated integers denoting the elements in the list.
#
# Output Format
#
# Output a single integer denoting the value Smax.
#
# Sample Input
#
# 3 1000
# 2 5 4
# 3 7 8 9
# 5 5 7 8 9 10
# Sample Output
#
# 206
# Explanation
#
# Picking 5 from the 1st list, 9 from the 2nd list and 10 from the 3rd list gives the maximum S value equal to
# (5^2 + 9^2 + 10^2) % 1000 = 206.

from itertools import product


class MaximizeIt:
    def __init__(self, inputs):
        self.biggest = 0
        self.arr = []
        self.m = int

    def s_x(self, k, m, my_list, f_x=lambda x: pow(x, 2)):
        assert callable(f_x)
        assert isinstance(k, int)
        assert isinstance(m, int)

    # parse the inputs
    def parse_input(self, inputs):
        initial = inputs.split("\n")
        for each in initial:
            foo = each.strip(" ")
            self.arr.append(list(map(int, foo.split(" "))))
        letters = self.arr.pop(0)
        self.m = letters[1]
        return self.arr, self.m

    def slice_input(self, arr):
        for group in arr:
            group.pop(0)
        self.slices = list(product(*arr))
        return self.slices

    # run one slice
    def totaling(self, slices, m):
        self.total = sum([i**2 for i in slices]) % m
        return self.total

    def is_biggest(self, totals):
        if totals > self.biggest:
            self.biggest = totals
        return self.biggest

def maxing(input):
    some_input = open(input)
    useable = some_input.read()
    temp = MaximizeIt(useable)
    temp.parse_input(useable)
    temp.slice_input(temp.arr)
    for i in temp.slices:
        temp.totaling(i, temp.m)
        temp.is_biggest(temp.total)
    return temp.biggest

if __name__ == "__main__":
    pass

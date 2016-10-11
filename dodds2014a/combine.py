import sys

with open(sys.argv[1]) as lhs:
    with open(sys.argv[2]) as rhs:
        for left, right in zip(lhs, rhs):
            print(left.strip()+"\t"+right.strip())


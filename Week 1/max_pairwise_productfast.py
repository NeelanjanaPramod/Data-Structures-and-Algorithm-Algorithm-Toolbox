# python3


def max_pairwise_product(numbers, len):
    big = -1
    for i in range(len):
        if (big == -1 or numbers[i] > numbers[big]):
            big = i
    big2 = -1
    for j in range(len):
        if (j != big) and (big2 == -1 or (numbers[j] > numbers[big2])):
            big2 = j

    return numbers[big] * numbers[big2]


if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    assert (len(a) == n)
    print(max_pairwise_product(a, n))
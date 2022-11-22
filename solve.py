def solve(n, repeats):
    num_n = str(n)
    list_ = []
    for i in range(1, repeats + 1):
        list_.append(int(num_n * i))
        result = sum(list_)
    return result

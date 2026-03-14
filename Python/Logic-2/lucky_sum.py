def lucky_sum(a, b, c):
    values = [a, b, c]
    cut = values.index(13) if 13 in values else len(values)
    return sum(values[:cut])
    
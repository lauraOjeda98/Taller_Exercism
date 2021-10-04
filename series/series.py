def slices(series, length):
    len_series = len(series)

    if length <= 0 or length > len_series:
        raise ValueError("Not valid.")

    slices = []
    for i in range(0, len_series - length+1):
        slices += [series[i:i+length]]

    return slices

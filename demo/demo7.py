def print_vertical_histogram(data):
    max_value = max(data)
    print('max', max_value)
    for level in range(max_value, 0, -1):
        line = ""
        for value in data:
            if value >= level:
                line += " * "
            else:
                line += "   "
        print(line)

    # x-axis
    # print("-" * (len(data) * 3))
    # for i in range(len(data)):
    #     print(f" {i + 1} ", end="")
    # print("\n")

data_values = [2, 5, 7]
print_vertical_histogram(data_values)

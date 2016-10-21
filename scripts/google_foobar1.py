def answer(data, n):
    # your code here
    new_data = list(data)
    list_of_removed_items = list()
    for i in data:
        value_counter = data.count(i)
        if value_counter > n and i not in list_of_removed_items:
            list_of_removed_items.append(i)
            for j in range(value_counter):
                new_data.remove(i)
    return new_data

if __name__ == "__main__":
    data = [1, 2, 3]
    n = 0
    print answer(data, n)

main_list = [12, 3, 45, 8, 22, 17, 5, 30, 1, 16,
             "banana", "apple", "pear", "grape", "kiwi",
             "orange", "melon", "peach", "plum", "cherry"]

ints_sorted = sorted([x for x in main_list if isinstance(x, int)])
strs_sorted = sorted([x for x in main_list if isinstance(x, str)])

sorted_list = ints_sorted + strs_sorted
even_list = [x for x in ints_sorted if x % 2 == 0]

print("Відсортований список:", sorted_list)
print("Кратні 2:", even_list)

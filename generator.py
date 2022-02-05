import csv
import sys

range_nums = range(10)
# for i in range_nums:
#     print(i)

list_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in list_nums:
#     print(i)

# メモリサイズを計算
# rangeは使われる時に計算して確保する(generator)
# print(sys.getsizeof(range_nums))
# print(sys.getsizeof(list_nums))


with open("example.csv") as f:
    reader = csv.DictReader(f)  # これはgenerator
    for line in reader:     # forのたびにメモリを確保する
        print(line)

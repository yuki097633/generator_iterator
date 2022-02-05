import sys

# リスト内包表記
# メモリを最初に使っちゃう
square_list = [num * num for num in range(100)]
# print(square_list)

# ()にするとgeneratorになる　generator_expression
# nextで呼ぶ形でできる
square_gen = (num * num for num in range(100))
# print(next(square_gen))
# print(next(square_gen))
# print(next(square_gen))
# print(next(square_gen))
# print(next(square_gen))

print(sys.getsizeof(square_list))
print(sys.getsizeof(square_gen))

even_square = [num * num for num in range(10) if num % 2 == 0]
print(even_square)

even_square_gen = (num * num for num in range(10) if num % 2 == 0)
for num in even_square_gen:
    print(num)

# できるならgenerator_expressionで作れると楽

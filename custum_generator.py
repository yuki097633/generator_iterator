# range(10)
def my_range(stop):
    start = 0
    while start < stop:
        # return start
        yield start  # yieldだとその関数はgeneratorになる
        start += 1

# ジェネレーター関数の戻り値はgenerator iteratorオブジェクト
# イテレーションによりyieldの値を返すオブジェクトになる


# mrはgenerator
mr = my_range(10)
# print(type(mr))
# print(next(mr))
# print(next(mr))

# for i in mr:
#     print(i)


# challenge
def even(num):
    while num >= 2:
        if num % 2 == 0:
            yield num
        num -= 1


for i in even(10):
    print(i)

print("*" * 30)
even_gen = even(10)
print(next(even_gen))
print(iter(even_gen))

# Demo.py 
import sys
import timeit

# List와 Tuple 생성
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

# 1. 가변성(Mutability) 테스트
print("1. Mutability 테스트:")
try:
    my_list[0] = 10
    print("List 변경 가능:", my_list)
except TypeError as e:
    print("List 변경 불가능:", e)

try:
    my_tuple[0] = 10
    print("Tuple 변경 가능:", my_tuple)
except TypeError as e:
    print("Tuple 변경 불가능:", e)

# 2. 속도 테스트
print("\n2. 속도 테스트:")
list_time = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)
tuple_time = timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000)
print(f"List 생성 속도: {list_time:.6f}초")
print(f"Tuple 생성 속도: {tuple_time:.6f}초")

# 3. 메모리 사용량 비교
print("\n3. 메모리 사용량 비교:")
print("List 메모리 사용량:", sys.getsizeof(my_list), "bytes")
print("Tuple 메모리 사용량:", sys.getsizeof(my_tuple), "bytes")


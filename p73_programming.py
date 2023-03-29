# # 1번 문제
# x = int(input("닭의 수: ")) #닭
# y = int(input("돼지의 수: ")) #돼지
# z = int(input("소의 수: ")) #소

# total = (x * 2) + (y * 4) + (z * 4)

# print(f"전체 다리의 수: {total}")


# # 2번 문제
# w, h = map(float, input("면적과 높이를 콤마로 구분해서 입력하세요 ").split(","))

# area = w * h * 0.5

# print(f"삼각형의 넓이: {area}")


# # 3번 문제
# price = int(input("상품의 가격 : "))
# cnt = int(input("상품의 개수 : "))
# tax = int(input("부가세 : "))
# dfee = int(input("배송료 : "))

# total = (price * cnt)+(price * cnt * (tax/100)) + dfee

# print(f"전체 가격 = {total}")


# 4번 문제
a = 10
b = 20


print(f"바꾸기 전: a = {a} b = {b}")

# x = b
# b = a
# a = x

a, b = b, a
print(f"바꾸기 후: a = {a} b = {b}")
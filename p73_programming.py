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


# # 4번 문제
# a = 10
# b = 20


# print(f"바꾸기 전: a = {a} b = {b}")

# # x = b
# # b = a
# # a = x

# a, b = b, a
# print(f"바꾸기 후: a = {a} b = {b}")


# # 5번 문제
# import turtle
# t= turtle.Turtle()
# t.shape("turtle")

# side=int(input("삼각형 변의 길이를 알려주세요."))
# t.forward(side)
# t.left(120)
# t.forward(side)
# t.left(120)
# t.forward(side)

# turtle.done()


# # 6번 문제
# x = '''반짝 반짝 작은별 ....\n
# 동쪽하늘에서도 ....\n
# 반짝 반짝 작은별 ....\n'''

# print(x)


# # 7번 문제
# x = input("드라이브 이름 : ")
# y = input("디렉토리 이름 : ")
# z = input("파일 이름 : ")
# k = input ("확장자 : ")

# s=x+":"+y+z+"."+k
# print(f"완전한 이름은 {s}")


# 8번 문제
street= input("주소 : ")
type= input("건물 유형 : ")
number_of_rooms=input("방의 갯수 : ")
price=input("가격 : ")

x='''
###################################
#                                 #
#        부동산 매물 광고          #
#                                 #
###################################
'''
print(x)
y="{street}에 위치한 아주 좋은 {type} 가 매물로 나왔습니다. 이 아파트는 {number_of_rooms} 개의 방을 가지고 있으며 가격은 {price} 원입니다."
print(y)
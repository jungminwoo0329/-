#터틀 그래픽을 이용해서 그림 그리기 예제
import turtle # 터틀 그래픽 사용을 선언

t = turtle.Turtle()
t.shape("turtle") # 거북이 모양을 정의

t.fillcolor("blue")

t.begin_fill()
t.penup()
t.goto(-200,-100)
t.pendown()
t.goto(-200,200)
t.goto(200,200)
t.goto(200,-100)
t.goto(-200,-100)
t.penup()
t.end_fill()

t.fillcolor("brown")

t.begin_fill()
t.goto(0,0)
t.pendown()
t.goto(0,100)
t.goto(100,100)
t.goto(100,0)
t.goto(0,0)
t.penup()


t.end_fill()

t.begin_fill()
t.goto(-200,200)
t.pendown()
t.goto(0,300)
t.goto(200,200)
t.goto(-200,200)
t.penup()
t.end_fill()

turtle.done()

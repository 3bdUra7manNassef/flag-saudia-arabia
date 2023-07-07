#drowning a flag saudi_arabia

#*modules*#
import turtle

#*create a window*#
wind = turtle.Screen()
wind.setup(500,500)
wind.title('saudi_arabia')
wind.bgcolor('#000000')

#*create an abo_grgr(object)*#
abo_grgr = turtle.Turtle()
abo_grgr.speed(0)
abo_grgr.color('#006400')
abo_grgr.penup()
abo_grgr.goto(100, 50)
abo_grgr.hideturtle()
abo_grgr.pendown()
abo_grgr.pensize(3)
abo_grgr.begin_fill()

#*create a writer*#
write = turtle.Turtle()
write.pendown()
write.hideturtle()
write.color('#006400')
write.goto(-150,-50)
write.color('black')
write.write('المملكة العربية السعودية', move=False, align='left', font=('Arial', 12, 'normal'))

#*draw a rectangular*#

abo_grgr.right(90)
abo_grgr.fd(200)
abo_grgr.right(90)
abo_grgr.fd(350)

abo_grgr.right(90)
abo_grgr.fd(200)
abo_grgr.right(90)
abo_grgr.fd(350)
abo_grgr.end_fill()

abo_grgr.goto(-150,-100)
abo_grgr.color('#F0F8FF')
abo_grgr.fd(150)

#*stay screen*#
turtle.mainloop()

import turtle
from Service.L_System import L_System
from Service.DrawWord import Draw_Path

l_system = L_System()
drawing = Draw_Path()

word = l_system.iterate_replace(7)
drawing.draw(word)

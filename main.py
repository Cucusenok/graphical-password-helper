# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 19:12:21 2019

@author: cucusenok
@name: grafic key generator
"""

from tkinter import *

class MainCanvas():
    def __init__(self):
        self.canvas = Canvas(root, width=400, height=400, bg='white')
        self.canvas.pack()
        self.circleRadius = 0
        
    def createGraficsKeys(self, startPosition):
        x,y = startPosition, startPosition #начальная позиция X|Y относительно canvas
        margin_left = 20 #фактически диаметр
        self.circleRadius = margin_left/2
        for n in range(9):
            #получаем возможность обращаться к точкам по индексу, так же как при сгенерированном алгоритмом
            self.canvas.create_oval(x, y,
                               x+margin_left, y+margin_left, 
                               fill='yellow', outline='blue', 
                               width=2)
            x+=40
            if ((n+1) % 3 == 0):
                y+=40 #сделаем отступ от предыдущей строки
                x=startPosition #вернем в начало строки
                
    #создает линию связующую точки на canvas
    def createDotCircleConnection(self, circle1, circle2):
        #соеденим круги линией. берем x и y координаты первого и второго круга и смещаем на их радиус 
        #чтобы линия выходила из центра круга
        self.canvas.create_line(self.canvas.coords(circle1)[0] + self.circleRadius,  self.canvas.coords(circle1)[1] + self.circleRadius,
                             self.canvas.coords(circle2)[0] + self.circleRadius,  self.canvas.coords(circle2)[1] + self.circleRadius,
                                 fill='red', width=3, arrow=LAST)
        

        
root = Tk()
 

canvas = MainCanvas()
canvas.createGraficsKeys(80)
canvas.createDotCircleConnection(1, 2)
canvas.createDotCircleConnection(2, 3)
canvas.createDotCircleConnection(3, 5)
canvas.createDotCircleConnection(5, 9)
canvas.createDotCircleConnection(9, 7)



#createDotCirclesnection(canvas, 1, 2, radius)
#createDotCirclesnection(canvas, 3, 9, radius)

 

 
root.mainloop()



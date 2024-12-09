import simplegui
import math

# Global Variables

width = int(input("Initial Width?"))
height = int(input("Initial Height?"))
face1 = False
face2 = False
face3 = False
face4 = False
face5 = False

# Event Handlers

def all_false():
    global face1
    global face2
    global face3
    global face4
    global face5
    face1 = False
    face2 = False
    face3 = False
    face4 = False
    face5 = False
    
def toggle_topLeft():
    all_false()
    global face1
    face1 = not face1
    
def toggle_topRight():
    all_false()
    global face2
    face2 = not face2
      
def toggle_bottomLeft():
    all_false()
    global face3
    face3 = not face3
    
def toggle_bottomRight():
    all_false()
    global face4
    face4 = not face4

def draw(canvas):
    leftWidth = width*0.25
    topHeight = height*0.25
    rightWidth = width*0.75
    if face1:
        canvas.draw_circle((leftWidth, topHeight), topHeight, 1, "Yellow", "Yellow")
        canvas.draw_circle((leftWidth*0.2,topHeight*0.2), topHeight*0.2, 1, "yellow", "yellow")
        canvas.draw_circle((leftWidth*1.8,topHeight*0.2), topHeight*0.2, 1, "yellow", "yellow")
        canvas.draw_circle((leftWidth*0.6,topHeight*0.6),topHeight*0.2,2,"black","black")
        canvas.draw_circle((leftWidth*1.4,topHeight*0.6),topHeight*0.2,2,"black","black")
        canvas.draw_polygon([(leftWidth*0.6,topHeight*1.1),(leftWidth,topHeight*1.6),(leftWidth*1.4,topHeight*1.1)], 2,"black","white")
    if face2:
        canvas.draw_circle((rightWidth, topHeight), topHeight, 1, "Yellow", "Yellow")
        canvas.draw_circle((rightWidth*0.85, topHeight*0.85), topHeight*0.12, 2, "Black","Black")
        canvas.draw_circle((rightWidth*0.85, topHeight*0.81), topHeight*0.12, 2, "Yellow","Yellow")
        canvas.draw_circle((rightWidth*1.1,topHeight*0.85),topHeight*0.12,2,"black","black")
        canvas.draw_circle((rightWidth*1.1,topHeight*0.81), topHeight*0.12, 2, "Yellow","Yellow")
        canvas.draw_circle((rightWidth*0.92, topHeight*1.25), topHeight*0.12, 2, "Black","Black")
        #zzz
        canvas.draw_line((width/2.4,height/3),(width/2, height/3), 3, "Blue")
        canvas.draw_line((width/2.4, height/3),(width/2, height/3.3), 3, "Blue")
        canvas.draw_line((width/2, height/3.3),(width/2.4, height/3.3), 3, "Blue")
       
        canvas.draw_line((width/1.7, height/4),(width/1.5, height/4), 3, "Blue")
        canvas.draw_line((width/1.7, height/4),(width/1.5, height/5), 3, "Blue")
        canvas.draw_line((width/1.5, height/5),(width/1.7, height/5), 3, "Blue")
    if face3:
        canvas.draw_circle((width/2, height/2), width/2 - 50, 10, "orange", "orange")
        canvas.draw_circle((width/2 - 100, height/2 - 100), 25, 2, "Black", "Black")
        canvas.draw_circle((width/2 + 100, height/2 - 100), 25, 2, "Black", "Black")
        canvas.draw_line((width/3, height/2 + 170), (width - width/3, height/2 + 100), 10, "Black")  
        canvas.draw_line((width - width/3, height/2 + 170), (width/3, height/2 + 100), 10, "Black")
    if face4:
        canvas.draw_circle((width/2, height/2), width/2 - 50, 10, "white", "Yellow")
        canvas.draw_circle([width/2.75, height/2 - 100], 10 , 10, "Black", "White")
        canvas.draw_circle([width-150, height/2 - 100], 10 , 10, "Black", "White")
        canvas.draw_line((width/2, height/2 - 150),(width/4, height/2 - 125), 5, "Black")
        canvas.draw_line((width - width/30, height/2 - 150),(width - width/3 - 50, height/2 - 125), 5, "Black")
        canvas.draw_polygon([(width/2, height - height/5), (width - 70, height - height/4 + 25), (width/2 - 10, height - height/4 - 60), (width/2 + 10, height - height/4 - 30), (width/2, height - height/4 + 25)],10, "orange", "orange")
        canvas.draw_circle((164, 284), 35, 5, "pink", 'pink')
        
frame = simplegui.create_frame("Pictures", width, height) 

frame.set_draw_handler(draw)
frame.add_button("Top Left", toggle_topLeft, 100)
frame.add_button("Top Right", toggle_topRight, 100)
frame.add_button("Bottom Left", toggle_bottomLeft, 100)
frame.add_button("Bottom Right", toggle_bottomRight, 100)

# Frame Start
frame.start()

from graphics import *
from parser 
def hUD(speed, batteryLevel,DistanceTraveled):
    win = GraphWin("My Circle", 800, 480)

    speed = Text(Point(400,240), "20MPH")
    battery = Text(Point(700,25),"Battery Level 50%")
    speed.setSize(25)
    battery.setSize(15)
    speed.draw(win)
    battery.draw(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

while(true){
    hUD()
}

import curses
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)

screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(38,False)
                GPIO.output(40,True)
            elif char == curses.KEY_DOWN:
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(38,True)
                GPIO.output(40,False)
            elif char == curses.KEY_RIGHT:
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(38,False)
                GPIO.output(40,True)
            elif char == curses.KEY_LEFT:
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(38,True)
                GPIO.output(40,False)
            elif char == 10:
                GPIO.output(7,False)
                GPIO.output(11,False)
                GPIO.output(38,False)
                GPIO.output(40,False)
             
finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
    

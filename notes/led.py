from migen import *

if __name__ == "__main__":
  led = Signal() # by default size is 1 bit
  counter = Signal(4) # 4 bit counter
  button = Signal()

# assignment
# whenever the button is pressed, the led will glow

led.eq(button)
# assignment is done with the keyword eq
# this above statement is a fragment

# getting familiar with if/ elif / else

#case1
If(button == 1, led.eq(1)).Else(led.eq(0))

#case2
If(button == 1, led.eq(1)).Elif(button == 0, led.eq(0))

# creating multiple signals

leds = [Signal() for _ in range(8)]

buttons = [Signal() for _ in range(8)]

table = []

for i in range(8):
  table.append(leds[i].eq(buttons[i]))


#print(yield table) # this is wrong way
# Q) where can we use yield?
print (table)

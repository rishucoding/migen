from migen import *

"""
blinky:
a module with a led, that blinks and freq of 
blinking can be controlled. 
"""

class Blinky(Module):
  def __init__(self):
    self.led = led = Signal()
    self.counter = counter = Signal(3)

    self.sync += counter.eq(counter+1)
    self.comb += led.eq(counter[2])

# creating a testbench

def blink_test(dut):
  for i in range(20):
    x = yield dut.counter
    print("{} {}".format(bin(x,4), (yield dut.led)))
    yield

# a module is seen as a generator of a design
# dut is design under test.. which is passed into the run_simulation in main

# yield increases the clock cycle by 1
# yield is also used to get/set the values in dut

dut = Blinky()
run_simulation(dut, blink_test(dut), vcd_name='blinky.vcd')





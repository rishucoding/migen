from migen import *

# a counter which increments every cycle
class Counter(Module):
  def __init__(self):
    self.count = Signal(4)

    self.sync += self.count.eq(self.count + 1)

# a function to test the counter
def counter_test(dut, count=20):
  for i in range(count):
    print ((yield dut.count)) #read and print
    yield 

if __name__ == "__main__":
  dut = Counter() # create an object
  run_simulation(dut, counter_test(dut), vcd_name='basic1.vcd')



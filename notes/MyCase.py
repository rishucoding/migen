from migen import *

class MyFHDL(Module):
  def __init__(self):
    self.foo = foo = Signal(8)
    prime = [2,3,5,7,11,13,17,19] #list of prime numbers
    counter = Signal(3)

    cases = {} # set type

    for i in range(8):
      cases[i] = foo.eq(prime[i])

    self.sync += counter.eq(counter + 1)
    self.comb += Case(counter, cases)

def testbench(dut):
  for i in range(32):
      print((yield dut.foo)) # always enclose yield stmts in brackets
      yield
# by running this for loop for 32 times, i am having 32 clock cycles
      # in each clock, the counter value increases.. thus a different case
# and thus a different value of foo is printed


dut = MyFHDL() # OBJECT of our design
run_simulation(dut, testbench(dut), vcd_name = 'case.vcd')


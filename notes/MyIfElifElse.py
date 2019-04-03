from migen import *

class MyFHDL(Module):
  def __init__(self):
    self.foo = foo = Signal(8)
    self.bar = bar = Signal(8) #8bits

    self.comb += [
      If(foo <5,
        bar.eq(1)
      ).Elif(foo == 5,
        bar.eq(2)
      ).Elif(foo == 6,
        bar.eq(3)
      ).Else(
        bar.eq(4)
      )
    
    
    ]

def testbench(dut):
  for i in range(10):
    yield dut.foo.eq(i)
    yield
    print("foo: {}, bar: {}".format( i, (yield dut.bar)))
#NOTE: always put arguments in brackets in format, else error

dut = MyFHDL()
run_simulation(dut, testbench(dut), vcd_name="ifelse.vcd")

from migen import *

# idea is that a module can import another module

class MyAdder(Module):
  def __init__(self,width):
    self.a = a = Signal(width)
    self.b = b = Signal(width)

    self.result = result = Signal(width + 1)

    self.comb += result.eq(a+b)

class MyTop(Module):
  def __init__(self):
    self.inp = inp = Signal(8) # 8bits input

    # call the adder module

    adder = MyAdder(8)
    # add the module to the submodules list

    self.submodules +=adder
    
    self.res = adder.result

    self.comb +=[adder.a.eq(inp), 
                adder.b.eq(3)]

def testbench(dut):
  for i in range(10):
    yield dut.inp.eq(i)
    yield
    print("{} {}".format(i, (yield dut.res)))


dut = MyTop()
run_simulation(dut, testbench(dut), vcd_name='adder.vcd')

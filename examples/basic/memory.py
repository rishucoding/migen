from migen.fhdl.structure import Fragment
from migen.fhdl.specials import Memory
from migen.fhdl.module import Module
from migen.fhdl import verilog

class Example(Module):
	def __init__(self):
		self.specials.mem = Memory(32, 100, init=[5, 18, 32])
		p1 = self.mem.get_port(write_capable=True, we_granularity=8)
		p2 = self.mem.get_port(has_re=True, clock_domain="rd")
		self.ios = {p1.adr, p1.dat_r, p1.we, p1.dat_w,
			p2.adr, p2.dat_r, p2.re}

example = Example()
print(verilog.convert(example, example.ios))

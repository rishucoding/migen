from migen import *
from migen.fhdl import verilog
"""
1. making a table for mapping (0,1,2,...,E,F) -> seven segment led on
2. hexa is a simple integer from (0 to 15)
3. abcdefg is the corresponding 7 bit led code mapped in table
4. we use cases to identify led code for a given input hexa. 
""" 
class sevenseg_ctrl(Module):
    def __init__(self):
        self.abcdefg = abcdefg = Signal(7)
        self.hexa = hexa = Signal(4)
        table = [
            0x3f, 0x06, 0x5b, 0x4f, 
            0x66, 0x6d, 0x7d, 0x07, 
            0x7f, 0x6f, 0x77, 0x7c, 
            0x39, 0x5e, 0x79, 0x71
            ]
 
        cases = {}
        for i in range(16):
            cases[i] = abcdefg.eq(table[i])
 
        self.comb += Case(hexa, cases)

"""
1. This function prints the led pattern
2. It prints line by line, first line being A led, second line (F,G,B) led
and third line (E,D,C) led.
3. eg: let's say the hexa = 0. This means 'abcdefg' code is '011 1111' in hex. 
TODO: understand this encoding!.
"""
def display_seven(val):
    line0 = ["   ", " _ "]
    line1 = ["   ", "  |", " _ ", " _|", "|  ", "| |" , "|_ ", "|_|"]
    a = val&1;
    fgb = ((val >> 1) & 1) | ((val >> 5) & 2) | ((val >> 3) & 4)
    edc = ((val >> 2) & 1) | ((val >> 2) & 2) | ((val >> 2) & 4)
    print(line0[a])
    print(line1[fgb])
    print(line1[edc])
 
def sevseg_tb(dut):
    for i in range(16):
        yield dut.hexa.eq(i)
        yield
        display_seven((yield dut.abcdefg))
# call design to display each number 
 
dut = sevenseg_ctrl()
print(verilog.convert(dut,{dut.hexa, dut.abcdefg}))
#run_simulation(dut, sevseg_tb(dut))

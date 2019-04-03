"""
A module is a migen class, has two things: 
  1. a table for synchronous fragments
  2. a table for combinatory fragments

"""
from migen import *
class MyModule(Module):
  def __init__(self):
    led1 = Signal()
    led2 = Signal()
    button = Signal()
    # signals in our design

    self.comb += led1.eq(button) # asynchronous logic
    self.sync += led2.eq(~led2) # synchronous logic
    # fragments making the logic


"""
//corresponding verilog code

module top(
        output led1,
        output reg led2,
        input button,
        input sys_clk,
        input sys_rst
);

assign led1 = button;
always @(posedge sys_clk) begin
      led2 <= (~led2);
      if(sys_rst) begin
        led2 <= 1'd0; //
        end
"""

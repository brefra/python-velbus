"""
@author: Thomas Delaet <thomas@delaet.org>
"""
import velbus

COMMAND_CODE = 0xed

class ModuleStatusMessage(velbus.Message):
	"""
	send by: VMB6IN
	received by:
	"""	
	def __init__(self):
		velbus.Message.__init__(self)
		self.closed = []
		self.led_on = []
		self.led_slow_blinking = []
		self.led_fast_blinking = []
		
	def populate(self, priority, address, rtr, data):
		"""
		@return ""
		"""
		assert isinstance(data, str)
		self.needs_low_priority(priority)
		self.needs_no_rtr(rtr)
		self.needs_data(data, 4)
		self.set_attributes(priority, address, rtr)
		self.closed = self.byte_to_channels(data[0])
		self.led_on = self.byte_to_channels(data[1])
		self.led_slow_blinking = self.byte_to_channels(data[2])
		self.led_fast_blinking = self.byte_to_channels(data[3])
			
	def data_to_binary(self):
		"""
		@return: str
		"""
		return chr(COMMAND_CODE) + self.channels_to_byte(self.closed) + \
			self.channels_to_byte(self.led_on) + \
			self.channels_to_byte(self.led_slow_blinking) + \
			self.channels_to_byte(self.led_fast_blinking)
					
velbus.register_command(COMMAND_CODE, ModuleStatusMessage)
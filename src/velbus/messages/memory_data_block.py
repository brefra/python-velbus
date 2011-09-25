"""
@author: Thomas Delaet <thomas@delaet.org>
"""
import velbus

COMMAND_CODE = 0xcc

class MemoryDataBlockMessage(velbus.Message):
	"""
	send by: VMB6IN, VMB4RYLD
	received by:
	"""	
	def __init__(self):
		velbus.Message.__init__(self)
		self.high_address = 0x00
		self.low_address = 0x00
		self.data = ""
		
	def populate(self, priority, address, rtr, data):
		"""
		@return ""
		"""
		assert isinstance(data, str)
		self.needs_low_priority(priority)
		self.needs_no_rtr(rtr)
		self.needs_data(data, 6)
		self.set_attributes(priority, address, rtr)
		self.high_address = ord(data[0])
		self.low_address = ord(data[1])
		self.data = data[2:]
			
	def data_to_binary(self):
		"""
		@return: str
		"""
		return chr(COMMAND_CODE) + chr(self.high_address) + \
					chr(self.low_address) + self.data
					
velbus.register_command(COMMAND_CODE, MemoryDataBlockMessage)
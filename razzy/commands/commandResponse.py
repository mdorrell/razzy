class CommandResponse():
  CODE_EXIT = 0
  CODE_OK = 200
  
  def __init__(self,code, message):
    self.code = code
    self.message = message

  @property
  def code(self):
    return self.__code

  @code.setter
  def code(self, val):
    self.__code = val

  @property
  def message(self):
    return self.__message

  @message.setter
  def code(self, val):
    self.__message = val
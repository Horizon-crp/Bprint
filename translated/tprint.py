from threading import Thread; from sys import stdout; from typing import Optional
def tprint(*values, sep: Optional[str] = ' ', end: Optional[str] = '\n', File = stdout, flush: bool = False):
  '''
  The threading version of print
  '''
  sep = str(sep); e: str = ''
  for i in values: e += str(i) + sep
  e += end
  if flush is False:
    def write():
      File.write(e)
  else:
    def write():
      File.write(e); flush()
  Thread(target=write).start(); return None

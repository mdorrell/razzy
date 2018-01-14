from commands import *
from razzy import Razzy

import sys
import os

# Load razzy 
razzy  = Razzy()

try:
  doContinue = True;

  commands = globals()

  # Initialize razzy
  razzy.init(commands)
  while doContinue:
    
    # Each loop listens for a command and processes it
    doContinue = razzy.run()

finally:
  # Shutdown properly
  razzy.shutdown()

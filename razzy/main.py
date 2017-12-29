from commands import *
from razzy import Razzy

import sys
import os

# Load razzy 
razzy  = Razzy()

try:
  # Initialize razzy
  razzy.init()
  while True:
    
    # Each loop listens for a command and processes it
    razzy.run()

finally:
  # Shutdown properly
  razzy.shutdown()

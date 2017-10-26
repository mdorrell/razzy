__all__ = []

import pkgutil
import inspect

# Define COMMANDS array
COMMANDS = {}

for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(name).load_module(name)

    for name, value in inspect.getmembers(module):
        if name.startswith('__'):
            continue

        # Allows us to import all modules in commands folder at once
        globals()[name] = value
        __all__.append(name)
          
        # get all classes in folder except CommandBase  
        if hasattr(value, '__bases__'):
          if name != "CommandBase":
            try:
              keywords = value.getKeywords(value)
              COMMANDS[name] = keywords
            except AttributeError:
              pass
                        

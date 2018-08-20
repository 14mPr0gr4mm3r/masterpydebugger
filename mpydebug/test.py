from debugger import *

debugger = MasterDebugger()
print(debugger.getLevels())
debugger.setNewLevel('IMPORTANT', 4)
print(debugger.getLevels())
debugger.debug('Hello', level=4)

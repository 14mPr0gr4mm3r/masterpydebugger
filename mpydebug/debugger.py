"""
MasterPyDebugger ©2018
@author: Gustavo-Sampaio (14mPr0gr4mm3r)
G28S11T20S03
"""
import sys
from datetime import datetime
version = '0.1'
init = "Welcome, user! You're using now the MasterPyDebugger!"

class MasterDebugger():
    def __init__(self):
        """
        The default format of debugging message is defined, so!
        """
        self.LEVELSTRENGTH = [1, 2, 3]
        self.LEVELS = ['INFO', 'WARNING', 'ERROR']
        self.DEFAULTFORMAT = '{}: [{}] {}'
        return None
    def getLevels(self):
        return self.LEVELS, self.LEVELSTRENGTH
    def setNewLevel(self, newlevelname:str, levelstrength:int):
        if (levelstrength > 3):
            try:
                self.LEVELS.append(newlevelname)
                self.LEVELSTRENGTH.append(levelstrength)
            except Exception as e:
                print(e)
        else:
            print(f'You cannot use "{levelstrength}" level strength')
            sys.exit()
    def debug(self, msg, path_filename=None, formatation='{}: [{}] {}', level='INFO', method='console'):
        """
        Obviously, there are several arguments here! The most of them are already defined. And here, you can, finally, debug your app!
        """
        if method == 'console' and path_filename == None:
            if (formatation == self.DEFAULTFORMAT):
                if type(level) is int:
                    print(formatation.format(self.LEVELS[self.LEVELSTRENGTH.index(level)], datetime.today(), msg))
                else:
                    print(formatation.format(level, datetime.today(), msg))
            else:
                print(f'{formatation}')
        elif method == 'localfile' and path_filename != None:
            try:
                if (formatation == self.DEFAULTFORMAT):
                    open(path_filename, 'a').write(formatation.format(level, datetime.today(), msg))
                else:
                    open(path_filename, 'a').write(f'{formatation}')
            except FileNotFoundError:
                print('This path or filename is incorrect')
                sys.exit()

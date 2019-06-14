import os, sys
mypackage_path = os.path.abspath(os.getcwd() + '\..' + '\mypackage')
sys.path.append( mypackage_path )
from GameCards98 import GameCards98


app = GameCards98()

app.start_game()
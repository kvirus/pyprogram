import glob
import os
import shutil
dist = "D:/1C"
for i in glob.glob('//anny/IT_INFRASTR/BD/6.ASystem/*2022_04*.*'):
    print(i)
    shutil.copy(i,dist)
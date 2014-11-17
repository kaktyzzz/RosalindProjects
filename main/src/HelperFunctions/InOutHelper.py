import platform
import os

dirPathLst = ['..', '..','InOut']
# dirPathLst = ['..', 'InOut']
type = '.txt'
outPrefix = '_out'
dirPath = ''.join(s + os.sep for s in dirPathLst);
dirPath = os.sep + dirPath

def getFullPathInput(fileName):
    return os.path.dirname(__file__) + dirPath + fileName + type

def getFullPathOutput(fileName):
    return os.path.dirname(__file__) + dirPath + fileName + outPrefix + type

def getFullPathOther(fileName):
    return os.path.dirname(__file__) + os.sep + fileName
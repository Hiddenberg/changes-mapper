import json
import sys
import os
import hashlib

BUFFER_SIZE = 65536

md5 = hashlib.md5()


def addDirSlash(dirName):
   #↓ using ternary operation to add a "/" at the end if the path doesnt have it
   slashDir = dirName if dirName[-1] == "/" else dirName+"/"
   return slashDir

def scannRecursive(initialPath):
   if os.path.exists(initialPath):
      if os.path.isdir(initialPath):
         initialPath = addDirSlash(initialPath) 
      else:
         print("Initial path MUST be a directory")
         return
   else:
      print("Path provided does not exist")
      return

   nextDirsToScan = None
   pathFiles = []
   pathDirs = []
   while True:
      # If theres are no previous directories to scan start with the initial path
      if nextDirsToScan == None:
         nextDirsToScan = [initialPath]
      elif isinstance(nextDirsToScan,list) and len(nextDirsToScan) == 0:
         break

      pathSubdirs = []
      folders = []
      files = []
      for dir in nextDirsToScan:
         pathContents = os.listdir(dir)

         for thing in pathContents:
            thingFullPath = dir+thing

            if os.path.isdir(thingFullPath):
               thingFullPath = addDirSlash(thingFullPath)
               pathDirs.append(thingFullPath)
               folders.append(thing)

            elif os.path.isfile(thingFullPath):
               pathFiles.append(thingFullPath)
               files.append(thing)

         print("scanned path: " + dir)
         print("folders: ")
         print(folders)
         print("files: ")
         print(files)
         print("+++++++++++++++++++++++++++++++++++\n")

         pathSubdirs.extend(pathDirs)

         pathDirs.clear()
         pathFiles.clear()
      nextDirsToScan = pathSubdirs




def checkAndGetPath():
   if len(sys.argv) == 1:
      print("You must provide a initial directory to start scanning")
      exit()
   else:
      return sys.argv[1]

providedPath = checkAndGetPath()
scannRecursive(providedPath)
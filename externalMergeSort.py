#!/bin/bash
import os
import tempfile
import heapq


class externamMergeSort:

 """ Splits the large file into small files ,sort the small files and uses python
     heapq module to merge the different small sorted files.  Each sorted files is 
     loaded as a  generator ,hence won't loads entire data into memory """

 def __init__(self):
  self.fileHandlerList = [] 
  self.tempFileHandlerList = []
  self.getCurrentDir()

 def getCurrentDir(self):
  self.cwd = os.getcwd()

 def iterateSortedData(self,sortedCompleteData):
  for no in sortedCompleteData:
   print no

 """ Kway  merge the small sorted files using python heapq module """
 def sorttempFiles(self):
   mergedNo = (map(int,tempFileHandler) for tempFileHandler in self.tempFileHandlerList) #it's a generator, so never loads into memory
   sortedCompleteData=heapq.merge(*mergedNo)
   return sortedCompleteData

 """ Split the large files into small sorted files Uses tempfile module .
     Stores the file handle of each small file  into tempFileHandlerList """
 def splitFiles(self,largeFileName,smallFileSize):
   largeFileHandler = open(largeFileName)
   tempBuffer = []
   size = 0
   while True:
     number=largeFileHandler.readline()   
     if not number:
       break
     tempBuffer.append(number)
     size+=1
     if size%smallFileSize == 0:
       tempBuffer=sorted(tempBuffer,key=lambda no:int(no.strip()))
       tempFile=tempfile.NamedTemporaryFile(dir=self.cwd+"/temp",delete=False)
       tempFile.writelines(tempBuffer)
       self.tempFileHandlerList.append(tempBuffer)
       tempBuffer=[]

if __name__ == "__main__":
  largeFileName = 'largefile'
  smallFileSize = 10
  obj = externamMergeSort()
  obj.splitFiles(largeFileName,smallFileSize)
  sortedCompleteData = obj.sorttempFiles()
  obj.iterateSortedData(sortedCompleteData)


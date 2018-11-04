#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import tempfile
import heapq
import sys


class heapnode:

    def __init__(
        self,
        item,
        index,
        fileHandler,
        ):
        self.item = item
        self.index = index
        self.fileHandler = fileHandler


class heaprr:

    def __init__(self):
        self.list = []


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

    def iterateSortedData(self, sortedCompleteData):
        for no in sortedCompleteData:
            print no

    def sorttempFiles(self):
        mergedNo = (map(int, tempFileHandler) for tempFileHandler in
            self.tempFileHandlerList)  # it's a generator, so never loads into memory
        sortedCompleteData = heapq.merge(*mergedNo)
        return sortedCompleteData

    def heapify(
        self,
        arr,
        i,
        n,
        ):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left].item < arr[i].item:
            smallest = left
        else:
            smallest = i

        if right < n and arr[right].item < arr[smallest].item:
            smallest = right

        if i != smallest:
            (arr[i], arr[smallest]) = (arr[smallest], arr[i])
            self.heapify(arr, smallest, n)

    def construct_heap(self, arr):
        l = len(arr) - 1
        mid = l / 2
        while mid >= 0:
            self.heapify(arr, mid, l)
            mid -= 1

    def sorttempFiles_low_level(self):
        list = []
        sorted_output = []
        for tempFileHandler in self.tempFileHandlerList:
            item = int(tempFileHandler.readline().strip())
            list.append(heapnode(item, 0, tempFileHandler))

        self.construct_heap(list)
        while True:
            min = list[0]
            if min.item == sys.maxint:
                break
            index = min.index
            sorted_output.append(min.item)
            fileHandler = min.fileHandler
            item = fileHandler.readline().strip()
            if not item:
                item = sys.maxint
            else:
                item = int(item)
            list[0] = heapnode(item, index + 1, fileHandler)
            self.heapify(list, 0, len(list))
        return sorted_output

    def splitFiles(self, largeFileName, smallFileSize):
        largeFileHandler = open(largeFileName)
        tempBuffer = []
        size = 0
        while True:
            number = largeFileHandler.readline()
            if not number:
                break
            tempBuffer.append(number)
            size += 1
            if size % smallFileSize == 0:
                tempBuffer = sorted(tempBuffer, key=lambda no: \
                                    int(no.strip()))
                tempFile = tempfile.NamedTemporaryFile(dir=self.cwd
                        + '/temp', delete=False)
                tempFile.writelines(tempBuffer)
                tempFile.seek(0)
                self.tempFileHandlerList.append(tempFile)
                tempBuffer = []


if __name__ == '__main__':
    largeFileName = 'largefile'
    smallFileSize = 10
    obj = externamMergeSort()
    obj.splitFiles(largeFileName, smallFileSize)
    print obj.sorttempFiles_low_level()

 # sortedCompleteData = obj.sorttempFiles()
#  obj.iterateSortedData(sortedCompleteData)

			

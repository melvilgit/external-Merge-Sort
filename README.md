# External MergeSort in Python

  Implemented *Pythonic* way as well as *low level native External Merge Sort*
  
  **Problem Stement** </br>
  All Sorting Algorithm works within the RAM .When the data to be  sorted does not fit into the RAM and      instead they   resides in the slower external memory (usually a hard drive) , this technique is used .
Example , If we  have to Sort 100 numbers with each number 1KB and our RAM size is 10KB ,external merge sort works like a charm !.

**How to ?**

> Split Phase
* Split the 100 KB file into 10 files each 10kb
* Sort the 10KB files using some efficient Sorting Algo in O(nlogn)
* Stores each of the smaller files to disk .

> Merge Phase
* Do a [K-way merge](https://en.wikipedia.org/wiki/K-way_merge_algorithm)  with each smaller files one by one. Inline the details .
* After the Split Phase , A list of file handler of all the splitted files will be stored - **sortedTempFileHandlerList**
* We create a list of heapnode - **heapnodes**. Each heapnode will  stores the actual entry and also the file which owns it . The heapnodes is heapified and it will be a min-heap.
* Assuming there 10 files , heapnodes will takes 10KB only (each number assume 1KB) .
   - Loop While Least Element is **INT_MAX**
     * Picks the heapnode with least element from heapnodes . ( 0(1) since it's a min heap )
     * Write the element to  **sortedLargeFile** (it will be the sorted number)
     * Find the *filehandler* of the corresponding element by looking at heapnode.filehandler .
     *  Read the next item from the file . If it's **EOF**, mark the  item as **INT_MAX**  
     *  Put the item to heap top . Again Heapify to persist min heap property .
     *  *Continue ;*
      
* At the end of the Merge Phase **sortedLargeFile** will have all the elements in sorted  order .




   
  

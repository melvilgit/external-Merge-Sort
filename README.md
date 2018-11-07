# External MergeSort in Python

  Implemented *Pythonic* way as well as *low level native External Merge Sort*
  
  **Problem Stement** </br>
  All Sorting Algorithm works within the RAM .When the data to be  sorted does not fit into the RAM and      instead they   resides in the slower external memory (usually a hard drive) , this technique is used .
Example , If we  have to Sort 100 numbers with each number 1KB and our RAM size is 10KB ,[external merge sort](https://en.wikipedia.org/wiki/External_sorting) works like a charm !.

**How to ?**

> Split Phase
* Split the 100 KB file into 10 files each 10kb
* Sort the 10KB files using some efficient Sorting Algo in O(nlogn)
* Stores each of the smaller files to disk .

> Merge Phase
* Do a [K-way merge](https://en.wikipedia.org/wiki/K-way_merge_algorithm)  with each smaller files one by one. Inline the details .
* After the Split Phase , A list of file handler of all the splitted files will be stored - **sortedTempFileHandlerList**
* Now, We creates a list of heapnode - **heapnodes**. Each heapnode will  stores the actual entry read from the file and also the file which owns it . The heapnodes is heapified and it will be a min-heap.
* Assuming there 10 files , heapnodes will takes 10KB only (each number assume 1KB) .
   - Loop While Least Element  (the top of heap ) is **INT_MAX**
     * Picks the node with least element from heapnodes  . ( 0(1) since heapnodes is a min heap )
     * Write the element to  **sortedLargeFile** (it will be the sorted number)
     * Find the *filehandler* of the corresponding element by looking at heapnode.filehandler .
     *  Read the next item from the file . If it's **EOF**, mark the  item as **INT_MAX**  
     *  Put the item to heap top . Again Heapify to persist min heap property .
     *  *Continue ;*
      
* At the end of the Merge Phase **sortedLargeFile** will have all the elements in sorted  order .
 
## Example </br>
Say We have a file largefile with the following Contents 

5 8 6 3 7 1 4 9 10 2

In Split Phase ,We Split them into the   Sorted chunks in 5 separate temp files.

temp1 - 5 ,8   &nbsp;&nbsp; temp2 - 3 ,6      &nbsp;&nbsp;  temp3 - 1, 7 &nbsp;&nbsp;  temp4 -4 , 9  &nbsp;&nbsp; temp5 - 2 ,10 

Next Construct a Min Heap with top element from each files
                       
                             1                       *
                           /  \
                          2    5
                        /  \                         *
                       4    3     

Now picks the least Element from the min heap and write it to sortedOutputFile - *1*. </br>
Finds the next element of the file which owns   min element *1* . </br>
The no is *7* from temp3 . Move  it to heap.

          7                                    2
        /  \                                 /  \
       2     5      Heapify -->             3    5	
      /  \                                 / \
     4    3                               4   7 
Picks the least element  *2* and moves it to  sortedOutputFile - *1 2*. </br>
Finds the next element of the file which owns   min element *2* . </br>
The no is *10* from temp5 . Move  it to heap.

          10                                   3
        /  \                                 /  \
       3     5      Heapify -->             4    5	
      /  \                                 / \
     4    7                               10   7 
Picks the least element  *3* and moves it to  sortedOutputFile - *1 2 3*. </br>
Finds the next element of the file which owns   min element *3* . </br>
The no is *6* from temp2 . Move  it to heap.

          6                                   4
        /  \                                 /  \
       4     5      Heapify -->             6    5	
      /  \                                 / \
    10   7                               10   7 
Picks the least element  *4* and moves it to  sortedOutputFile - *1 2 3 4*. </br>
Finds the next element of the file which owns   min element *4* . </br>
The no is *9* from temp4 . Move  it to heap.

          9                                   5
        /  \                                 /  \
       6     5      Heapify -->             6    9	
      /  \                                 / \
    10   7                               10   7 

Picks the least element  *5* and moves it to  sortedOutputFile - *1 2 3 4 5*. </br>
Finds the next element of the file which owns   min element *5*. </br>
The no is *8* from temp1 . Move  it to heap

          8                                   6
        /  \                                 /  \
       6     9      Heapify -->             7    9	
      /  \                                 / \
    10   7                               10   8 

Picks the least element  *6* and moves it to  sortedOutputFile - *1 2 3 4 5 6* . </br>
Finds the next element of the file which owns   min element *5*  . . </br>
<b> We have see EOF . So mark the read no as  <i>INT_MAX </i></b>  . </br>

       INT_MAX                                 7
        /  \                                 /  \
       7    9      Heapify -->              8     9	
      /  \                                 / \
    10   8                               10   INT_MAX
Picks the least element  *6* and moves it to  sortedOutputFile - *1 2 3 4 5 6 7* . </br>
If we loop this process , we would reaches a point where , the heap would looks like below 
and the </br> sortedOutputFile - *1 2 3 4 5 6 7 8 9 10*  . </br>We  would also breaks at this point when the min element from heap becomes *INT_MAX* .

                           INT_MAX                       
                            /   \
                        INT_MAX  INT_MAX
                        /    \                         
                     INT_MAX INT_MAX        

                 




   
  

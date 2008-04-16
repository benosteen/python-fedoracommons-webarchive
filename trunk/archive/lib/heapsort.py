"""
A basic Heap sort, based on pseudo code (see end) found on Wikipedia, and via the related links. 

Usage:
(Change lib for whatever location this script is in, in this case lib/heapsort.py)
>>> from lib.heapsort import HeapSort
>>> h = HeapSort()
>>> n = []
>>> for i in xrange(0,100):
...     n.append(randint(1,10000))
... 
>>> n
[6357, 3522, 5848, 7113, 3753, 9544, 8846, 1467, 9283, 9132, 5568, 1835, 3008, 107, 132, 3835, 7465, 5041, 3558, 543, 8817, 6198, 480, 1774, 782, 6263, 5409, 1461, 7098, 9399, 9332, 1530, 4341, 1173, 47, 3677, 668, 1788, 7760, 4958, 3421, 7045, 9213, 6269, 3784, 7934, 8814, 8656, 962, 7178, 7390, 7305, 3471, 9214, 8567, 4471, 3861, 6372, 182, 6034, 2509, 3486, 2337, 8317, 2954, 5078, 8189, 9412, 4531, 1684, 3633, 230, 7424, 2335, 1610, 366, 6157, 1811, 2374, 2339, 1399, 3267, 1050, 5189, 2061, 1782, 6862, 4403, 1513, 4050, 690, 6163, 6922, 6970, 9037, 6176, 1612, 3469, 9869, 7807]
>>> h.HeapSort(n)
>>> n
[47, 107, 132, 182, 230, 366, 480, 543, 668, 690, 782, 962, 1050, 1173, 1399, 1461, 1467, 1513, 1530, 1610, 1612, 1684, 1774, 1782, 1788, 1811, 1835, 2061, 2335, 2337, 2339, 2374, 2509, 2954, 3008, 3267, 3421, 3469, 3471, 3486, 3522, 3558, 3633, 3677, 3753, 3784, 3835, 3861, 4050, 4341, 4403, 4471, 4531, 4958, 5041, 5078, 5189, 5409, 5568, 5848, 6034, 6157, 6163, 6176, 6198, 6263, 6269, 6357, 6372, 6862, 6922, 6970, 7045, 7098, 7113, 7178, 7305, 7390, 7424, 7465, 7760, 7807, 7934, 8189, 8317, 8567, 8656, 8814, 8817, 8846, 9037, 9132, 9213, 9214, 9283, 9332, 9399, 9412, 9544, 9869]

Works with any python object that overloads the '>' operator, via __gt__. For example, an object like
datetime.
"""
class HeapSort(object):
    def Left(self, i): return 2*i
    def Right(self, i): return 2*i+1

    def siftDown(self, heap_list, i, n): 
        # get the left and right index values:
        l,r = self.Left(i), self.Right(i)
        
        # Basic comparison 
        if l <= n and heap_list[l] > heap_list[i]:
            index_of_max_value = l
        else:
            index_of_max_value = i
            
        if r <= n and heap_list[r] > heap_list[index_of_max_value]:
            index_of_max_value = r
            
        if index_of_max_value != i:
            heap_list[i], heap_list[index_of_max_value] = heap_list[index_of_max_value], heap_list[i]
            self.siftDown(heap_list, index_of_max_value, n)

    # python's len built-in function returns the number of items. heap_lists the indexes start at
    # 0, the last item has an index of len(heap_list)-1, which is what this function is after.
    def HeapLength(self, heap_list): return len(heap_list)-1
    
    def BuildHeap(self, heap_list): # build a heap heap_list from an unsorted array
        n = self.HeapLength(heap_list)
        # pseudocode: for i <- |length[A]/2| downto 1st item
        for i in range(n/2,-1,-1):
            self.siftDown(heap_list,i,n)

    def HeapSort(self, heap_list): # use a heap to build sorted array from the end
        """
        Based on pseudo-code found for performing a HeapSort. 
        """
        # Make the list ordered like a 'heap'
        self.BuildHeap(heap_list)
        
        HeapSize=self.HeapLength(heap_list)
        # pseudocode: for i <- length[A] downto 2nd item
        for i in range(HeapSize,0,-1):
            # swap the largest item (at index 1) with the 'end' of the array at i
            heap_list[0],heap_list[i]=heap_list[i],heap_list[0]
            HeapSize=HeapSize-1 # shrink heap size by 1 to get next largest element
            self.siftDown(heap_list,0,HeapSize)


"""
[NB I had to jigger with the left/right functions, as well as the looping limits to make it work
with python's 0...n-1 indexing scheme, because I believe the pseudocode and the prefacing text don't
actually use the same indexing scheme... don't blame me, it's taken from online lecture notes at: 
http://www.softpanorama.org/Algorithms/Sorting/heapsort.shtml]

The heapsort algorithm uses the data structure called the heap. A heap is defined as a complete binary tree in which each node has a value greater than both its children (if any). Each node in the heap corresponds to an element of the array, with the root node corresponding to the element with index 0 in the array. Considering a node corresponding to index i, then its left child has index (2*i + 1) and its right child has index (2*i + 2). If any or both of these elements do not exist in the array, then the corresponding child node does not exist either. Note that in a heap the largest element is located at the root node. The code for the algorithm is:

    Heapify(A, i){
        l <- left(i)
        r <- right(i)
        if l <= heapsize[A] and A[l] > A[i]
            then largest <- l
            else largest <- i
        if r <= heapsize[A] and A[r] > A[largest]
            then largest <- r
        if largest != i
            then swap A[i] <-> A[largest]
                Heapify(A, largest)
    }

    Buildheap(A){
        heapsize[A] <- length[A]
        for i <- |length[A]/2| downto 1
            do Heapify(A, i)
    }

    Heapsort(A){
        Buildheap(A)
        for i <- length[A] downto 2
            do swap A[1] <-> A[i]
            heapsize[A] <- heapsize[A] - 1
            Heapify(A, 1)
    } 
"""

def bubblesort(array): #function declaration 
	#expects an array  
    for ipass in range(1,len(array)-1): #iterate through array
        for i in range(len(array)-1): #iterate to find the biggest item 
            if array[i]>array[i+1]: #compare to find the bigger term 
                array[i], array[i+1] = array[i+1], array[i] # swap
    return array #rturn array (sorted)


def insertionsort(lst):#function declaration
	#expexcts an array
    for i in range (1,len(lst)): #iterate through array
        temp = lst[i] #store the 2nd item in the "temp" variable
        j=i-1 #define a variable j which is 1 less than i
        while j>=0 and lst[j] > temp: #iterate through already sorted list to find a place to keep the temp variable
        	#2 conditions are first term
        	#or the item being compared is smaller than temp
            lst[j+1]=lst[j] #move the other value along
            j=j-1 #change the value of the counter j 
        lst[j+1]=temp  #place temp in the spot it is meant to be placed in
    return lst #return array


def msort(x): #function declaration
	#expects an array 
    result = [] #defines a result array
    if len(x) < 2: #looks for a corner case in which recursion ends if sixe = 0,1
        return x #return x 
    mid = int(len(x)/2) #define the midpoint
    y = msort(x[:mid]) #sort right half through recursion
    z = msort(x[mid:]) #sort left half through recursion
    while (len(y) > 0) or (len(z) > 0): #while loop to join z and y 
        if len(y) > 0 and len(z) > 0: #if both of them have atleast 1 item
            if y[0] > z[0]: #compare the smallest items of both arrays
                result.append(z[0]) #if z[0] is smaller add it to x
                z.pop(0) #and remove it from th array
            else:
                result.append(y[0]) #else add the smallest term from y (y[0]) to resule
                y.pop(0) #and remove it from y
        elif len(z) > 0: #if only z has items
            for i in z: #loop through items in z
                result.append(i) #add them to result
                z.pop(0) #and remove them from z
        else: #if only y has items
            for i in y: #loop through items in y
                result.append(i) #add them to result
                y.pop(0) #remove them from y
    return result #return result

def partition(array, start, end):#declare partition function
	#expects the array and the start and end point of the smaller array inside it that needs to be sorted
    pivot = array[start] #declare the pivot
    low = start + 1 #declare the pointer for lower value since the first is the pivot only the second can be lower value
    high = end #declare the pointer for higher value
    while True: #run this loop till low > high
        while low <= high and array[high] >= pivot: #try to get the high value to be less than the pivot
            high = high - 1 #decreases the high pointer by 1
        while low <= high and array[low] <= pivot: #try to get low value to be higher than the pivot 
            low = low + 1 #increase the low pointer by 1
        if low > high: # if low value is greater than high then break out of this while loop
            break #command to break out of loop
        else: #else
        	array[low], array[high] = array[high], array[low] #swap the low and high value
    array[start], array[high] = array[high], array[start] #swap pivot and the value and the value that is just less than the pivoe
    return high #return the point of split
 
def quickSort(array, start, end):#declare the sorting function
	#expects the array and the start and end point of the smaller array inside it that needs to be sorted
    if start >= end: #checks for a corner case and return an empty array if there were no items at the beginning
        return #return empty array
    p = partition(array, start, end) #get the split point
    quickSort(array, start, p-1) #quicksort the left side using recursion
    quickSort(array, p+1, end) #quicksort the right part of the array
    return array #return the sorted array


def linearSearch(array, item):#declare the function
	#function expects the array and the item to be searched for
	for i in range(len(array)): #iterate through the array of items
		if item == array[i]: #check if array[i] is the item that is being searched for
			return i #return i (the index) if it is
	return False #return false if item that is being searched for isn't found


def binarySearch(array, element, start, end): #declare the binary search function
	#expects the array(sorted), the element to be searched for, the starting index and the ending index
    if start > end: #checks if start is after the end 
        return False #returns False if it is as element couldnt be found this way
    mid = (start + end) // 2 #calculate the mid value by doing integer division (2) on the sum of the end and the start
    if element == array[mid]: #check if the mid term is the objetc
        return mid #if it is return the mid index
    if element < array[mid]: #if element is less than the mid value 
        return binarySearch(array, element, start, mid-1) #then search in the left part of the array
    else: #else
        return binarySearch(array, element, mid+1, end) #else search in the right part of the array



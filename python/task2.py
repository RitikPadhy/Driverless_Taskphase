#Remove the duplicate elements of the tuple
def removeDuplicates(lst):
      
    return [t for t in (set(tuple(i) for i in lst))]
          
# Driver code
lst = [(1, 2), (5, 7), (3, 6), (1, 2)]
print(removeDuplicates(lst))

test_tup = removeDuplicates(lst)
  
# printing original tuple
print("The original tuple is : " + str(test_tup)) 
  
# Tuple elements inversions
# Using list() + sum()
int res = sum(list(test_tup))
  
# printing result 
print("The summation of tuple elements are : " + str(res)) 
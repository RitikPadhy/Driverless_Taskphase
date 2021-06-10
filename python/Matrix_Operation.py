import numpy as np
class operations
{
    def calc_inv(A)
    {
       return np.linalg.inv(A)
    }
    def calc_det(b)
    {
        print np.linalg.det(b) 
    }
    def calc_adj(index,arr)
    {
        yy=[]
    for i in range(len(arr)):
        hh=[]
        for j in range(len(arr)):
            if(i==index[0] or j==index[1]):
                pass
            else:
                hh.append(arr[i][j])
        if(hh!=[]):
            yy.append(hh)
    # yy.remove([])
    return yy
 
 
dd=[[0,4,3,5],[2,3,2,6],[3,4,5,7],[3,4,5,7]]
 
for i in range(len(dd)):
    for j in range(len(dd)):
        tm_list=remove_line(tuple([i,j]),dd)
        print((i,j),tm_list)

    }
    sys.path.append(".")
}
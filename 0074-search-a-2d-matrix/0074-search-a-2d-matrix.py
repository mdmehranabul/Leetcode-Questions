class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)

        top=0
        bottom=row-1

        while top<=bottom:
            focus_row=(top+bottom)//2

            if target>matrix[focus_row][-1]:
                top=focus_row+1
            elif target<matrix[focus_row][0]:
                bottom=focus_row-1
            else:
                break
        #print(focus_row,top,bottom)

        L,U=0,len(matrix[0])-1

        while U>=L:
            mid=L+(U-L)//2

            if target==matrix[focus_row][mid]:
                return True
            elif target>matrix[focus_row][mid]:
                L=mid+1
            else:
                U=mid-1
        return False

# Time Complexity : O(log(m)+log(n))
# Space Complexity : O(1)
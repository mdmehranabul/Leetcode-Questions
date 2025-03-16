class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        top=0
        bottom=rows-1

        while top<=bottom:
            focus_row=(top+bottom)//2
            if matrix[focus_row][0]>target:
                bottom=focus_row-1
            elif matrix[focus_row][-1]<target:
                top=focus_row+1
            else:
                break
            
        l=0
        r=len(matrix[focus_row])-1

        while l<=r:
            mid=l+(r-l)//2

            if matrix[focus_row][mid]==target:
                return True
            elif matrix[focus_row][mid]<target:
                l=mid+1
            else:
                r=mid-1
        return False
        
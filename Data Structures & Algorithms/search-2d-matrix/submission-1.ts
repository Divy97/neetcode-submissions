class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */

    binarySearch(row:number[], target:number): boolean {
        let left = 0;
        let right = row.length - 1;
        
        while (left <= right) {
            let mid = Math.floor((left + right) / 2);
            
            if (row[mid] === target) {
                return true
            } else if (row[mid] < target) {
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
        return false
    }

    searchMatrix(matrix: number[][], target: number): boolean {
        let top = 0
        let bottom = matrix.length - 1
    
        while (top <= bottom) {
            const mid = Math.floor((top + bottom) / 2);
            const row = matrix[mid]
            
            if (target < row[0]) {
                bottom = mid - 1
            } else if (target > row[row.length - 1]) {
                top = mid + 1
            } else {
                return this.binarySearch(row, target)
            }
        }
    
        return false
    }
}

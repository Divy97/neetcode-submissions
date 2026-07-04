class Solution {
    /**
     * @param {number[]} nums1
     * @param {number[]} nums2
     * @return {number}
     */


    findMedianSortedArrays(nums1: number[], nums2: number[]): number {
        let A = nums1;
        let B = nums2;

        // to make sure we always search in shorter array - A will be always shorter
        if (A.length > B.length) {
            [A, B] = [B, A];
        }

        const total = A.length + B.length;
        const half = Math.floor((total + 1) / 2);

        let left = 0;
        let right = A.length;

        while (left <= right) {
    
            const partitionA = Math.floor((left + right) / 2);
            const partitionB = half - partitionA;

            const leftA = partitionA === 0 ? -Infinity : A[partitionA - 1];

            const rightA = partitionA === A.length ? Infinity : A[partitionA];

            const leftB = partitionB === 0 ? -Infinity : B[partitionB - 1];

            const rightB = partitionB === B.length ? Infinity : B[partitionB];

            // Correct partition found

            if (leftA <= rightB && leftB <= rightA) {
                if (total % 2 === 1) {
                    return Math.max(leftA, leftB);
                }
                return (Math.max(leftA, leftB) + Math.min(rightA, rightB)) / 2;
            }

            // Too many elements taken from A

            if (leftA > rightB) {
                right = partitionA - 1;
            } else {
                // Too few elements taken from A
                left = partitionA + 1;
            }
        }
        return -1;
    }
}
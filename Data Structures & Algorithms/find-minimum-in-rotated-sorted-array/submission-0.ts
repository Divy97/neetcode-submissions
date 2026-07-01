class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums: number[]): number {
        let answer :number = Number.MAX_VALUE

        let left = 0;
        let right = nums.length - 1;

        while (left <= right) {
            let mid = Math.floor((left + right) / 2);

            if (nums[left] <= nums[right]) {
                answer =  Math.min(answer,nums[left])
                break
            }

            if (nums[left] <= nums[mid]) {
                answer = Math.min(nums[mid], nums[left])
                left = mid + 1
            } else {
                answer = Math.min(answer,nums[mid])
                right = mid - 1
            }
        }
        return answer;
    }
}

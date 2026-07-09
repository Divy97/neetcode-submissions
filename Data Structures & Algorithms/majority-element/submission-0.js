class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    majorityElement(nums) {
        const n = nums.length;
        while (true) {
            const candidate = nums[Math.floor(Math.random() * n)];
            let count = 0;
            for (const num of nums) {
                if (num === candidate) {
                    count++;
                }
            }
            if (count > Math.floor(n / 2)) {
                return candidate;
            }
        }
    }
}
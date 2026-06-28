class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */

    findTotalHours(piles:number[], mid: number):number {
        let totalHours = 0

        for (let i = 0; i < piles.length; i++) {
            totalHours += Math.ceil(piles[i] / mid)
        }
        return totalHours
    }

    minEatingSpeed(piles: number[], h: number): number {
        let left = 1;
        let right = Math.max(...piles)

        let ans = -1

        while (left <= right) {
            let mid = Math.floor((left + right) / 2);
            
            let totalHours = this.findTotalHours(piles, mid)
            if (totalHours <= h) {
                ans = mid
                right = mid - 1
            } else {
                left = mid + 1
            }
        }
        return ans
    }
}

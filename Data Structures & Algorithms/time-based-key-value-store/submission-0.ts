class TimeMap {
    private store: Map<string, [string, number][]>;

    constructor() {
        this.store = new Map();
    }

    

    set(key: string, value: string, timestamp: number): void {
        if (!this.store.has(key)) {
            this.store.set(key, []);
        }

        this.store.get(key)!.push([value, timestamp]);
    }

    get(key: string, timestamp: number): string {
        if (!this.store.has(key)) {
            return "";
        }

        const values = this.store.get(key)!;

        let left = 0;
        let right = values.length - 1;
        let answer = "";

        while (left <= right) {
            const mid = Math.floor((left + right) / 2);

            if (values[mid][1] <= timestamp) {
                answer = values[mid][0];
                left = mid + 1; 
            } else {
                right = mid - 1;
            }
        }

        return answer;
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key, value, timestamp)
 * var param_2 = obj.get(key, timestamp)
 */
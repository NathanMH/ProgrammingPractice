class Queue {
    data = [];
    constructor() {
        this.data = [];
    }

    add(item) {
        this.data.unshift(item);
    }

    remove() {
        this.data.pop();
    }
}

const test_queue = new Queue;
test_queue.add(5);
test_queue.add(4);
test_queue.add(3);
test_queue.add(2);
test_queue.add(8);
test_queue.add(7);
test_queue.add(6);
test_queue.add(1);

test_queue.remove();
test_queue.remove();
test_queue.remove();

console.log(test_queue);
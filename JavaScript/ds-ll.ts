class node {
    data: string;
    next: node;
    constructor(data: string, next = null) {
        this.data = data;
        this.next = next;
    }
}

var test_node = new node("Hi");

console.log(test_node);
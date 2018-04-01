function Graph(){
	this.nodes = [];
	this.edges = [];
}


Graph.prototype.addNode = function(node) {
	this.nodes.push(node)
};

Graph.prototype.removeNode = function(first_argument) {
	// body...
};

Graph.prototype.addEdge = function(node1,node2) {
			
};

Graph.prototype.removeEdge = function(first_argument) {
	// body...
};


function Node(){
	this.name = name;
	this.edges = [];
}

function Edge(){
	this.from;
	this.to;
}
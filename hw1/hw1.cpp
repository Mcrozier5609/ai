// C++ program to print DFS traversal from a given vertex in a  given graph
#include<iostream>
#include<list>
#include<stack>
#include<stdio.h>
 
using namespace std;

struct state {
		int can40a;
    int can40b;
    int can4;
    int can5;
    int max[4] = {40, 40, 4, 5};
    list<state> children;
};
 
// Graph class represents a directed graph using adjacency list representation
class Graph
{
    list<state> states;    // Pointer to an array containing adjacency lists
    void DFSUtil(int v, bool visited[]);  // A function used by DFS
public:
		int V; //number of states
    Graph();   // Constructor
    bool isValid(state *current);
    void addStates(state current);
    void victory();
    stack<state> path;
};
 
Graph::Graph()
{
    this->V = 0;
    //states = new list<state>;
}

void Graph::addStates(state current) {
		//check if valid and add to list
		if (isValid(&current)) {
    		this->states.push_back(current);
    		V++;
        path.push(current);
        if (current.can4 == 2 && current.can5 == 2){
        		victory();
        }
    }
    else {
    		path.pop();
    		return;
    }
    
    //make children
    state child = current;
  	int x;
    int y;
    for(x = 0; x < 4; x++) {
    		if (current.cans[x] > 0) {
        		//TRY TO POUR OUT
            for(y = 0; y < 4; y++) {
                if (y == x) {
                
                }
                else {
                		if (current.cans[y] < current.max[y]) {
                      	int temp = current.cans[x];
                        if (child.cans[x] > (child.max[y] - child.cans[y])) {
                    				child.cans[x] = child.cans[x] - (child.max[y] - child.cans[y]);
                        }
                        else {
                        		child.cans[x] = 0;
                        }
                        if (temp < (child.max[y] - child.cans[y])) {
                        		child.cans[y] = child.cans[y] + temp;
                        }
                        else {
                        		child.cans[y] = child.max[y];
                        }
                    }
                }
                addStates(child);
            }
        }
    }
    path.pop();
    return;
}

void Graph::victory(){
		printf("VICTORY\npath:\n");
    state output[path.size()];
    stack<state> path2 = path;
    int j = path.size();
    for(int i = 0; i < path.size(); i++) {
				output[i] = path2.top();
        path2.pop();
		}
    for(j = j; j > 0; j--){
    		printf("%d %d %d %d\n",output[j].can40a,output[j].can40b,output[j].can5,output[j].can4);
    }
}

bool Graph::isValid(state *current) {
		int temp;
		if (current->can40a < current->can40b){
    		temp = current->can40a;
        current->can40a = current->can40b;
        current->can40b = temp;
    }
		
		for (list<state>::iterator it = states.begin(); it != states.end(); ++it){
    		if ((current->can40a != it->can40a)&&(current->can40b != it->can40b)&&(current->can4 != it->can4)&&(current->can5 != it->can5)) {
						return true;
        }
        else {
      			return false;
        }
    }
}

int main()
{
		state initialState;
    
    Graph g;
    g.addStates(initialState);
    printf("Number of states: %d", g.V);
 
    return 0;
}

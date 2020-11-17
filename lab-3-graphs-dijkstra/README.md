# How to use
1. clone this repository:
```
git clone https://github.com/redd4ford/iot-laboratory-works-algorithms-2020
```
* or simply download and extract it anywhere you wish;

2. open command prompt and switch the directory to */lab-3-graphs-dijkstra*:
```
cd iot-laboratory-works-algorithms-2020/lab-3-graphs-dijkstra
```
* if you decided to download and extract it to, let us say, D:/projects, you would do it like that:
```
D:
```
```
cd projects/iot-laboratory-works-algorithms-2020/lab-3-graphs-dijkstra
```


3. make sure you have Python 3+! then you must be able to run:
```
python gamsrv.py
```

4. *gamsrv.out* file should contain the result.

***

this program uses a custom Graph implementation to solve the GAMSRV problem. gamsrv.in file is for input; it contains M+2 lines, where:
* line 1: N M (N is the number of vertexes, M is the number of edges),
* line 2: a list of integers separated by spaces - numbers of vertexes which are Clients (vertexes are numbered from 1 to N),
* lines 3-(M+2): contain triplets of natural numbers: startnode, endnode, latency.

using Dijkstra's algorithm to get the shortest path to each node, the program finds the Server location that minimizes the largest latency value to the Client, and prints this latency.

the algorithm works like this:
1. get the total number of nodes, number of client nodes, and edges from *gamsrv.in* file,
2. for each router, get latencies from it to all the clients,
3. find the max latency between the router and all the clients,
4. if the max latency is minimal, this router can be considered a good position for the server,
5. repeat 2-4 until there is no node left to calculate,
6. write the minimal max latency to *gamsrv.out*.

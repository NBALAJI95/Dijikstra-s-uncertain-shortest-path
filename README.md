# Dijkstra’s Shortest Uncertain Path Algorithm
CS5592 Project, Spring Semester 2017
Version: March 21, 2017.
Due: Monday, April 17, 2017 (or earlier)
Roads, airspace, and computer and communication networks are often modeled as graphs. There are other examples in
social networks and cloud computing, and so on. In such a network, nodes are the cities, or intersections, or server nodes
(sources of demand, such as traffic or communication sites), and the links connect hem. If you want to go from one node to
another (by plane, by car, or routing internet traffic or information packet), then you need a plan: source, destination, and a
planned path in between. Let us explain this in terms of an road network between cities as the motivating application, but
keep in mind that this project might have additional uses. When planning a car-trip, say from a to b, most people would
want to find the shortest route, and there are several algorithms known that will help you find the shortest path. But please
do not forget that you are not the only car on the road, and with more cars on the road will cause interference and extra
delay because you share the road with more and more others. In other words: the delay along an edge is rarely a constant
value, but rather fluctuates according to a random variable for each edge: the value is uncertain. We are still interested in
finding some sort of shortest path, but shortest is now defined in a stochastic setting. We will call such a paths a UncertainShortestPath.
You will be given a number of different input scenario’s. Each scenario will have
1. The size n of the system (the total number of cities), together with the index of two cities, a and b.
2. An adjacency matrix E with edge-weights. The (i, j)th entry E[i, j] represents the main characteristics of the random variable representing the traveling time on the edge between the two specific nodes, i and j, assuming that there are no other cars on the edge that might slow you down. The main characteristics we provide are T, the type of distribution, together with two more parameters, α and β, whose interpretation depends on the type

# Criteria to be used
The criteria to be used are:
Mean Value Pick the path whose total “expected value” is smallest from among all paths.
Optimist Pick the path such that it’s “expected value - standard deviation” (as long as this is positive) is smallest from
among all paths.
Pessimist Pick the path such that it’s “expected value + standard deviation” is smallest from among all paths.
Double Pessimist Pick the path such that it’s “expected value + 2 standard deviation” is smallest from among all paths.
Stable Pick the path such that it’s “squared coefficient of variation” is smallest from among all paths.
We are sure you can come up with others (e.g. additional weights, or probabilities, or Laplace Transforms, or use
Chebyshev’s moment inequalities to find bounds, or ......). In fact, if your team has three members, you must add one
additional criterion, and explain why it may make sense. Whichever additional strategy your team decides to adopt and
adapt, you must add them to the 5 mentioned above and compare all 5 or more shortest paths from a to b.
Performance measures
Subsequently, you will then have to compare and analyze the paths as generated, For each of these paths, you are asked
to determine the hop-count. Also, the path delay itself has an “expected value,” “expected value - standard deviation,”
“expected value + standard deviation,” “expected value + 2 standard deviation,” and “squared coefficient of variation.” You
are asked to determine their values. You are also asked how these paths differ. Is there a link common to all paths? You
must compare the paths according to at least the following characteristics. Present your result in a table, such as the one
below. In the table, we use µ to indicate the path-mean, σ to indicate it’s standard deviation. Also, “hops” indicates the
hop-length.
µ − σ µ µ + σ µ + 2σ c2
(Y) hops
Mean Value
Optimist
Pessimist
Doubly Pess
Stable
add your own
Finally, you are asked to check whether or not the strategies result in a different path. Alternately, for all links on any
path, count how many paths use this link, and print five links that are shared with the largest number of paths. For instance,
Mean Value Optimist Pessimist Doubly Pess Stable own
edge (x,y)
(..., ...)
(..., ...)
(..., ...)


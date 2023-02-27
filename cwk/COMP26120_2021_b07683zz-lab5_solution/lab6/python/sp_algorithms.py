import graph
import pq
import general
from shortest_path import sssp_result_t, sp_result_t
import weight

##
 # Use BFS to compute APSP.
 # Edge weights are to be ignored, and the shortest paths in terms
 # of edge count shall be computed.
 #
 # If dst is not INVALID_NODE, the algorithm should stop as soon as it has computed a shortest path to dst.
 #
 #/
def bfs(g, src, dst):
    stat_edges_explored = 0
    
    N = g.graph_get_num_nodes()
    pred = [graph.INVALID_NODE]*N
    dist = [weight.weight_inf()]*N
    
    general.error("Not implemented")
    
    return sssp_result_t(N, src, dst, False, pred, dist, stat_edges_explored)

##
 # Use Bellman-Ford to compute shortest paths in a weighted graph.
 # For nodes reachable from infinite weight cycles, your algorithm
 # should report a distance of -inf, and the predecessor INVALID_NODE.
 #
 #/
def bellman_ford(g, src):
    general.error("Not implemented")

##
 # Use Dijkstra's algorithm to compute shortest paths in a weighted graph with
 # non-negative weights.
 #
 # If dst is not INVALID_NODE, the algorithm should stop as soon as it has computed a shortest path to dst.
 #
 # @pre Graph has no negative weights
 #/
def dijkstra(g, src, dst):
    general.error("Not implemented")

##
 # Use the A* algorithm to compute a shortest path between src and dst.
 # You can assume that there are no negatrive weights, and that the heuristics h is monotone.
 #
 # @pre Graph has no negative weights
 # @pre h is monotone, i.e., for all u, h(u) + w(u,v) <= h(v)
 #
 #/
def astar_search(g, src, dst, h):
    general.error("Not implemented")

"""
Module to store utility functions for test purposes.
"""
from os import path, mkdir
from collections import deque
# importing os vs. importing os.path has no impact in python, but can add impact in other languages

VAR = 'slkjfdl'
def two_sum(nums, target):
    """ Find the index of the two first numbers that add up to target.

    :param nums: a list of numbers
    :param target: the value to reach
    :return: a list of the index of the two numbers
    :raises TypeError: if the target is not a number
    """
    print_statement('statement')

def two_sum(nums, target):

    if isinstance(target, str):
        raise TypeError("The target should be a number.")
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]


def print_statement(statement):
    """ prints a statement

    :param statement: a string
    :return: a string
    """
    print(statement)
    return '123'


def create_download_directory():
    """ Creates a download directory if it doesn't exist

    :return: True or False
    """

    here = path.dirname(__file__)
    download_dir_path = path.join(here, 'downloads')
    # depending on the os, we might have different system for path, ex: "/", "\". using path.join, takes care of this

    if not path.exists(download_dir_path):
        mkdir(download_dir_path)
        return True
    return False


def build_graph(edges):
    """ Converts a list of directed edges into a graph represented as a dictionary.

    This function takes a list of tuples, where each tuple represents a directed edge
    from one node to another in the graph. The graph is represented as a dictionary
    where each key is a node and its value is a list of all nodes it has edges to.

    Parameters:
    - edges (list of tuples): Each tuple contains two elements, representing a
      directional link from the first element (source node) to the second element
      (destination node).

    Returns:
    - dict: A dictionary representation of the graph where keys are source nodes
      and values are lists of destination nodes.

    Example:
    Given edges [(0, 1), (0, 2), (1, 2), (2, 3)], the function returns
    {0: [1, 2], 1: [2], 2: [3]}.
    """
    graph = {}
    for edge in edges:
        if edge[0] in graph:
            graph[edge[0]].append(edge[1])
        else:
            graph[edge[0]] = [edge[1]]
    return graph


def find_cycles(graph):
    """
    Finds all unique cycles in the graph using a Breadth-First Search (BFS) approach
    and returns them as a list of tuples, where each tuple represents a cycle.

    This function iterates over each node in the graph, using BFS to explore reachable
    nodes. It keeps track of the path taken to reach each node. If it encounters a node
    that completes a cycle back to the starting node, and the set of nodes in the cycle
    has not been encountered before, it records this cycle.

    Parameters:
    - graph (dict): A graph represented as a dictionary where each key is a node and
      its value is a list of nodes it has edges to.

    Returns:
    - list of tuples: Each tuple contains nodes forming a cycle, including the starting
      node repeated at the end to signify the cycle closure.

    Note:
    The function ensures that each cycle is unique based on the members of the cycle,
    not the starting point of the cycle in the path. Cycles that contain the same set
    of nodes but start at different points are considered the same and only one is returned.

    Example:
    Given a graph {0: [1, 2], 1: [2], 2: [3], 3: [0]}, the function may return
    [(0, 1, 2, 3, 0), (0, 2, 3, 0)] as it identifies the cycles in the graph.
    """
    cycles = []
    cycles_members = []
    for start_node in graph:
        queue = deque([(start_node, [start_node])])
        while queue:
            current_node, path = queue.popleft()
            for neighbor in graph.get(current_node, []):
                cycle_members = set(path + [neighbor])
                if neighbor == start_node and cycle_members not in cycles_members:
                    cycles.append(tuple(path + [neighbor]))
                    cycles_members.append(cycle_members)
                elif neighbor not in path:
                    queue.append((neighbor, path + [neighbor]))
    return cycles


# if __name__ == "__main__":
#     edges = [(0, 1), (0, 2), (1, 2), (2, 3), (3, 0)]
#     graph = build_graph(edges)
#     cycles = find_cycles(graph)
 # AVOID HAVING MAIN in a library!

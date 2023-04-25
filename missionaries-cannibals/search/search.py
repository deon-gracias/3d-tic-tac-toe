import sys

from search import Node


def iterative_deepening_search(problem):
    for depth in range(sys.maxsize):
        result = depth_limited_search(problem, depth)
        if result != 'cutoff':
            return result


def depth_limited_search(problem, limit=50):
    root = Node(problem.initial_state)
    return __recursive_dls(root, problem, limit)


def __recursive_dls(node, problem, limit):
    """Recursive helper function for depth limited search.

    Returns 'cutoff' if no solution was found within the specified limit.
    Otherwise returns the node containing the goal state.
    """
    if problem.is_goal_state(node.state):
        return node
    elif limit == 0:
        return 'cutoff'
    else:
        cutoff_occurred = False
        for child in node.expand(problem):
            result = __recursive_dls(child, problem, limit - 1)
            if result == 'cutoff':
                cutoff_occurred = True
            elif result is not None:
                return result
        return 'cutoff' if cutoff_occurred else None

meowstake_matches_cache = {}
def meowstake_matches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    '''
    if ______________: # Fill in the condition
        # BEGIN
        "*** YOUR CODE HERE ***"
        # END

    elif ___________: # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        # END

    else:
        add_diff = ...  # Fill in these lines
        remove_diff = ... 
        substitute_diff = ... 
        # BEGIN
        "*** YOUR CODE HERE ***"
        # END
    ''' 
    if (start, goal, limit) in meowstake_matches_cache:
        return meowstake_matches_cache[(start, goal, limit)]
    if limit == 0:
        return 999 if start != goal else 0
    elif start == '' or goal == '':
        return max(len(start), len(goal))
    elif start[0] == goal[0]:
        meowstake_matches_cache[(start, goal, limit)] = meowstake_matches(start[1:], goal[1:], limit)
        return meowstake_matches_cache[(start, goal, limit)]
    else:
        add_diff = 1 + meowstake_matches(goal[0]+start, goal,limit-1)
        remove_diff = 1 + meowstake_matches(start[1:], goal, limit-1)
        substitute_diff = 1 + meowstake_matches(goal[0]+start[1:], goal, limit-1)
        meowstake_matches_cache[(start, goal, limit)] = min(add_diff, remove_diff, substitute_diff)
        return meowstake_matches_cache[(start, goal, limit)]


key_distance_diff_cache = {}
key_distance = get_key_distances()
def key_distance_diff(start, goal, limit):
    """ A diff function that takes into account the distances between keys when
    computing the difference score."""

    start = start.lower() #converts the string to lowercase
    goal = goal.lower() #converts the string to lowercase

    # BEGIN PROBLEM EC1
    ''' Attempt #1
    def helper(start, goal, diff):
        a = start[0]
        b = goal[0]
        distance = key_distance[a, b]
        if diff == limit and a != b:
            return float("inf")
        elif len(start) == 1 or len(goal) == 1:
            if a != b:
                return diff + distance
            return diff
        elif a != b:
            return helper(start[1:], goal[1:], diff + distance)
        return helper(start[1:], goal[1:], diff)
    return helper(start, goal, abs(len(start)-len(goal)))
    '''

    if (start, goal, limit) in key_distance_diff_cache:
        return key_distance_diff_cache[(start, goal, limit)]
    if limit == 0:
        return float("inf") if start != goal else 0
    elif start == '' or goal == '':
        return max(len(start), len(goal))
    elif start[0] == goal[0]:
        key_distance_diff_cache[(start, goal, limit)] = key_distance_diff(start[1:], goal[1:], limit)
        return key_distance_diff_cache[(start, goal, limit)]
    else:
        add_diff = 1 + key_distance_diff(goal[0]+start, goal,limit-1)
        remove_diff = 1 + key_distance_diff(start[1:], goal, limit-1)
        substitute_diff = key_distance[start[0], goal[0]] + key_distance_diff(goal[0]+start[1:], goal, limit-1)
        key_distance_diff_cache[(start, goal, limit)] = min(add_diff, remove_diff, substitute_diff)
        return key_distance_diff_cache[(start, goal, limit)]



key_distance = get_key_distances()
def key_distance_diff(start, goal, limit):
    """ A diff function that takes into account the distances between keys when
    computing the difference score."""

    start = start.lower() #converts the string to lowercase
    goal = goal.lower() #converts the string to lowercase

    # BEGIN PROBLEM EC1
    ''' Attempt #1
    def helper(start, goal, diff):
        a = start[0]
        b = goal[0]
        distance = key_distance[a, b]
        if diff == limit and a != b:
            return float("inf")
        elif len(start) == 1 or len(goal) == 1:
            if a != b:
                return diff + distance
            return diff
        elif a != b:
            return helper(start[1:], goal[1:], diff + distance)
        return helper(start[1:], goal[1:], diff)
    return helper(start, goal, abs(len(start)-len(goal)))
    '''

    if limit == 0:
        return float("inf") if start != goal else 0
    elif start == '' or goal == '':
        return max(len(start), len(goal))
    elif start[0] == goal[0]:
        return key_distance_diff(start[1:], goal[1:], limit)
    else:
        add_diff = 1 + key_distance_diff(goal[0]+start, goal,limit-1)
        remove_diff = 1 + key_distance_diff(start[1:], goal, limit-1)
        substitute_diff = key_distance[start[0], goal[0]] + key_distance_diff(goal[0]+start[1:], goal, limit-1)
        return min(add_diff, remove_diff, substitute_diff)
    # END PROBLEM EC1





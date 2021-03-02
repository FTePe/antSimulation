from path import Path
import numpy as np


def create_maze(m_map, m_paths={}):
    # m(aze)_map defines the layout
    # returns m(aze)_paths a dictionary of paths, with their locations in m_map as their keys
    loc_map = np.transpose(np.nonzero(m_map))
    for loc in loc_map:
        loc = tuple(loc)
        angle = 0  # some simple trig * path length
        if loc[0] > 0:
            parents = parent_check(m_map[loc[0]-1], loc)
        else:
            parents = []
        m_paths[loc] = Path(angle, loc, parents)
        for parent_loc in parents:
            m_paths[parent_loc].add_child(m_paths[loc])
    return m_paths


def parent_check(m, loc):
    # m = row of m_map to be searched for parents
    # loc = the location of the path
    # returns a list of tuples of parents locations
    locs = np.nonzero(m)[0]
    parents = []
    for l in locs:
        if l == loc[1]+1 or l == loc[1]-1:
            parents.append((loc[0]-1, l))
    return parents


def test():
    # choose which test to run
    test_structure = np.array([
        [0, 1, 0],  # path to nest
        [1, 0, 1],  # path, path
        [0, 1, 0]  # path to food
    ])
    
    test_structure = np.array([
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 1, 0, 1],
        [0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0]
    ])
    
    a = create_maze(test_structure)
    print(a)
    for i in a:
        print(a[i].parents)


if __name__ == '__main__':
    test()
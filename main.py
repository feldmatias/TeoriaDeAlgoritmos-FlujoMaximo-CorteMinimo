import sys

from initialization import create_graph
from max_flow_min_cut import max_flow_min_cut
from result import calculate_result

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Please enter file name.")
        print("Usage: `python main.py <filename>`")
    else:
        vertices, start, end = create_graph(sys.argv[1])
        max_flow, min_cut = max_flow_min_cut(vertices, start, end)
        calculate_result(max_flow, min_cut, start, end)

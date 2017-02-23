import os
import math
import random
import itertools


class Pizza(object):
	def __init__(self,rows, cols, grid):
		self.rows = rows
		self.cols = cols
		self.grid = grid

	def __str__(self):
		return "Pizza"


def read_file(filename):
    """Read the input file."""
    with open(filename, 'r') as fin:
    	line = fin.readline()
    	rows, cols, min_ing, max_cells, = [int(num) for num in line.split()]
    	grid = []
    	for row in range(rows):
    		grid.append(f.readline)

    pizza = Pizza(rows, cols, grid)
    return pizza, min_ing, max_cells


def write_file(grid, filename):
    """Write output file."""
    with open(filename, 'w') as fout:
        fout.write('%d\n' % len(data))
        for d in data:
            fout.write(' '.join([str(item) for item in d]) + '\n')
    return

def cut(pizza):
	pass

def main():
    """Main function."""

    if len(sys.argv) < 3:
        sys.exit('Syntax: %s <filename> <output>' % sys.argv[0])

    print 'Running on file: %s' % sys.argv[1]

    # read input file
    pizza, min_ing, max_cells = read_file(sys.argv[1])

    try:
        cuts = cut(pizza, min_ing, max_cells)
    except KeyboardInterrupt:
        pass

    # write output file
    write_file(cuts, sys.argv[2])

if __name__ == '__main__':
	main()
import os
import math
import random
import itertools
import sys


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
    	v, e, r, c, x = [int(num) for num in line.split()]
    	line = fin.readline()
    	v_sizes = [int(num) for num in line.split()]
    	end = []
    	for i in range(e):
    		l = []
    		dl, cap = [int(num) for num in fin.readline().split()]
    		l.append((-1,dl))
    		for i in range(cap):
    			c_id, lat = [int(num) for num in fin.readline().split()]
    			l.append((c_id, lat))
    		end.append(l)
    	reqs = []
    	for i in range(r):
    		req, vid, endp = [int(num) for num in fin.readline().split()]
    		reqs.append((req, vid, endp))
    	return (v,e,r,c,x,v_sizes,end,reqs)


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
	#if len(sys.argv) < 3:
	#	sys.exit('Syntax: %s <filename> <output>' % sys.argv[0])

    #print 'Running on file: %s' % sys.argv[1]
    # read input file
    (v,e,r,c,x,v_sizes,end,reqs) = read_file(sys.argv[1])
    print v,e,r,c,x
    print v_sizes
    print end
    print reqs

    # write output file
    #write_file(cuts, sys.argv[2])

if __name__ == '__main__':
	main()
import os
import math
import random
import itertools
import sys


class Cache(object):
    def __init__(self, id, size):
        self.id = id
        self.size = size
        self.size_left = size
        self.video_list = []

    def add_video(self, video_id, video_size):
        """Returns True if adding is successful. False otherwise"""
        after_size = self.size_left - video_size
        if after_size >= 0 and (video_id, video_size) not in self.video_list:
            self.size_left = after_size
            self.video_list.append((video_id, video_size))
            return True
        else:
            return False

    def is_empty(self):
        """Retuns true if cache server is empty"""
        if self.video_list:
            return False
        return True

    def __str__(self):
        return ('%s ' % self.id) + ' '.join(str(id) for (id, size) in self.video_list)


class Endpoint(object):
    def __init__(self, latency):
        self.dc_lat = latency
        self.caches = []

    def add_cache(self, cache, latency):
        self.caches.append((cache, latency))

    def cache_video(self, video_id, video_size):
        for cache, _ in self.caches:
            if cache.add_video(video_id, video_size):
                return cache.id
        return -1





def read_file(filename):
    """Read the input file."""
    with open(filename, 'r') as fin:
        line = fin.readline()
        v, e, r, c, x = [int(num) for num in line.split()]
        line = fin.readline()
        videos = [int(num) for num in line.split()]
        endpoints = []
        caches = []
        for i in range(c):
            caches.append(Cache(i, x))

        for i in range(e):

            l = []
            dl, cap = [int(num) for num in fin.readline().split()]
            endpoint = Endpoint(dl)
            for j in range(cap):

                c_id, lat = [int(num) for num in fin.readline().split()]
                endpoint.add_cache(caches[c_id], lat)
            endpoints.append(endpoint)
        requests = []
        for i in range(r):
            video, endpoint, request_count = [int(num) for num in fin.readline().split()]
            requests.append((video, endpoint, request_count))
        return (v, e, r, c, x, videos, endpoints, requests, caches)

        grid = []
        for row in range(rows):
            grid.append(f.readline)




def write_file(caches, filename):
    """Write output file."""
    with open(filename, 'w') as fout:
        ilist = []
        count = 0
        for i, cache in enumerate(caches):
            if not cache.is_empty():
                ilist.append(i)
                count += 1

        fout.write(str(count)+'\n')
        for i in ilist:
            fout.write(str(caches[i])+'\n')
    return

import time

def main():
    start = time.time()

    (v, e, r, c, x, videos, endpoints, requests, caches) = read_file(sys.argv[1])

    for video, endpoint, request_number in requests:
        endpoints[endpoint].cache_video(video, videos[video])


    #write output file
    write_file(caches, sys.argv[2])
    end = time.time()

    print('Finished in {0} seconds'.format(end - start))

if __name__ == '__main__':
    main()

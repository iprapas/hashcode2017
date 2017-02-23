import operator

(v, e, r, c, x) = map(int, raw_input().split())

print "v: ", v
print "e: ", e
print "r: ", r
print "c: ", c
print "x: ", x

sizes = map(int, raw_input().split())
video = {}
for video_id in xrange(0, v): 
	video[video_id] = sizes[video_id]

print "video: ", video

endpoint = {}
for endpoint_id in xrange(0, e): 
	(dc_latency, k) = map(int, raw_input().split())
	cache_latency = []
	for cache in xrange(0, k): 
		cache_latency.append( map(int, raw_input().split()) )
	endpoint[endpoint_id] = ( dc_latency, cache_latency ) 

print "endpoint: ", endpoint

requests = []
for request in xrange(0, r): 
	(video_id, endpoint_id, n) = map(int, raw_input().split())
	print "Processing request #", request, "..."
	print "video_id: ", video_id
	print "endpoint_id: ", endpoint_id
	print "n: ", n
	dc_latency = endpoint[endpoint_id][0]
	print "dc_latency: ", dc_latency
	video_size = video[video_id]
	print "video_size: ", video_size 
	request_scores = {}
	for (cache_id, cache_latency) in endpoint[endpoint_id][1]: 
		current_score = n * (dc_latency - cache_latency) / video_size 
		request_scores[cache_id] = current_score
	print "request_scores: ", request_scores
	sorted_request_scores = sorted(request_scores.items(), key=operator.itemgetter(1), reverse=True)
	print "sorted_request_scores: ", sorted_request_scores
	requests.append( (video_id, sorted_request_scores ))
print "requests: ", requests
# requests = [ (video_id, sorted_requests_scores) ]
# sorted_requests_scores = [ (cache_id, score) ]

caches = {} 
for cache_id in xrange(0, c): 
	
class Video(object):
	def __init(self,vid,size):
		self.vid = vid
		self.size = size

		

class Server(object):
	def __init__(self,ids,size):
		self.ids = ids
		self.size = size
	        self.sizeLeft = size	
		self.videoList = []

	
	def __str__(self):
		return "Cache Server #" + self.ids

	def addVideo(self,vid,size):
		self.videoList.add(vid)
		self.sizeLeft = self.sizeLeft - size

class Endpoint(object):
	def __init__(self, latency):
		self.latency = latency;
		self.caches 


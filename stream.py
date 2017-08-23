#! python3


class Stream:
  def __init__(self):
      self.name = stream['stream']
      for key in stream:
          setattr(self, key, stream[key])



stream_111 = {'stream': '11-11', 'pressure': 1, 'df':22}

x = Stream(stream_111)

print (x.pressure, x.name)

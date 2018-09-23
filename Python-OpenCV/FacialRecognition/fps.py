import datetime


class FPS:
    def __init__(self):
        # store the start, end and number of frames
        # that were examined between the interval
        self._start = None
        self._end = None
        self._numFrames = 0

    def start(self):
        # start timer
        self._start = datetime.datetime.now()
        return self

    def stop(self):
        # stop the timer
        self._end = datetime.datetime.now()
        return self

    def update(self):
        # increment the total number of frames examined
        # during the start/end intervals
        self._numFrames += 1

    def elapsed(self):
        # return the total number of second between start
        # and end intervals
        return (self._end - self._start).total_seconds()

    def fps(self):
        # compute the approx. frames per second
        return self._numFrames / self.elapsed()

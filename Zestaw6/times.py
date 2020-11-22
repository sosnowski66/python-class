

class Time:

    def __init__(self, s=0):
        self.s = int(s)

    def __str__(self):
        hours = self.s // 3600
        seconds = self.s - hours * 3600
        minutes = seconds // 60
        seconds -= minutes * 60

        return "{0:02d}:{1:02d}:{2:02d}".format(hours, minutes, seconds)

    def __repr__(self):
        return "Time({0})".format(self.s)

    def __add__(self, other):
        return Time(self.s + other.s)

    def __cmp__(self, other):
        from filecmp import cmp
        return cmp(self.s, other.s)

    def __eq__(self, other):
        return self.s == other.s

    def __ne__(self, other):
        return self.s != other.s

    def __gt__(self, other):
        return self.s > other.s

    def __ge__(self, other):
        return self.s >= other.s

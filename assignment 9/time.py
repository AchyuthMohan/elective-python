class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def __add__(self, other):
        if isinstance(other, Time):
            total_seconds = self.to_seconds() + other.to_seconds()
            return Time.from_seconds(total_seconds)
        else:
            raise TypeError("Unsupported operand type for +: 'Time' and '{}'".format(type(other)))

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @classmethod
    def from_seconds(cls, total_seconds):
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return cls(int(hours), int(minutes), int(seconds))
t1 = Time(12, 30, 45)
t2 = Time(4, 15, 20)

print(t1)  

t3 = t1 + t2
print(t3)  
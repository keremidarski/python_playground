class Interval:
    def __init__(self, start, end, start_opened=False, end_opened=False):
        self.start = start
        self.end = end
        self.start_opened = start_opened
        self.end_opened = end_opened


    def is_inside(self, value):
        inside_start = False
        inside_end = False

        if self.start_opened:
            inside_start = value > self.start
        else:
            inside_start = value >= self.start

        if self.end_opened:
            inside_end = value < self.end
        else:
            inside_end = value <= self.end

        return inside_start and inside_end


    def stringify(self):
        start_bracket = '['
        end_bracket = ']'

        if self.start_opened:
            start_bracket = '('

        if self.end_opened:
            end_bracket = ')'

        return f'{start_bracket}{self.start}, {self.end}{end_bracket}'       


# Expected: True
closed_interval = Interval(1, 10)

print(closed_interval.is_inside(1) is True)
print(closed_interval.is_inside(5) is True)
print(closed_interval.is_inside(10) is True)
print(closed_interval.stringify() == "[1, 10]")

opened_interval = Interval(1, 10, start_opened=True, end_opened=True)

print(opened_interval.is_inside(1) is False)
print(opened_interval.is_inside(5) is True)
print(opened_interval.is_inside(10) is False)
print(opened_interval.stringify() == "(1, 10)")

half_opened_interval = Interval(1, 10, start_opened=False, end_opened=True)

print(half_opened_interval.is_inside(1) is True)
print(half_opened_interval.is_inside(5) is True)
print(half_opened_interval.is_inside(10) is False)
print(half_opened_interval.stringify() == "[1, 10)")

half_opened_interval = Interval(1, 10, start_opened=True, end_opened=False)

print(half_opened_interval.is_inside(1) is False)
print(half_opened_interval.is_inside(5) is True)
print(half_opened_interval.is_inside(10) is True)
print(half_opened_interval.stringify() == "(1, 10]")

class Signal(list):
    def __add__(self, other):
        if not isinstance(other, Signal):
            raise TypeError("Can only add Signal to Signal")
        if len(self) != len(other):
            raise ValueError("Signals must be of the same length")
        return Signal([a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        if not isinstance(other, Signal):
            raise TypeError("Can only subtract Signal to Signal")
        if len(self) != len(other):
            raise ValueError("Signals must be of the same length")
        return Signal([a - b for a, b in zip(self, other)]) 
class Calculator:
    """
            Calculator class manipulating starting value of 0 with these  functions:
            - addition,
            - subtraction,
            - multiplication,
            - division,
            - Root of number.
            - Reset function.
    """

    def __init__(self):
        self.value = 0.0

    def add(self, x=0):  # adds initial value with x

        self.value += x
        return self.value

    def subtract(self, x=0):  # subtracts x from the initial value
        self.value -= x
        return self.value

    def multiply(self, x=0):  # multiplies initial value by x
        self.value *= x
        return self.value

    def divide(self, x):  # divides initial value by x

        if x == 0:
            return "Cannot divide by zero"

        self.value = self.value / x

        return self.value

    def root(self):  # takes square root of value

        if self.value < 0:
            self.value = 0

        self.value = self.value ** (1 / 2)
        return self.value

    def reset(self):  # resets manipulated value to initial state
        self.value = 0.0

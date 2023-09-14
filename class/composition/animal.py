class Tail:
    def __init__(self, length):
        self.length = length

    def wag(self):
        print("Tail wagging")


class Horse:
    def __init__(self, color, tail_length):
        self.color = color
        self.tail = Tail(tail_length)


if __name__ == "__main__":
    horse = Horse("brown", 100)
    print(horse.color)
    print(horse.tail.length)
    horse.tail.wag()

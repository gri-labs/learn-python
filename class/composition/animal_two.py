class Tail:
    def __init__(self, length):
        self.length = length

    def wag(self):
        print("Tail wagging")


class Horse:
    def __init__(self, color, tail):
        self.color = color
        self.tail = tail


if __name__ == "__main__":
    horse = Horse("brown", Tail(100))
    print(horse.color)
    print(horse.tail.length)
    horse.tail.wag()

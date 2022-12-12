class Monkey:
    def __init__(self, test_val, worry_op, worry_val, fail_target, pass_target, items, divisor=-1):
        self.items = items
        self.test_val = test_val
        self.worry_op = worry_op
        self.worry_val = worry_val
        self.pass_target = pass_target
        self.fail_target = fail_target
        self.items = items.copy()
        self.calmdown = divisor
        self.plays = 0

    def __len__(self):
        return len(self.items)

    def __gt__(self, other):
        return self.plays > other.plays

    def __eq__(self, other):
        return self.plays == other.plays

    def __ge__(self, other):
        return self.plays >= other.plays

    def __repr__(self):
        return f"Plays: {self.plays}\tItems: {self.items}"

    def catch_item(self, item):
        self.items.append(item)

    def pass_next_item(self):
        self.plays += 1
        temp = self.items.pop(0)
        temp = eval(f"{temp} {self.worry_op} {self.worry_val}")
        if self.calmdown == -1:
            temp = temp // 3
        else:
            temp = temp % self.calmdown
        if temp % self.test_val == 0:
            target = self.pass_target
        else:
            target = self.fail_target
        return temp, target

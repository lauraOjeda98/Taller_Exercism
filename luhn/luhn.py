class Luhn:
    def __init__(self, card_num):
        self._card_num = card_num.replace(" ", "")

    def valid(self):
        card_num = self._card_num

        if not card_num.isnumeric() or len(card_num) < 2:
            return False

        result = sum(int(i) for i in card_num[-1::-2])

        for i in card_num[-2::-2]:
            num = 2 * int(i)

            if num < 9:
                result += num
            else:
                result += num-9

        return result % 10 == 0

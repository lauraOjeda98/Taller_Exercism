class PhoneNumber:
    def __init__(self, number):
        number = number.replace(".", "").replace(" ", "")
        num = ""
        for i in number:
            if i.isdigit():
                num += i

        if num[0] == "1":
            num = num[1:]

        if num[0] == "0" or num[0] == "1" or num[3] == "0" or num[3] == "1" or len(num) != 10:
            raise ValueError("Not valid format.")

        self.area_code = "".join(num[:3])
        self.exchange = "".join(num[3:6])
        self.subcriber = "".join(num[6:])

        self.number = self.area_code + self.exchange + self.subcriber

    def pretty(self):
        return f"({self.area_code})-{self.exchange}-{self.subcriber}"

class StrategyDeal:
    def __init__(self, bank=None, entry=None, targets=None, close=None):
        self.bank = bank
        self.entry = entry
        self.targets = targets
        self.per = [(target / entry - 1) * 100 for target in targets]
        self.close = close

    def get_targets(self):
        return self.targets

    def get_target_percents(self):
        return self.per

    def get_target_banks(self):
        return [round(self.bank * (p / 100 + 1), 3) for p in self.per]

    def __str__(self):
        targets = "\n\n".join(
            [
                f"{i + 1} target: {self.get_targets()[i]}\n"
                f"Percent: {round(self.get_target_percents()[i], 3)}\n"
                f"Bank: {round(self.get_target_banks()[i], 3)}"
                for i in range(len(self.get_targets()))
            ]
        )
        return f"BANK: {self.bank}\nSTART_PRICE: {self.entry}\nSTOP_PRICE: {self.close}\n\n{targets}"


def read_data(file_name):
    self = open(file_name)
    content = self.read().split("-----")
    self.close()
    return content


def write_data(file_name, data):
    self = open(file_name, 'w')
    content = "\n\n-----\n".join([str(d) for d in data])
    self.write(content)
    self.close()


def prepare_data(deal):
    lines = deal.split("\n")

    raw_bank = list(filter(lambda x: x.startswith('BANK: '), lines))
    raw_entry = list(filter(lambda x: x.startswith('Вход: '), lines))
    raw_targets = list(filter(lambda x: x.startswith('Таргет: '), lines))
    raw_close = list(filter(lambda x: x.startswith('Выход: '), lines))

    if len(raw_bank) != 1 or len(raw_entry) != 1 or len(raw_targets) != 1 or len(raw_close) != 1:
        return None

    deal_titles = {
        "BANK": int(raw_bank[0][6:]),
        "Вход": float(raw_entry[0][6:]),
        "Таргет": list(map(float, raw_targets[0][8:].split(';'))),
        "Выход": float(raw_close[0][7:])
    }
    return deal_titles


def main():
    content = read_data('deals.txt')

    result = []
    for raw_deal in content:
        deal_dict = prepare_data(raw_deal)
        if deal_dict is not None:
            result.append(
                StrategyDeal(deal_dict["BANK"], deal_dict["Вход"], deal_dict["Таргет"], deal_dict["Выход"])
            )

    write_data('out.txt', result)

if __name__ == '__main__':
    main()

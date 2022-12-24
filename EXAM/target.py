class StrategyDeal:
    def __init__(self, entry, targets, close, bank):
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
    file = open(file_name)
    content = file.read()
    file.close()
    return content


def write_data(file_name, data):
    self = open(file_name, 'w')
    content = "\n\n-----\n".join([str(d) for d in data])
    self.write(content)
    self.close()


def one_deal(content):
    deal, raw_targets = content.split(), []
    for j in range(len(deal) - 1):
        if deal[j] == 'Р’С…РѕРґ:':
            raw_entry = float(deal[j + 1])
        elif deal[j] == 'РўР°СЂРіРµС‚:':
            k = j + 1
            while deal[k] != 'Р’С‹С…РѕРґ:':
                raw_targets.append(float(deal[k].replace(',', '')))
                k += 1

        elif deal[j] == 'Р’С‹С…РѕРґ:':
            raw_close = float(deal[j + 1])
        elif deal[j] == 'BANK:':
            raw_bank = int(deal[j + 1])

    deal_dict = {
        "BANK": raw_bank,
        "Вход": raw_entry,
        "Таргет": raw_targets,
        "Выход": raw_close
    }
    return deal_dict


def main():
    content = read_data('deals.txt').split('-----')
    result = []
    for raw_deal in content:
        deal_dict = one_deal(raw_deal)
        if deal_dict is not None:
            result.append(
                StrategyDeal(deal_dict["Вход"], deal_dict["Таргет"], deal_dict["Выход"], deal_dict["BANK"])
            )

    write_data('out.txt', result)


if __name__ == '__main__':
    main()

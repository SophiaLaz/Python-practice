class StrategyDeal:
    def __init__(self, entry, targets, close, bank):
        self.entry, self.targets, self.close, self.bank = entry, targets, close, bank


    def get_targets(self):
        return self.targets

    def get_target_percents(self):
        for i in range(len(self.targets)):
            per = round(self.targets[i] / self.entry, 3)
        return per

    def get_target_banks(self):
        for i in range(len(self.targets)):
            bank = round(self.bank * per[i], 3)
        return bank

    def __str__(self):
        return "BANK: " + str(self.bank)


def read_data(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    return content


def write_data(file_name, data):
    file = open(file_name, 'w')
    content = "".join(data)
    file.write(content)
    file.close()


def main():
    content = read_data('deals.txt')

    deal = StrategyDeal
    for line in content:

        if line != "-----":

            line = line.strip()

            if 'Вход: ' in line:
                line = line.replace('Вход: ', '')
                entry = float(line)
                deal.entry = entry

            elif 'Таргет: ' in line:
                line = line.replace('Таргет: ', '')
                targets = list(map(float, line.split(';')))
                deal.entry = targets

            elif 'Выход: ' in line:
                line = line.replace('Выход: ', '')
                close = float(line)
                deal.close = close

            elif 'BANK: ' in line:
                line = line.replace('BANK: ', '')
                bank = int(line)
                deal.bank = bank

        print(deal.str)

    result = content
    write_data('out.txt', result)


if __name__ == '__main__':
    main()

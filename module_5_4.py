class Building:
    total = None

    def __init__(self, total):
        self.total = total

    for total in range(40):
        total += 1
        print('Построено жилых домов - ', total)

import calculate as calc

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')

    matrix = calc.Calculate(list)

    return matrix.get_calculations()

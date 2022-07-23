

def exchange_money(budget: float, exchange_rate: float) -> float:
    return budget/exchange_rate


def get_change(budget: float, exchanging_value: float) -> float:
    return budget-exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    return denomination*number_of_bills


def get_number_of_bills(budget: float, denomination: int) -> int:
    return budget//denomination


def exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination: int) -> int:
    new_exchange_rate = exchange_rate*(1 + spread/100)
    new_budget = budget/new_exchange_rate
    return get_number_of_bills(new_budget, denomination)*denomination


def non_exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination: int) -> int:
    new_exchange_rate = exchange_rate*(1 + spread/100)
    new_budget = budget/new_exchange_rate
    return int(new_budget - exchangeable_value(budget, exchange_rate, spread, denomination))

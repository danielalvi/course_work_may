import pytest

from utils import get_last_values, get_formated_data


def get_filtered_data(test_date):
    assert get_filtered_data(test_date) == [
        {
            "id": 921286598,
            "state": "EXECUTED",
            "date": "2018-03-09T23:57:37.537412",
            "operationAmount": {
                "amount": "25780.71",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 26406253703545413262",
            "to": "Счет 20735820461482021315"
        },
        {
            "id": 207126257,
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961",
            "operationAmount": {
                "amount": "92688.46",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 35737585785074382265"
        },
        {
            "id": 957763565,
            "state": "EXECUTED",
            "date": "2019-01-05T00:52:30.108534",
            "operationAmount": {
                "amount": "87941.37",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 46363668439560358409",
            "to": "Счет 18889008294666828266"
        },
        {
            "id": 667307132,
            "state": "EXECUTED",
            "date": "2019-07-13T18:51:29.313309",
            "operationAmount": {
                "amount": "97853.86",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 1308795367077170",
            "to": "Счет 96527012349577388612"
        }
    ]



def tet_get_values(test_data):
    data = get_last_values(test_data,4)
    assert [x["data"]for x in data] == ["2018-03-09T23:57:37.537412","2019-07-15T11:47:40.496961", "2019-01-05T00:52:30.108534", "2019-07-13T18:51:29.313309"]


def test_formated_data(test_data):
    data = get_formated_data(test_data)
    assert data == ["19.11.2019 Перевод организации\nMaestro 7810 84 ** **** 5568 ->Счет ** 2869\n30153.72 руб",
                   "13.11.2019 Перевод со счета на счет\nСчет 3861 14 ** **** 9794 -> Счет ** 8125\n62814.53 руб.",
                   "30.10.2019 Перевод с карты на счет\nVisaGold 7756 67 ** **** 2839 -> Счет ** 9453\n23036.03 руб.",
                   "29.09.2019 Перевод со счета на счет\nСчет 3542 14 ** **** 9637 -> Счет ** 4961\n45849.53 USD"
                   ]





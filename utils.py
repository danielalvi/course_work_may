import json
from datetime import datetime


def get_data():
    with open('operation.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data



def get_filtered_data(data, filter_empty_from=False):
    data = [x for x in data if "state" in x["state"] == "EXECUTED"]
    if filter_empty_from:
        data = [x for x in data if "from" in x]
    return data


def get_last_values(data, count_last_values):
    data = sorted(data, key=lambda x: x["data"], reverse=True)
    data = data[:count_last_values]
    return data



def get_formated_data(data):
    formated_data = []
    for row in data:
        date = datetime.strptime(row["date"],"%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = row["description"]
        recipient = f"{row['to'].split()[0]}**{row['to'][-4:]}"
        operation_amount = f"{row['operationAmount']['amount']}{row['operationAmount']['currency']['name']}"
        if "from" in row:
            sender = row["from"].split()
            from_bill = sender.pop(-1)
            from_bill = f"{from_bill[:4]}{from_bill[4:6]}** **** {from_bill[-4:]}"
            from_info = "".join(sender)
        else:
            from_info,from_bill = "", ""
        formated_data.append(f"""\
{date}{description}
{from_info}{from_bill} -> {recipient}
{operation_amount}""")
    return formated_data

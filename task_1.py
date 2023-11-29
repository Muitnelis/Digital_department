import json


FILENAME = "input.json"


def task() -> int:
    ans = 0
    with open(FILENAME) as f:
        json_data = json.load(f)

    for i in json_data:
        ans += i['score'] * i['weight']
    return round(ans, 3)


if __name__ == '__main__':
    print(task())

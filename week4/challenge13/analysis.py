# coding=utf-8
import json
import pandas as pd


def analysis(file, user_id):
    with open(file) as f:
        data = json.loads(f.read())
    df = pd.DataFrame(data)
    times = len(df[df['user_id'] == user_id])
    minutes = df[df['user_id'] == user_id]['minutes'].sum()
    return times, minutes

if __name__ == '__main__':
    analysis()
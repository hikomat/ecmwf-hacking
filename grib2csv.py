import pandas as pd
import numpy as np
import sys
import os


def pivot(oname, tokens):
    d = pd.DataFrame(tokens)
    d.columns = ['lat', 'lon', 'v', 'date', 'step', 'steprange', 'col']
    d[['lat', 'lon', 'v']] = d[['lat', 'lon', 'v']].astype(float)
    d[['step', 'steprange']] = d[['step', 'steprange']].astype(int)
    # print(d.shape, d.isnull().sum().sum())
    p = pd.pivot_table(d, 'v', ['date', 'step'], ['col', 'lat', 'lon'], np.mean)
    p.columns = list(map(lambda x: '_'.join(map(str, x)), p.columns))
    p.to_csv('data/' + oname + '/' + prev_date + '-' + oname + '.csv')
    print(oname, prev_date, p.shape, p.isnull().sum().sum())


if __name__ == '__main__':

    oname = sys.argv[1]

    try:
        os.mkdir('data/' + oname)
    except:
        pass

    prev_date = None
    lines = []
    for n, line in enumerate(sys.stdin):
        if 'Latitude' not in line:
            tokens = line.strip().split()
            date = tokens[3]
            if prev_date != date and prev_date is not None:
                pivot(oname, lines)
                lines = []
            lines.append(tokens)
            prev_date = date
    pivot(oname, lines)

import pandas as pd
import glob
import os


if __name__ == '__main__':

    try:
        os.mkdir('concated')
    except:
        pass

    for directory in glob.glob('data/*'):
        print(directory)
        files = sorted(glob.glob(directory + '/*'))
        ds = []
        for fi in files:
            print(fi)
            ds.append(pd.read_csv(fi))
        d = pd.concat(ds)
        d.to_csv('concated/{}.csv'.format(directory.replace('/', '.')))

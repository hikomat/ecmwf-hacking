import pandas as pd
import glob

for directory in glob.glob('data/*'):
    print(directory)
    files = sorted(glob.glob(directory + '/*'))
    ds = []
    for fi in files:
        print(fi)
        ds.append(pd.read_csv(fi))
    d = pd.concat(ds)
    d.to_csv('concated/{}.csv'.format(directory.replace('/', '.')))

import os
import pandas as pd
import filter

for fname in os.listdir('prksn_test'):
    if fname.endswith('.csv'):
        print(fname)
        data = filter.filter(f'prksn_test/{fname}')
        data.sort_values(by=['time']).to_csv(f'processed_prksn/{fname}', sep=';', header=False, index=False, float_format='%.3f')

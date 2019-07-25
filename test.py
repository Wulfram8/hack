import os
import pandas as pd
import filter

for fname in os.listdir('ctrl_test'):
    print(fname)
    data = filter.filter(f'ctrl_test/{fname}')
    data.sort_values(by=['time']).to_csv(f'processed_ctrl/{fname}', sep=';', header=False, index=False, float_format='%.3f')

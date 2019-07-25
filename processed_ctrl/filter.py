                result.append([t, p, 0.0, 0.0, 0.0]);;0.000;0.000;0.000
                result.append([t, p, 0.0, 0.0, 0.0]);', names=['time', 'part', 'x', 'y', 'z']);0.000;0.000;0.000
                result.append([t, p, result[-(p_col - 1)][2], result[-(p_col - 1)][3], result[-(p_col - 1)][4]]);;0.000;0.000;0.000
                result.append([t, p, result[-(p_col - 1)][2], result[-(p_col - 1)][3], result[-(p_col - 1)][4]]);', names=['time', 'part', 'x', 'y', 'z']);0.000;0.000;0.000
                result.append([t, p, values[2], values[3], values[4]]);;;;
                result.append([t, p, values[2], values[3], values[4]]);', names=['time', 'part', 'x', 'y', 'z']);;;
                values = data[(data['time'] == t) & (data['part'] == p)].values[0];;0.000;0.000;0.000
                values = data[(data['time'] == t) & (data['part'] == p)].values[0];', names=['time', 'part', 'x', 'y', 'z']);0.000;0.000;0.000
            elif len(result) > p_col:;;;;
            elif len(result) > p_col:;', names=['time', 'part', 'x', 'y', 'z']);;;
            else:;', names=['time', 'part', 'x', 'y', 'z']);0.000;0.000;0.000
            else:;;0.000;0.000;0.000
            if not data[(data['time'] == t) & (data['part'] == p)].empty:;', names=['time', 'part', 'x', 'y', 'z']);;;
            if not data[(data['time'] == t) & (data['part'] == p)].empty:;;;;
        for p in parts:;', names=['time', 'part', 'x', 'y', 'z']);;;
        for p in parts:;;;;
    # result = [[0.0, 0.0, 0.0, 0.0, 0.0,] for i in range(20)];;0.000;0.000;0.000
    # result = [[0.0, 0.0, 0.0, 0.0, 0.0,] for i in range(20)];', names=['time', 'part', 'x', 'y', 'z']);0.000;0.000;0.000
    data = pd.read_csv(file, sep=';', names=['time', 'part', 'x', 'y', 'z']);;;
    data = pd.read_csv(file, sep=';;0.000;0.000;0.000
    file = open(path, 'r');;0.000;0.000;0.000
    file = open(path, 'r');', names=['time', 'part', 'x', 'y', 'z']);0.000;0.000;0.000
    for t in set(data['time']):;', names=['time', 'part', 'x', 'y', 'z']);0.000;0.000;0.000
    for t in set(data['time']):;;0.000;0.000;0.000
    p_col = len(parts);', names=['time', 'part', 'x', 'y', 'z']);0.000;0.000;0.000
    p_col = len(parts);;0.000;0.000;0.000
    parts = set(data['part']);;;;
    parts = set(data['part']);', names=['time', 'part', 'x', 'y', 'z']);;;
    print(time.time() - start_time);;;;
    print(time.time() - start_time);', names=['time', 'part', 'x', 'y', 'z']);;;
    result = [];', names=['time', 'part', 'x', 'y', 'z']);0.000;0.000;0.000
    result = [];;0.000;0.000;0.000
    return pd.DataFrame(result, columns=['time', 'part', 'x', 'y', 'z']);', names=['time', 'part', 'x', 'y', 'z']);0.000;0.000;0.000
    return pd.DataFrame(result, columns=['time', 'part', 'x', 'y', 'z']);;0.000;0.000;0.000
    start_time = time.time();;0.000;0.000;0.000
    start_time = time.time();', names=['time', 'part', 'x', 'y', 'z']);0.000;0.000;0.000
def filter(path):;', names=['time', 'part', 'x', 'y', 'z']);0.000;0.000;0.000
def filter(path):;;0.000;0.000;0.000
import pandas as pd;;0.000;0.000;0.000
import pandas as pd;', names=['time', 'part', 'x', 'y', 'z']);0.000;0.000;0.000
import time;;;;
import time;', names=['time', 'part', 'x', 'y', 'z']);;;

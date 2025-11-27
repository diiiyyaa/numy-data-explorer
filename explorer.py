# explorer.py
import numpy as np
import pandas as pd
import time

def load_csv_to_numpy(path, delimiter=',', usecols=None):
    df = pd.read_csv(path, delimiter=delimiter, usecols=usecols)
    return df.values, list(df.columns)

def array_info(arr):
    return {
        'shape': arr.shape,
        'dtype': arr.dtype,
        'size': arr.size,
        'ndim': arr.ndim,
        'min': float(np.min(arr)) if np.issubdtype(arr.dtype, np.number) else None,
        'max': float(np.max(arr)) if np.issubdtype(arr.dtype, np.number) else None
    }

def axis_statistics(arr, axis=None):
    # returns dict of summary stats
    stats = {}
    if np.issubdtype(arr.dtype, np.number):
        stats['mean'] = np.nanmean(arr, axis=axis).tolist()
        stats['median'] = np.nanmedian(arr, axis=axis).tolist()
        stats['std'] = np.nanstd(arr, axis=axis).tolist()
        stats['sum'] = np.nansum(arr, axis=axis).tolist()
    else:
        stats['error'] = 'Non-numeric dtype'
    return stats

def reshape_array(arr, new_shape):
    return arr.reshape(new_shape)

def broadcast_example(arr, vector):
    # broadcast vector across rows (example)
    return arr + vector

def save_array_npy(path, arr):
    np.save(path, arr)

def load_array_npy(path):
    return np.load(path + '.npy')

def save_arrays_npz(path, **arrays):
    # save multiple arrays; call like save_arrays_npz('out', a=a, b=b)
    np.savez(path, **arrays)

def benchmark_operation(arr, op='sum', repetitions=5):
    """Compare numpy vs python list for the given op.
       op can be 'sum' or 'mean' or 'dot' etc."""
    results = {}
    # prepare list version (nested lists if 2D)
    pylist = arr.tolist()

    def time_fn(fn):
        t0 = time.perf_counter()
        for _ in range(repetitions):
            fn()
        return (time.perf_counter() - t0) / repetitions

    if op == 'sum':
        results['numpy'] = time_fn(lambda: np.sum(arr))
        results['pylist'] = time_fn(lambda: sum(sum(row) for row in pylist) if arr.ndim==2 else sum(pylist))
    elif op == 'mean':
        results['numpy'] = time_fn(lambda: np.mean(arr))
        results['pylist'] = time_fn(lambda: (sum(sum(row) for row in pylist) / (arr.size)) if arr.ndim==2 else (sum(pylist)/len(pylist)))
    else:
        raise ValueError('Unsupported op')
    return results

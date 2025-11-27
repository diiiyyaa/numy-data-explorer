# app.py
import streamlit as st
import numpy as np
from explorer import load_csv_to_numpy, array_info, axis_statistics, reshape_array, save_array_npy, load_array_npy, benchmark_operation

st.title("NumPy Data Explorer")

uploaded = st.file_uploader("Upload CSV", type=['csv'])
if uploaded:
    arr, cols = load_csv_to_numpy(uploaded)
    st.write("Columns:", cols)
    st.write("Array shape:", arr.shape)
    st.dataframe(arr[:10])               # show first 10 rows

    st.header("Array Info")
    st.json(array_info(arr))

    st.header("Axis statistics")
    axis = st.selectbox("Axis (None for full)", [None, 0, 1])
    st.json(axis_statistics(arr, axis=axis))

    st.header("Reshape / Broadcast")
    if st.button("Reshape to (rows, -1)"):
        try:
            new = reshape_array(arr, (arr.shape[0], -1))
            st.write("Reshaped:", new.shape)
        except Exception as e:
            st.error(str(e))

    st.header("Save / Load")
    if st.button("Save as out.npy"):
        save_array_npy("out", arr)
        st.success("Saved to out.npy (in app folder)")
    if st.button("Load out.npy"):
        try:
            loaded = load_array_npy("out")
            st.write("Loaded shape:", loaded.shape)
        except Exception as e:
            st.error(str(e))

    st.header("Benchmark (NumPy vs Python lists)")
    op = st.selectbox("Operation", ['sum', 'mean'])
    if st.button("Run benchmark"):
        res = benchmark_operation(arr.astype(float), op=op, repetitions=10)
        st.write(res)
        bigger = "NumPy faster" if res['numpy'] < res['pylist'] else "Python list faster (rare)"
        st.warning(bigger)

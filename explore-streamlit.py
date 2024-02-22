import streamlit as st
import matplotlib.pyplot as plt
import random
import subprocess
import os

if st.button("Steve"):
    st.name = "Steve"
if st.button("Alice"):
    st.name = "Alice"

if hasattr(st, "name"):
    st.write(st.name)
    
with open(__file__) as fp:
    st.code(fp.read())

st.write(os.environ)

output = subprocess.check_output("ps -uxww", shell=True)
st.write(output.decode().split("\n"))

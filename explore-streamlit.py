import streamlit as st

if st.button("Steve"):
    st.name = "Steve"
if st.button("Alice"):
    st.name = "Alice"

if hasattr(st, "name"):
    st.write(st.name)
    
with open(__file__) as fp:
    st.code(fp.read())


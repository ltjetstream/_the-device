import streamlit as st
num1 = st.number_input('Digite o primeiro número:')
num2 = st.number_input('Digite o outro número: ')

if st.button('somar'):
 res = num1 + num2
 st.text("resultado: ")
 st.title(res)

if st.button('subtrair'):
  sub = num1 - num2
  st.text("resultado: ")
  st.title(sub)

if st.button('multiplicar'):
   mult = num1 * num2
   st.text("resultado: ")
   st.title(mult)

if st.button('dividir'):
  div = num1 / num2
  st.text("resultado: ")
  st.title(div)
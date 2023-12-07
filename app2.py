import streamlit as st
import random


st.title(' ------------ \n Par ou Ímpar \n ------------')

reiniciar = st.button("Reiniciar o Jogo")

while reiniciar:
  
  numero = st.number_input('Escolha um número de dedos', min_value = 0, max_value = 5, step = 1)
  escolha = st.radio('Par ou Ímpar?', ['Par', 'Ímpar'])
  
  if st.button('Começar'):
    num = random.randint(0, 5)
    total = numero + num
    result = 'Par' if total%2==0 else 'Ímpar'
    vitoria = escolha.lower() == result.lower()
  
    st.write(f'Seu número: {numero}')
    st.write(f'Número da CPU: {num}')
    st.write(f'Total: {total}')
    st.write(f'vitoria = {resultado}')
  
    if vitoria:
      st.success('Parabéns - Você venceu.')
    else:
      st.error("Você perdeu...")
      st.image("https://imgb.ifunny.co/images/aae9b8b5530bbae969d8b45c5c39433167904d3d009fc17f46aed93117c84de0_1.webp")
  else:
    break

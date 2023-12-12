import streamlit as st
import random

def main():
    st.title(' ------------ \n Par ou Ímpar \n ------------')
    
    session_state = st.session_state
    
    if 'reiniciar' not in session_state:
        session_state.reiniciar = False

    if not session_state.reiniciar:
        reiniciar_button_placeholder = st.empty()
        reiniciar = reiniciar_button_placeholder.button("Iniciar o Jogo")

        if reiniciar:
            session_state.reiniciar = True
            reiniciar_button_placeholder.empty()  # Remove o botão após ser clicado

    if session_state.reiniciar:
        numero = st.number_input('Escolha um número de dedos', min_value=0, max_value=5, step=1)
        escolha = st.radio('Par ou Ímpar?', ['Par', 'Ímpar'])

        if st.button('Começar'):
            num = random.randint(0, 5)
            total = numero + num
            result = 'Par' if total % 2 == 0 else 'Ímpar'
            vitoria = escolha.lower() == result.lower()

            st.write(f'Seu número: {numero}')
            st.write(f'Número da CPU: {num}')
            st.write(f'Total: {total}')
            
            if vitoria:
                st.success('Parabéns - Você venceu.')
                st.image("https://64.media.tumblr.com/f5618a2c62b3981a681c5b8a6ca3c044/tumblr_mykk6euBYr1siega5o1_500.gif", caption="Os Schrute estão orgulhosos de você.")
            else:
                st.error("Você perdeu...")
                st.image("https://imgb.ifunny.co/images/aae9b8b5530bbae969d8b45c5c39433167904d3d009fc17f46aed93117c84de0_1.webp")

            session_state.reiniciar = st.button("Jogar Novamente", key="jogar_novamente")

if __name__ == "__main__":
    main()
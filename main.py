import streamlit as st
import speedtest

st.set_page_config(
    page_title="Teste de Velocidade",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="expanded"
)

def main():
    st.header("SpeedTest", divider=True)
    st.write('Clique no botão abaixo para iniciar o teste.')

    # Cria uma variável de sessão para armazenar o estado do teste
    if 'teste_realizado' not in st.session_state:
        st.session_state.teste_realizado = False

    if st.session_state.teste_realizado:
        # Se o teste foi realizado, mostra a opção para realizar um novo teste
        if st.button('Realizar Novo Teste'):
            st.session_state.teste_realizado = False
            st.experimental_rerun()  # Reinicia a aplicação para resetar o estado
    else:
        # Se o teste não foi realizado, mostra o botão de iniciar
        start_button = st.button('Iniciar')

        # Apenas inicia o teste se o botão for pressionado
        if start_button:
            with st.spinner('Testando a velocidade da sua internet...'):
                s = speedtest.Speedtest()
                s.get_best_server()
                download_speed = s.download() / 1_000_000  # Mbps
                upload_speed = s.upload() / 1_000_000      # Mbps
                results = s.results.dict()

                max_speed = 100  # Limite para barra de progresso

                st.write(f"Velocidade de Download: {download_speed:.2f} Mbps")
                st.progress(min(download_speed / max_speed, 1.0))

                st.write(f"Velocidade de Upload: {upload_speed:.2f} Mbps")
                st.progress(min(upload_speed / max_speed, 1.0))

                st.write(f"Ping: {results['ping']} ms")

                # Após o teste, altera o estado para que o novo botão apareça
                st.session_state.teste_realizado = True

if __name__ == "__main__":
    main()

    # CSS para o botão
st.markdown(
    """
    <style>
    /* Estilo padrão do botão */
    .stButton > button {
        background-color: #0267ab; /* Verde */
        color: white;
        font-size: 20px;
        height: 50px;
        width: 200px;
        border: none;
        border-radius: 5px;
        transition: background-color 0.3s, color 0.3s; /* Transição suave */
    }

    /* Efeito hover */
    .stButton > button:hover {
        background-color: #008fee; /* Cor ao passar o mouse */
        color: #000000; /* Cor do texto ao passar o mouse */
        border: 1px solid #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

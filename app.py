import streamlit as st
from music_recommender import recomendar_musicas

st.set_page_config(
    page_title="Moodify",
    page_icon="🎧",
    layout="centered"
)

# 🎨 Estilo personalizado
st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
    }
    .title {
        text-align: center;
        font-size: 2.5em;
        color: #2E86AB;
        font-weight: bold;
    }
    .subtitle {
        text-align: center;
        font-size: 1.2em;
        color: #555;
        margin-bottom: 2em;
    }
    .recommendation {
        background-color: #fff;
        padding: 1em;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 1em;
    }
    </style>
""", unsafe_allow_html=True)

# 🎵 Cabeçalho
st.markdown('<div class="title">🎧 Moodify</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Descubra músicas baseadas no seu humor 🎶</div>', unsafe_allow_html=True)

# 😄 Seletor de humor
humor = st.selectbox("💬 Como você está se sentindo agora?", ["positivo", "neutro", "negativo"])

# 🎼 Gêneros
generos = st.multiselect(
    "🎵 Escolha seus estilos musicais favoritos:",
    ["pop", "rock", "hip-hop", "jazz", "classical", "electronic", "country", "blues", "funk", "mpb", "reggae"]
)

# 🎶 Recomendar
if st.button("🔍 Buscar recomendações"):
    if not humor or not generos:
        st.warning("⚠️ Por favor, selecione o seu humor e pelo menos um estilo musical.")
    else:
        with st.spinner("🔄 Gerando recomendações musicais com base no seu humor..."):
            recomendacoes = recomendar_musicas(humor, generos)
        st.success("✅ Aqui estão suas músicas personalizadas:")
        
        for musica in recomendacoes:
            st.markdown(f"""
                <div class="recommendation">
                    <strong>{musica['nome']}</strong><br>
                    🎤 {musica['artista']}<br>
                    <a href="{musica['link']}" target="_blank">▶️ Ouvir no Spotify</a>
                </div>
            """, unsafe_allow_html=True)

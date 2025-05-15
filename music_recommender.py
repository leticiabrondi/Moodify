import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

if not client_id or not client_secret:
    raise ValueError("Configure SPOTIPY_CLIENT_ID e SPOTIPY_CLIENT_SECRET no arquivo .env")

client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

HUMOR_MAP = {
    "positivo": {"valence": 0.8, "energy": 0.7},
    "neutro": {"valence": 0.5, "energy": 0.5},
    "negativo": {"valence": 0.3, "energy": 0.3},
}

def recomendar_musicas(humor, generos, quantidade=5):
    if humor not in HUMOR_MAP:
        raise ValueError("Humor inválido. Use: positivo, neutro ou negativo")

    params = HUMOR_MAP[humor]
    seed_genres = generos[:5]

    results = sp.recommendations(
        seed_genres=seed_genres,
        limit=quantidade,
        target_valence=params["valence"],
        target_energy=params["energy"]
    )

    musicas = []
    for track in results['tracks']:
        musicas.append({
            "nome": track['name'],
            "artista": track['artists'][0]['name'],
            "link": track['external_urls']['spotify']
        })

    return musicas

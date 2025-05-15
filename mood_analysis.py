from textblob import TextBlob

def analisar_humor(texto):
    """
    Analisa o sentimento do texto e classifica como positivo, neutro ou negativo.
    
    Args:
        texto (str): Frase descritiva do humor do usuário.

    Returns:
        str: Classificação de humor ('positivo', 'neutro', 'negativo')
    """
    blob = TextBlob(texto)
    polaridade = blob.sentiment.polarity

    if polaridade > 0.2:
        return "positivo"
    elif polaridade < -0.2:
        return "negativo"
    else:
        return "neutro"

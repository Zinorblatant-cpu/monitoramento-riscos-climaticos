from datetime import datetime
from collections import defaultdict

def verificar_risco_incendio(dados_climaticos):
    """
    Avalia a previsão dos próximos 5 dias para identificar risco de incêndios florestais.

    Critérios considerados:
    - Temperatura máxima > 35°C
    - Umidade média < 40%
    - Vento máximo > 30 km/h
    - Probabilidade de chuva < 10%

    Os dados são agrupados por dia e um 'índice de risco' é calculado para cada um.
    """

    print("\n🔥 PREVISÃO DE RISCO DE INCÊNDIO FLORESTAL (próximos 5 dias):")

    # Dicionário para organizar os dados por data (formato YYYY-MM-DD)
    risco_por_dia = defaultdict(list)

    # Etapa 1: Organiza as previsões por data
    for previsao in dados_climaticos['list']:
        momento_previsto = datetime.fromtimestamp(previsao['dt'])
        data_formatada = momento_previsto.strftime('%Y-%m-%d')

        try:
            temperatura_max = previsao['main']['temp_max']
            umidade = previsao['main']['humidity']
            vento_ms = previsao['wind']['speed']
            prob_chuva = previsao['pop']
        except KeyError:
            continue  # Pula se faltar algum campo necessário

        # Converte vento de m/s para km/h
        vento_kmh = vento_ms * 3.6

        # Armazena os dados no agrupamento do dia correspondente
        risco_por_dia[data_formatada].append({
            'temp': temperatura_max,
            'humidity': umidade,
            'wind': vento_kmh,
            'pop': prob_chuva
        })

    alerta_incendio_detectado = False

    # Etapa 2: Avalia o risco para cada dia
    for data, registros in sorted(risco_por_dia.items()):
        temperatura_max_dia = max(r['temp'] for r in registros)
        umidade_media = sum(r['humidity'] for r in registros) / len(registros)
        vento_max_dia = max(r['wind'] for r in registros)
        chuva_media = sum(r['pop'] for r in registros) / len(registros)

        # Ignora dias muito frios, sem risco de incêndio
        if temperatura_max_dia < 10:
            continue

        # Cálculo do índice de risco com base nos critérios
        indice_risco = 0
        if temperatura_max_dia > 35:
            indice_risco += 1
        if umidade_media < 40:
            indice_risco += 1
        if vento_max_dia > 30:
            indice_risco += 1
        if chuva_media < 0.1:
            indice_risco += 1

        # Etapa 3: Exibe os alertas com base no risco identificado
        if indice_risco >= 3:
            alerta_incendio_detectado = True
            print(f"🔴 ALTO RISCO DE INCÊNDIO em {data}")
            print(f"🌡️ Temp. Máxima: {temperatura_max_dia:.1f}°C | 💧 Umidade Média: {umidade_media:.0f}%")
            print(f"🌬️ Vento Máx.: {vento_max_dia:.1f} km/h | 🌦️ Chuva: {chuva_media * 100:.0f}%")
            print("-" * 60)

        elif indice_risco == 2:
            alerta_incendio_detectado = True
            print(f"⚠️ RISCO MODERADO DE INCÊNDIO em {data}")
            print(f"🌡️ Temp. Máxima: {temperatura_max_dia:.1f}°C | 💧 Umidade Média: {umidade_media:.0f}%")
            print("-" * 60)

        elif indice_risco == 1:
            print(f"🟡 RISCO BAIXO DE INCÊNDIO em {data}")
            print(f"🌡️ Temp. Máxima: {temperatura_max_dia:.1f}°C | 💧 Umidade Média: {umidade_media:.0f}%")
            print("-" * 60)

    # Mensagem final se nenhum risco for detectado
    if not alerta_incendio_detectado:
        print("✅ Nenhum risco significativo de incêndio nos próximos 5 dias.")

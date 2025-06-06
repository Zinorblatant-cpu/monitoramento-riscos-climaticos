from datetime import datetime
from collections import defaultdict

def verificar_clima_seco_e_quente(dados_previsao):
    """
    Analisa as previsões dos próximos 5 dias para identificar:
    
    - 🔥 Seca: Temperaturas ≥ 30°C e pouca chance de chuva (pop < 10%) por 5 dias consecutivos.
    - 🌡️ Onda de calor: Temperaturas máximas acima de 30°C por 3 dias consecutivos.
    
    Os dados são agrupados por data para facilitar a análise diária.
    """

    # Contadores de dias consecutivos com clima extremo
    dias_secos = 0
    dias_quentes = 0
    alerta_emitido = False

    print("\n☀️ ANÁLISE DE CLIMA SECO E QUENTE (próximos 5 dias):")

    # Dicionário para agrupar previsões por data (ex: '2025-06-03')
    previsoes_por_dia = defaultdict(list)

    # Etapa 1: Coleta e organiza as previsões por dia
    for previsao in dados_previsao['list']:  
        try:
            # Extrai e formata o timestamp da previsão
            horario_previsto = datetime.fromtimestamp(previsao['dt'])
            data_chave = horario_previsto.strftime('%Y-%m-%d')

            # Extrai probabilidade de chuva e temperatura máxima
            prob_chuva = previsao['pop']
            temperatura_max = previsao['main']['temp_max']

            # Armazena as informações no agrupamento diário
            previsoes_por_dia[data_chave].append({
                'pop': prob_chuva,
                'temp_max': temperatura_max
            })

        except KeyError as erro:
            campo_ausente = erro.args[0]
            print(f"⚠️ Campo ausente: '{campo_ausente}' na previsão de {horario_previsto}")
            continue

    # Etapa 2: Avalia as condições por dia
    for data, registros in previsoes_por_dia.items():
        # Calcula a média da chance de chuva e a maior temperatura registrada no dia
        media_chuva = sum(item['pop'] for item in registros) / len(registros)
        temperatura_dia = max(item['temp_max'] for item in registros)

        # Exibe resumo diário
        print(f"📅 Dia {data} | Temp. Máxima: {temperatura_dia:.1f}°C | Chuva Média: {media_chuva * 100:.0f}%")

        # Avalia risco de seca
        if media_chuva < 0.1 and temperatura_dia >= 30:
            dias_secos += 1
            print(f"⚠️ RISCO DE SECA: Clima seco e quente | Temp={temperatura_dia:.1f}°C | Chuva={media_chuva * 100:.0f}%")
            if dias_secos >= 5:
                print(f"🔴 ALERTA: Período seco prolongado detectado desde {data}")
                alerta_emitido = True
        else:
            dias_secos = 0  # Reinicia contagem se o padrão for interrompido

        # Avalia risco de onda de calor
        if temperatura_dia >= 30:
            dias_quentes += 1
            print(f"🌡️ RISCO DE ONDA DE CALOR: Temp. elevada de {temperatura_dia:.1f}°C")
            if dias_quentes >= 3:
                print(f"🔴 ALERTA: Onda de calor identificada — mais de 3 dias acima de 30°C")
                alerta_emitido = True
        else:
            dias_quentes = 0  # Reinicia contagem se houver alívio térmico

    # Conclusão: Nenhum risco relevante encontrado
    if not alerta_emitido:
        print("✅ Nenhum risco climático significativo foi detectado.")

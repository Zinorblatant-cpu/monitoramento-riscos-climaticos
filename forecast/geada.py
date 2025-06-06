from datetime import datetime
from collections import defaultdict

def verificar_geada(dados_climaticos):
    """
    Avalia a previsão dos próximos 5 dias para identificar risco de geada.

    Critérios:
    - Temperatura mínima do dia inferior a 0°C
    - Céu limpo ou parcialmente nublado (sem chuva ou neve)

    Os dados são agrupados por dia e analisados para detecção de períodos consecutivos de frio.
    """

    dias_com_geada = 0
    alerta_geada = False

    print("\n❄️ PREVISÃO DE GEADA (próximos 5 dias):")

    # Agrupa previsões por data (ex: '2024-07-01')
    previsoes_por_dia = defaultdict(list)

    # Etapa 1: Organiza os dados por dia
    for previsao in dados_climaticos['list']:
        try:
            temperatura_min = previsao['main']['temp_min']
            descricao_tempo = previsao['weather'][0]['description'].lower()

            momento = datetime.fromtimestamp(previsao['dt'])
            chave_data = momento.strftime('%Y-%m-%d')

        except KeyError as erro:
            campo_faltando = erro.args[0]
            print(f"⚠️ Campo ausente: '{campo_faltando}' em {momento}")
            continue

        # Armazena os dados climáticos do período
        previsoes_por_dia[chave_data].append({
            'temp_min': temperatura_min,
            'descricao': descricao_tempo
        })

    # Etapa 2: Analisa a previsão agrupada por dia
    for data, registros in previsoes_por_dia.items():
        menor_temperatura = min(item['temp_min'] for item in registros)
        tempo_dia = registros[0]['descricao']

        # Verifica condições favoráveis à geada
        if menor_temperatura < 0 and ('clear' in tempo_dia or 'clouds' in tempo_dia):
            dias_com_geada += 1
            print(f"❄️ ALERTA DE GEADA: Temperatura de {menor_temperatura:.1f}°C prevista para {data}")
            print(f"☁️ Condição do tempo: {tempo_dia.title()}")
            print("-" * 60)

            if dias_com_geada >= 5:
                alerta_geada = True
                print(f"⚠️ ALERTA: Período prolongado de temperaturas negativas detectado a partir de {data}")
                break
        else:
            dias_com_geada = 0  # Reinicia o contador se um dia não atender aos critérios

    # Mensagem final caso nenhum alerta tenha sido acionado
    if not alerta_geada:
        print("✅ Nenhum período prolongado de geada previsto para os próximos 5 dias.")

from datetime import datetime

def verificar_enchentes(dados_climaticos):
    """
    Avalia os dados de previsão para as próximas 24 horas a fim de detectar risco de enchentes.

    Critérios utilizados:
    - Volume de chuva ≥ 50 mm em um período de 3 horas
    - Probabilidade de chuva ≥ 80% com temperatura abaixo de 30°C

    Exibe alertas no terminal quando algum desses critérios é atendido.
    """

    alerta_enchente = False  # Indica se algum risco foi identificado

    print("\n🌊 PREVISÃO DE ENCHENTES (próximas 24 horas):")

    # Avalia os 8 primeiros blocos de previsão (24 horas em intervalos de 3h)
    for previsao in dados_climaticos['list'][:8]:
        # Converte o timestamp para data/hora legível
        momento = datetime.fromtimestamp(previsao['dt'])
        horario_formatado = momento.strftime('%d/%m %H:%M')

        try:
            # Volume de chuva nas últimas 3 horas (mm)
            volume_chuva = previsao.get('rain', {}).get('3h', 0)

            # Probabilidade de chuva (%)
            chance_chuva = previsao['pop'] * 100

            # Temperatura máxima registrada no período
            temperatura_max = previsao['main']['temp_max']

        except KeyError as erro:
            campo_ausente = erro.args[0]
            print(f"⚠️ Campo ausente: '{campo_ausente}' às {horario_formatado}")
            continue

        # Critério 1: chuva intensa recente
        if volume_chuva >= 50:
            alerta_enchente = True
            print(f"⚠️ ALERTA DE CHUVA INTENSA: {volume_chuva:.1f} mm nas últimas 3h às {horario_formatado}")

        # Critério 2: alta chance de chuva + temperatura não muito alta
        elif chance_chuva >= 80 and temperatura_max < 30:
            alerta_enchente = True
            print(f"🟡 RISCO POTENCIAL DE ENCHENTE: {chance_chuva:.0f}% de chance de chuva às {horario_formatado}")

    # Caso nenhum critério tenha sido atendido
    if not alerta_enchente:
        print("✅ Nenhum risco significativo de enchente nas próximas 24 horas.")

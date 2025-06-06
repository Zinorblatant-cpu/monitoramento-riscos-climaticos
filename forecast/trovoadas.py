from datetime import datetime

def verificar_trovoadas(dados_climaticos):
    """
    Analisa a previsão para as próximas 24 horas em busca de trovoadas.

    Utiliza os dados fornecidos pela API para identificar tempestades elétricas,
    baseando-se nas descrições climáticas e na probabilidade de chuva.
    """

    alerta_trovoada = False  # Flag para indicar se foi detectado algum risco

    print("\n⚡ PREVISÃO DE TROVOADAS (próximas 24 horas):")

    # Percorre os 8 primeiros períodos de 3h (totalizando 24h)
    for previsao in dados_climaticos['list'][:8]:
        # Converte o timestamp para data legível
        horario_previsto = datetime.fromtimestamp(previsao['dt'])
        horario_formatado = horario_previsto.strftime('%d/%m %H:%M')

        # Obtém descrição principal e detalhada do tempo
        tempo_principal = previsao['weather'][0]['main']
        descricao_clima = previsao['weather'][0]['description']

        # Converte a probabilidade de precipitação para porcentagem
        chance_chuva = previsao['pop'] * 100

        # Verifica se o termo "thunderstorm" aparece na descrição principal
        if 'thunderstorm' in tempo_principal.lower():
            alerta_trovoada = True

            # Emite alerta detalhado ao usuário
            print(f"⚠️ ALERTA DE TROVOADA: '{descricao_clima.title()}' previsto para {horario_formatado}")
            print(f"🌧️ Chance de chuva: {chance_chuva:.0f}%")
            print("-" * 60)

    # Caso nenhuma trovoada tenha sido detectada
    if not alerta_trovoada:
        print("✅ Nenhuma trovoada prevista nas próximas 24 horas.")

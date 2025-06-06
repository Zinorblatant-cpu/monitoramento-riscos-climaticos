from datetime import datetime

def verificar_vento_forte(dados_climaticos):
    """
    Analisa as próximas 24 horas para identificar ventos fortes (> 50 km/h).
    
    Verifica os 8 primeiros períodos de previsão (3h cada), converte a velocidade
    do vento de m/s para km/h e emite alertas se forem detectadas rajadas acima do limite.
    """

    # Flag para indicar se foi identificado vento forte
    alerta_vento_forte = False

    print("\n💨 PREVISÃO DE VENTOS FORTES (próximas 24 horas):")

    # Verifica os 8 primeiros registros (correspondente a 24h)
    for previsao in dados_climaticos['list'][:8]:
        # Velocidade do vento em m/s
        velocidade_ms = previsao['wind']['speed']

        # Converte para km/h
        velocidade_kmh = velocidade_ms * 3.6

        # Converte o horário do timestamp para formato legível
        horario_previsto = datetime.fromtimestamp(previsao['dt'])
        horario_formatado = horario_previsto.strftime('%d/%m %H:%M')

        # Verifica se ultrapassa o limite de vento forte
        if velocidade_kmh > 50:
            alerta_vento_forte = True
            print(f"⚠️ VENTO FORTE: {velocidade_kmh:.1f} km/h previsto para {horario_formatado}")

    # Caso nenhum vento acima do limite seja identificado
    if not alerta_vento_forte:
        print("✅ Nenhuma ocorrência de ventos fortes nas próximas 24 horas.")

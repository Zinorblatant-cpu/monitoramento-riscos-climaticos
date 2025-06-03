import requests
import os

# Importando módulos com funções específicas para riscos climáticos
from .thunderstorms import verificar_trovoadas
from .wind import verificar_ventos_fortes
from .frost import verificar_geada
from .floods import verificar_enchentes
from .drought_heatwave import verificar_clima_seco_quente
from .wildfire import verificar_risco_incendio



# Função para limpar o terminal
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


# Função que apresenta o menu principal e executa as verificações
def exibir_menu(dados_climaticos):
    while True:
        print("🌦️ Selecione os riscos climáticos que deseja monitorar:")
        print("[1] ⚡ Raios e Tempestades")
        print("[2] 💨 Ventos Fortes (acima de 50 km/h)")
        print("[3] ❄️ Geada / Temperaturas Congelantes")
        print("[4] 💧 Inundações / Chuvas Intensas")
        print("[5] ☀️ Clima Seco e Quente (Onda de Calor e Seca)")
        print("[6] 🔥 Risco de Incêndios Florestais")
        print("[7] 🌍 Monitorar Todos os Riscos")
        print("[8] ❌ Encerrar Programa")

        try:
            opcao = int(input("Digite uma opção (1-8): "))
            limpar_terminal()

            if opcao == 8:
                print("👋 Encerrando o programa. Até logo!")
                break

            elif opcao == 1:
                verificar_trovoadas(dados_climaticos)
                input("\nPressione qualquer tecla para voltar ao menu...")
                limpar_terminal()

            elif opcao == 2:
                verificar_vento_forte(dados_climaticos)
                input("\nPressione qualquer tecla para voltar ao menu...")
                limpar_terminal()

            elif opcao == 3:
                verificar_geada(dados_climaticos)
                input("\nPressione qualquer tecla para voltar ao menu...")
                limpar_terminal()

            elif opcao == 4:
                verificar_enchentes(dados_climaticos)
                input("\nPressione qualquer tecla para voltar ao menu...")
                limpar_terminal()

            elif opcao == 5:
                verificar_clima_seco_e_quente(dados_previsao)
                input("\nPressione qualquer tecla para voltar ao menu...")
                limpar_terminal()
            
            elif opcao == 6:
                verificar_risco_incendio(dados_climaticos)
                input("\nPressione qualquer tecla para voltar ao menu...")
                limpar_terminal()

            elif opcao == 7:
                limpar_terminal()
                check_thunderstorms(dados_climaticos)
                print('-' * 60)
                check_strong_wind(dados_climaticos)
                print('-' * 60)
                check_frost(dados_climaticos)
                print('-' * 60)
                check_floods(dados_climaticos)
                print('-' * 60)
                check_dry_and_hot_weather(dados_climaticos)
                print('-' * 60)
                check_wildfire_risk(dados_climaticos)
                print('-' * 60)
                input("\nPressione qualquer tecla para voltar ao menu...")
                limpar_terminal()

            else:
                print("🚫 Opção inválida. Escolha entre 1 e 8.\n")

        except ValueError:
            limpar_terminal()
            print("❗ Entrada inválida. Por favor, digite um número.\n")


# Ponto de entrada do programa: conecta à API e inicia o menu
if __name__ == '__main__':
    # Chave da API do OpenWeatherMap
    CHAVE_API = '512569ff925265363234407e3e1cac15'

    # Coordenadas geográficas (Antártida) para teste de condições extremas
    latitude = -77.85
    longitude = 166.67

    # URL da API de previsão do tempo
    url_api = f'https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={CHAVE_API}&units=metric'

    print("📡 Conectando à API meteorológica...")
    resposta = requests.get(url_api)

    print(f"📶 Código de resposta: {resposta.status_code}")

    # Verifica se a requisição foi bem-sucedida
    if resposta.status_code != 200:
        print("❌ Erro ao obter dados da API:")
        print(resposta.json())
    else:
        print("✅ Dados recebidos com sucesso!")
        dados_recebidos = resposta.json()

        # Verifica se os dados esperados estão presentes
        if 'list' not in dados_recebidos:
            print("⚠️ Dados esperados não encontrados na resposta.")
        else:
            limpar_terminal()
            exibir_menu(dados_recebidos)  # Inicia menu com os dados carregados

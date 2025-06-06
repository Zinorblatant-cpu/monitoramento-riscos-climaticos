# 🌤️ Sistema de Monitoramento de Riscos Climáticos

## 📌 Descrição Geral

Este é um **sistema interativo de detecção de riscos climáticos** desenvolvido em Python que consome dados da **OpenWeatherMap API** para identificar condições adversas nos próximos 5 dias. Com base nas previsões, o programa permite ao usuário verificar:

- ⚡ Raios e tempestades
- 💨 Vento forte (> 50 km/h)
- ❄️ Geada / temperaturas negativas
- 💧 Enchentes ou chuva intensa
- ☀️ Seca prolongada e ondas de calor
- 🔥 Risco de incêndios florestais

O objetivo é demonstrar como podemos usar previsões climáticas para **prever e alertar sobre eventos climáticos adversos**, com uma interface simples no terminal.

---

## 🎯 Objetivo do Projeto

- Consumir dados da OpenWeatherMap API
- Detectar automaticamente condições climáticas adversas
- Apresentar alertas claros ao usuário via terminal
- Organizar o código usando boas práticas de modularização
- Estudar análise de risco com base em condições meteorológicas

Ideal tanto para **projetos acadêmicos** quanto para sistemas simples de apoio à agricultura, segurança ambiental ou planejamento urbano.

---

## 🛠️ Funcionamento Interno

### 🔁 Estrutura Modular

Cada tipo de alerta foi implementado como uma função separada dentro da pasta `forecast/`, permitindo fácil manutenção e expansão futura. As principais funções são:

| Arquivo | Função | Descrição |
|--------|--------|-----------|
| `trovoadas.py` | `verificar_trovoadas()` | Verifica se há trovoadas nas previsões |
| `vento.py` | `verificar_vento_forte()` | Detecta vento acima de 50 km/h |
| `geada.py` | `verificar_geada()` | Analisa previsão de geada |
| `enchentes.py` | `verificar_enchentes()` | Avalia chuvas fortes e risco de inundação |
| `seca_ondas_de_calor.py` | `verificar_clima_seco_e_quente()` | Identifica períodos secos com alta temperatura |
| `incendios.py` | `verificar_risco_incendio()` | Calcula risco de incêndio com base em clima |

Todas essas funções recebem o objeto `dados_climaticos`, extraído da resposta da API, e analisam os dados conforme critérios específicos.

---

## 🧮 Lógica de Detecção de Riscos

O projeto usa **critérios técnicos** para detectar cada risco. Alguns exemplos:

### 1. **Vento forte**
- Velocidade > 50 km/h
- Baseado no campo `wind.speed` (em m/s → convertido)

### 2. **Geada**
- Temperatura mínima < 0°C
- Tempo limpo ou nublado (`clear sky`, `few clouds`, etc.)

### 3. **Seca + Onda de Calor**
- Baixa probabilidade de chuva (`pop < 0.1`)
- Alta temperatura máxima (`temp_max >= 30°C`)

### 4. **Risco de Incêndio**
- Temperatura > 35°C
- Umidade média < 40%
- Vento > 30 km/h
- Baixa chance de chuva (`pop < 0.1`)

---

## 📦 Requisitos Técnicos

- Python 3.x
- Bibliotecas:
  - `requests` – Para requisições HTTP
  - `os` – Limpeza de tela no terminal

```bash
pip install requests
```

> ⚠️ A chave da API deve ser inserida diretamente no arquivo `__main__.py`.

---

## 🧪 Como o Projeto Trabalha com Dados Horários

A OpenWeatherMap retorna dados a cada 3 horas (`list`), totalizando até 40 registros (5 dias × 8 horários/dia). O projeto analisa esses dados diretamente, sem agrupamento por dia, mostrando as condições mais críticas encontradas.

Exemplo:
```python
for forecast in dados_climaticos['list'][:8]:  # Próximas 24h
    ...
```

---

## 🧩 Estrutura do Projeto

```
risco-climatico/
├── main.py                  # Menu principal e controle
├── forecast/
│   ├── trovoadas.py         # Alerta de trovoadas
│   ├── vento.py             # Alerta de vento forte
│   ├── geada.py             # Alerta de geada
│   ├── enchentes.py         # Alerta de enchentes
│   ├── seca_ondas_de_calor.py # Alerta de seca e calor
│   └── incendios.py         # Alerta de incêndios
└── README.md                # Este documento
```

---

## 🧪 Exemplo de Saída

```
🌦️ Selecione os riscos climáticos que deseja monitorar:
[1] ⚡ Raios e Tempestades
[2] 💨 Ventos Fortes (acima de 50 km/h)
[3] ❄️ Geada / Temperaturas Congelantes
[4] 💧 Inundações / Chuvas Intensas
[5] ☀️ Clima Seco e Quente (Onda de Calor e Seca)
[6] 🔥 Risco de Incêndios Florestais
[7] 🌍 Monitorar Todos os Riscos
[8] ❌ Encerrar Programa
```

Ao selecionar uma opção, o programa imprime alertas como:

```
⚠️ ALTA VELOCIDADE DO VENTO: 59.4 km/h previsto às 05/06 15:00
```

---

## 📁 Funções Principais Explicadas

### 1. `verificar_trovoadas()`
Detecta trovoadas com base no campo `weather.description`.

### 2. `verificar_vento_forte()`
Converte `wind.speed` de `m/s` para `km/h` e avisa se > 50 km/h.

### 3. `verificar_geada()`
Verifica temperaturas mínimas abaixo de 0°C com tempo claro/nublado.

### 4. `verificar_enchentes()`
Analisa volume de chuva (`rain.3h`) e chance de chuva (`pop`) para alertar sobre enchentes.

### 5. `verificar_clima_seco_e_quente()`
Combina baixa precipitação e alta temperatura para indicar seca ou onda de calor.

### 6. `verificar_risco_incendio()`
Calcula risco com base em:
- Temperatura alta
- Umidade baixa
- Vento forte
- Baixa probabilidade de chuva

---

## 📝 Benefícios do Projeto

- ✅ Uso de **API realista** (OpenWeatherMap)
- ✅ Interface interativa no terminal
- ✅ Fácil expansão para outros tipos de risco
- ✅ Boa prática de tratamento de erros e validação de campos

---

## 👨‍🏫 Integrante

- **Leonardo Lopes** RM: 565437
- **Giovanni de Lela** RM - 563066
- **Gabriel Nakamura** RM - 562221


---

## 🧾 Créditos

Desenvolvido como parte de um projeto acadêmico pela disciplina **Soluções Energéticas**, ministrada pelo professor **André**, na instituição **FIAP**.

---

## 📬 Contato

Se quiser entrar em contato ou contribuir com melhorias, fique à vontade!

---
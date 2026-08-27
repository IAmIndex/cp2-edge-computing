########################################################
######################## AGENTE ########################
########################################################

# from crewai import Agent, Task, Process, Crew


# def criar_agente():
    # relator = Agent(
    #     role="Analista de dados de computação de borda",
    #     goal="Analisar dados e criar relatórios com base nas especificações do sistema",
    #     backstory=(
    #         "Você é um analista de dados sênior especializado em fazer relatórios "
    #         "corporativos para insights úteis."
    #     ),
    #     verbose=True
    # )
    
    # return relator

# def criar_task(agente, specs, dados):
    # analisar_dados = Task(
    #     description=(
    #     f"""
    #         Considere as especificações abaixo:
    #         {specs}
            
    #         Analise os dados advindos abaixo:
    #         {dados}
            
    #         Identifique:
    #         1. Se os dados estão dentro da especificação;
    #         2. Impacto no negócio;
    #         3. Possíveis causas;
    #         4. Informações adicionais necessárias;
    #         5. Próxima ação recomendada.
            
    #         Caso o sensor apresente dados fora da especificação, direcione o relatório para a equipe de sustentação. Caso contrário, direcione-o à diretoria.
    #     """
    #     ),
    #     expected_output=(
    #         "Um relatório em Markdown com destinatário, diferença das especificações, impacto, "
    #         "possíveis causas e próximos passos. Caso os dados estejam dentro das especificações, "
    #         "informe os impactos positivos no lugar da diferença das especificações."
    #     ),
    #     agent=agente
    # )
    
    # return analisar_dados

# def criar_equipe(agentes, tasks):
    # equipe = Crew(
    #     agents=agentes,
    #     tasks=tasks,
    #     process=Process.sequential,
    #     verbose=True
    # )
    
    # return equipe

# relator = criar_agente()

specs = """
    Os dados do sensor medem a quantidade de verde em uma área, de 0 a 100%.
    
    Os dados são classificados como:
    0-10: Péssimo;
    11-30: Ruim;
    31-60: Moderado;
    61-80: Bom;
    81-100: Excelente.
    
    Dados aceitáveis são os dados acima de 60%. Ou seja, valores considerados "Bom" e "Excelente".
"""

########################################################
######################### MQTT #########################
########################################################

import paho.mqtt.client as mqtt

BROKER_URL = "test.mosquitto.org"
BROKER_PORT = 1883

client = mqtt.Client()

client.connect(BROKER_URL, BROKER_PORT)

client.subscribe("vibe_e_codas")

client.loop_start()

def on_message(client, userdata, message):
    dados = f"Certeza: {message.topic}"
    
    print(f"Mensagem recebida: {str(message.payload.decode('utf-8'))} no tópico {message.topic}")
    
    # analisar_dados = criar_task(relator, specs, dados)
    # equipe = criar_equipe([relator], [analisar_dados])
    
    # resultado = equipe.kickoff(
    #     inputs={
    #         "chamado":(
    #             "O sensor retornou uma nova leitura de dados hoje. "
    #             "Analise dentro das especificações os dados recém-chegados "
    #             "e como está afetando a empresa."
    #         )
    #     }
    # )

    # print(resultado.raw)

client.on_message = on_message

import time
time.sleep(30)

client.loop_stop()

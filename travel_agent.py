import streamlit as st
import openai
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

# Chave da API da OpenAI
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Front Page
st.set_page_config(page_title="AgenTravel", page_icon="✈️", layout="centered")
st.title("AgenTravel✈️")
st.markdown('## 📝 Seu agente de Viagem Virtual')
st.write("Planeje suas viagens com a ajuda de um agente virtual inteligente!")

# Inicializar o modelo LLM
llm = OpenAI(api_key=openai.api_key, temperature=0.7, max_tokens=2048)

# Configurar o PromptTemplate
prompt_template = PromptTemplate(input_variables=["prompt"], template="{prompt}")

# Configurar o LLMChain
def get_travel_advice(prompt_text):
    chain = LLMChain(llm=llm, prompt=prompt_template)
    response = chain.run({"prompt": prompt_text})
    return response

# Entrada do usuário - Destino
destination = st.text_input("Para onde você gostaria de viajar?")

# Entrada do usuário - Quantidade de dias
days = st.number_input("Quantos dias pretende ficar?", min_value=1, max_value=30, step=1)

# Entrada do usuário - Itinerário específico
itinerary_request = st.text_input("Tem algo específico que você gostaria de saber sobre o itinerário ou dicas? - Por exemplo: Praias, Restaurantes...")

# Botão
if st.button("Gerar Itinerário e Dicas"):
    if destination and days:
        if itinerary_request:
            prompt = (
                f"Você é um agente de viagem que fornece informações detalhadas sobre {destination} por {days} dias. {itinerary_request}. "
                "Forneça informações detalhadas sobre este destino, incluindo os lugares mais visitados, "
                "as melhores opções de hospedagem, e detalhes sobre os principais lugares para visitar e o tempo médio dos passeios. "
                "Estruture a resposta como uma lista."
            )
        else:
            prompt = (
                f"Você é um agente de viagem que fornece informações detalhadas sobre {destination} por {days} dias. "
                "Forneça informações detalhadas sobre este destino, incluindo os lugares mais visitados, "
                "as melhores opções de hospedagem, e detalhes sobre os principais lugares para visitar e o tempo médio dos passeios. "
                "Estruture a resposta como uma lista."
            )
        with st.spinner('Processando...'):
            detailed_advice = get_travel_advice(prompt)
        st.write(detailed_advice)
    else:
        st.write("Por favor, insira um destino e a quantidade de dias para sua viagem.")

# Projeto INFNET

## AgenTravel - Seu Agente de Viagem Virtual

1. Descrição da Aplicação
AgenTravel é uma aplicação web interativa que auxilia usuários no planejamento de viagens, fornecendo informações detalhadas sobre destinos turísticos. A aplicação é projetada para fornecer insights abrangentes sobre os lugares mais visitados, as melhores opções de hospedagem e os principais pontos turísticos, incluindo o tempo médio de visita. O usuário insere o destino e a duração da estadia, e a aplicação retorna um resumo estruturado dessas informações.

2. Objetivos Principais
* Facilitar o planejamento de viagens: Fornecer aos usuários informações detalhadas e organizadas sobre destinos turísticos, ajudando-os a planejar suas viagens de forma eficiente.
* Melhorar a experiência do usuário: Oferecer uma interface simples e intuitiva para que qualquer pessoa possa obter rapidamente as informações necessárias para sua viagem.
* Integração de compartilhamento: Permitir que os usuários compartilhem facilmente o plano de viagem via e-mail ou WhatsApp.

3. Arquitetura do Aplicativo

* Streamlit
Utilizado para criar a interface web interativa do AgenTravel. Ele permite a criação rápida de aplicativos web utilizando Python, oferecendo uma experiência de usuário responsiva e interativa.

* LangChain
LangChain foi Utilizado o PromptTemplate da para criar templates de prompts que são personalizados com base na entrada do usuário e LLMChain para gerenciar a execução do modelo de linguagem onde ele recebe o prompt e enviar para modelo da OpenAI.

4. Essa arquitetura permite a criação de uma aplicação interativa e eficiente que auxilia no planejamento de viagens, utilizando as capacidades avançadas de linguagem natural da OpenAI e a interface amigável do Streamlit.

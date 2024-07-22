# Projeto INFNET

1. Descrição da Aplicação e Objetivos Principais do Projeto
Aplicação: AgenTravel - Seu Agente de Viagem Virtual

Descrição:
AgenTravel é uma aplicação web interativa que auxilia usuários no planejamento de viagens, fornecendo informações detalhadas sobre destinos turísticos. A aplicação é projetada para fornecer insights abrangentes sobre os lugares mais visitados, as melhores opções de hospedagem, e os principais pontos turísticos, incluindo o tempo médio de visita. O usuário insere o destino e a duração da estadia, e a aplicação retorna um resumo estruturado dessas informações.

Objetivos Principais:

Facilitar o planejamento de viagens: Fornecer aos usuários informações detalhadas e organizadas sobre destinos turísticos, ajudando-os a planejar suas viagens de forma eficiente.
Melhorar a experiência do usuário: Oferecer uma interface simples e intuitiva para que qualquer pessoa possa obter rapidamente as informações necessárias para sua viagem.
Integração de compartilhamento: Permitir que os usuários compartilhem facilmente o plano de viagem via e-mail ou WhatsApp.
2. Arquitetura do Aplicativo
Arquitetura do Aplicativo:

Frontend: Streamlit

Streamlit é utilizado para criar a interface web interativa do AgenTravel. Ele permite a criação rápida de aplicativos web utilizando Python, oferecendo uma experiência de usuário responsiva e interativa.
Componentes de entrada:
Text Input para o destino da viagem.
Number Input para a quantidade de dias da viagem.
Text Input opcional para solicitações específicas sobre o itinerário.
Button para enviar o pedido de itinerário.
Componentes de saída:
Spinner para indicar processamento enquanto a resposta é gerada.
Markdown para exibir a resposta detalhada.
Links para compartilhar a resposta por e-mail ou WhatsApp.
Backend: LangChain e OpenAI

LangChain é utilizado para gerenciar e estruturar as chamadas ao modelo de linguagem da OpenAI (GPT-3.5/GPT-4). Ele facilita a integração do LLM e a criação de fluxos de trabalho baseados em linguagem natural.
PromptTemplate: Define o template do prompt que será enviado ao modelo de linguagem, incluindo variáveis como destino e dias de viagem.
LLMChain: Utiliza o PromptTemplate e o modelo de linguagem da OpenAI para gerar respostas baseadas nos prompts fornecidos pelos usuários.
OpenAI: O modelo de linguagem da OpenAI é responsável por processar os prompts e retornar respostas detalhadas. A API da OpenAI é configurada utilizando a chave de API carregada de um arquivo .env para segurança.
Fluxo de Trabalho:

Entrada do Usuário: O usuário insere o destino da viagem, a quantidade de dias e, opcionalmente, solicita informações específicas sobre o itinerário.
Geração de Prompt: Com base nas entradas do usuário, um prompt detalhado é gerado utilizando o PromptTemplate.
Processamento pelo Modelo de Linguagem: O LLMChain envia o prompt ao modelo de linguagem da OpenAI, que processa a solicitação e gera uma resposta estruturada.
Exibição da Resposta: A resposta gerada é exibida na interface do Streamlit, e links para compartilhar a resposta por e-mail ou WhatsApp são fornecidos.
Compartilhamento: O usuário pode optar por compartilhar a resposta gerada utilizando os links mailto: e WhatsApp API.
Essa arquitetura permite a criação de uma aplicação interativa e eficiente que auxilia no planejamento de viagens, utilizando as capacidades avançadas de linguagem natural da OpenAI e a interface amigável do Streamlit.

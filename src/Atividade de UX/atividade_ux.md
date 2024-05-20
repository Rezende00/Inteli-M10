# Atividade sobre tópicos de UX do módulo 10

### Aluno 🧑‍🎓
- Pedro de Carvalho Rezende

### Professores 👨‍🏫👩‍🏫
- Bruna Mayer
- Sergio Venâncio

## Objetivo 🎯

O objetivo desta atividade é medir seu conhecimento sobre os tópicos de UX do módulo 10, a saber: User Research, Métodos Mistos, Framework HEART, Arquitetura de Informação, Design de Interfaces e UX Writing.

## Instruções 🕹️

- Crie um documento de texto no editor e formato de sua preferência e identifique-se.
- Você deve escolher uma interface de algum produto ou serviço digital de sua preferência (ex. aplicativo do Uber) - indique o link do produto/serviço logo no início
- Você deve escrever um breve texto justificando sua escolha, que deverá se pautar em observação de algum problema de experiência do usuário nesse produto/serviço. 
    - O propósito deste trabalho é transformarmos observações de problemas em hipóteses, e então testá-las.
- Prepare-se para tirar prints do uso deste produto/serviço, para ilustrar seu trabalho.

<br>

# Parte 1: Análise HEART e GSM + proposta de coleta de dados

## Barema 📃
- Você deve produzir uma análise HEART + GSM do produto/serviço escolhido, 
    - com base no problema de experiência do usuário observado, 
    - identificando o máximo possível de elementos do framework HEART, 
    - listando objetivos, sinais e métricas de cada elemento mapeado;

- A partir da sua análise, você deve fazer uma proposta de coleta de dados quantitativa em ferramenta de sua escolha (ex. Google Analytics, Hotjar, Forms etc.), que vise compreender melhor o problema observado. 
    - Sua proposta deve indicar hipóteses, 
    - quais dados devem ser coletados para testar tais hipóteses, e 
    - as justificativas/motivações dessa hipótese/coleta (com base na análise HEART + GSM);

- **A avaliação será envolta da**:
    - completude da análise (se você deixar de identificar algum elemento HEART que poderia ser mapeado, haverá demérito);
    - coerência da análise e da proposta (se você justificar algum elemento, seu objetivo, sinal ou métrica de forma equivocada ou ilógica, haverá demérito; 
    - se você listar hipóteses/propostas de coleta de dados que não são devidamente justificadas conforme análise HEART, haverá demérito); 
- **Dica**: estabeleça uma Persona e crie um mapa de Jornada do Usuário (ou mesmo um Blueprint de Serviço) para facilitar o apontamento de sinais e métricas da sua análise.

## Entrega

### Interface do serviço digital escolhido: 
- App e Web serviço do Zé Delivery 
- Link do serviço, para web (o app é baixar na store do IoS ou Android): [Zé Delivery](https://www.ze.delivery/)

### Justificativa da escolha do serviço digital:

O Zé Delivery é um serviço de entrega de bebidas alcoólicas que se tornou muito popular no Brasil, principalmente durante a pandemia. Decidi escolher esse serviço para a atividade por causa de um problema que enfrentei ao usar o aplicativo. Identifiquei três problemas principais:

1. **Lentidão no carregamento**: O primeiro problema foi a grande lentidão no carregamento de qualquer tipo de processo dentro do aplicativo, algo que não acontece na versão web. Ganhei um cupom de 30 reais em um evento do Inteli e, ao tentar usá-lo, fiquei tão estressado que quase desisti.

2. **Recarregamento da tela**: O segundo problema foi o recarregamento da tela do aplicativo. Quando eu entrava no app, ele às vezes reiniciava, saindo da tela onde eu estava e voltando ao início.

3. **Questões de UX/UI**: O terceiro problema foi uma questão de UX/UI. Tanto no serviço web quanto no aplicativo, há uma apresentação de tipos de produtos e uma área de destaque com promoções. Minha compra, com o cupom de desconto, foi justamente de um produto em promoção nessa área, um produto que eu gosto muito. A questão é a forma como apresentaram essa área de destaque, que não é a primeira coisa que o usuário vê ao entrar no app.

Com base nesses pontos, minha experiência com o Zé Delivery no aplicativo foi bastante frustrante, destacando a necessidade de melhorias na performance e na usabilidade do app.

- Aqui pela imagem, vemos que a área de destaque está no final da visualização inicial, tanto para Web quanto para o App, fazendo com que não seja o real "destaque" que deveria ser para o usuário.
![alt text](image.png)
![alt text](<Imagem do WhatsApp de 2024-05-19 à(s) 13.15.03_2a46dd4c.jpg>)

### Análise HEART e GSM + proposta de coleta de dados

#### HEART + GSM

| HEART         | Goals                             | Signals                                                                                       | Metrics                                                               |
|---------------|-----------------------------------|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| **Happiness**     | Melhorar a satisfação do usuário com a interface e facilidade de uso	  | Feedback direto sobre a interface do usuário, taxa de satisfação em pesquisas de usuário, taxa de recomendação	                                   | Porcentagem de feedbacks positivos, Net Promoter Score (NPS) |
| **Engagement**    | Aumentar o engajamento na plataforma	 | Tempo de permanência no app/site, número de páginas visitadas, frequência de uso	                                   | Tempo médio de permanência, páginas visitadas por sessão           |
| **Adoption**      | Aumentar o número de novos usuários e pedidos	   | Cadastros novos, número de primeiros pedidos, crescimento do usuário ativo	    | Novos cadastros por mês, número de primeiros pedidos|
| **Retention**     | Manter usuários retornando à plataforma	   | Número de usuários que fazem pedidos recorrentes, frequência de pedidos	 | Taxa de retenção de clientes, frequência média de pedidos por usuário |
| **Task Success**  | Melhorar a conclusão bem-sucedida de pedidos	     | Número de pedidos completados sem problemas, erros reportados na finalização de pedidos	         | Taxa de sucesso de pedidos, número de problemas por pedido |

**Detalhamento das sugestões**:
-Happiness: Focar no feedback direto e no Net Promoter Score para medir a satisfação geral com a interface e usabilidade. Isso me ajudará a entender se os usuários gostam do serviço e estão dispostos a recomendá-lo.
- **Engagement**: Observar o tempo gasto e o número de páginas visitadas por sessão me indicará quão envolvente é o conteúdo e a interface para os usuários.
- **Adoption**: Acompanhar o crescimento de novos usuários e o número de primeiros pedidos são indicadores importantes para entender como novos usuários estão adotando o serviço.
- **Retention**: É crucial medir quantos usuários retornam e fazem pedidos repetidos, pois isso reflete o sucesso em manter os usuários engajados com o serviço a longo prazo.
Task Success: Monitorar a taxa de sucesso na finalização de pedidos e o número de problemas reportados me ajudará a avaliar a eficiência operacional e a satisfação do cliente no uso da plataforma

--- 
Para aprimorar a coleta de dados quantitativos e alinhar com a minha preferência em usar o DataDog, revisei a estratégia de coleta de dados para incluir métricas detalhadas que podem ser capturadas em tempo real. Este ajuste não só melhora a precisão da análise, mas também otimiza a resposta a problemas identificados, maximizando a eficácia do aplicativo. Aqui está a minha proposta revisada usando o DataDog:

### Proposta de coleta de dados quantitativa com DataDog

#### Hipóteses

1. **Hipótese 1**: A lentidão no carregamento do aplicativo está afetando a satisfação do usuário
    - **Justificativa**: A lentidão pode causar frustração e levar os usuários a abandonar o uso do aplicativo, afetando diretamente a satisfação do usuário.

2. **Hipótese 2**: O recarregamento da tela está afetando o engajamento do usuário
    - **Justificativa**: Interrupções no uso, como reinicializações de tela, podem diminuir o engajamento e confundir os usuários, levando a uma experiência de uso negativa.

3. **Hipótese 3**: A apresentação da área de destaque não está sendo eficaz
    - **Justificativa**: Se as promoções e descontos em destaque não são imediatamente visíveis ou atraentes, isso pode resultar em uma menor conversão de vendas e impactar a percepção de valor do aplicativo.

#### Coleta de dados com DataDog

1. **Tempo médio de carregamento do aplicativo**:
    - **Métrica**: Monitorar o tempo de carregamento por sessão.
    - **Ferramenta**: DataDog
    - **Objetivo**: Identificar e minimizar picos de lentidão para melhorar a experiência do usuário.

2. **Taxa de abandono da aplicação**:
    - **Métrica**: Percentual de sessões abandonadas antes da conclusão de um pedido.
    - **Ferramenta**: DataDog
    - **Objetivo**: Determinar o impacto da performance na decisão de continuar ou abandonar o aplicativo.

3. **Engajamento do usuário (sessões interrompidas)**:
    - **Métrica**: Número de reinicializações de tela por sessão.
    - **Ferramenta**: DataDog
    - **Objetivo**: Quantificar e reduzir as interrupções no engajamento para proporcionar uma experiência mais fluída.

4. **Visualizações da área de destaque**:
    - **Métrica**: Cliques em itens destacados versus visualizações totais da página.
    - **Ferramenta**: DataDog
    - **Objetivo**: Avaliar a eficácia visual e de interação das áreas de destaque, ajustando-as conforme necessário para maximizar a atração do usuário.

5. **Conversão de vendas nas áreas de destaque**:
    - **Métrica**: Número de compras realizadas através das promoções destacadas.
    - **Ferramenta**: DataDog
    - **Objetivo**: Medir a eficácia das campanhas promocionais em destaque e otimizar a apresentação para aumentar as vendas.

Utilizando o DataDog, posso monitorar esses aspectos em tempo real e integrar diferentes fontes de dados para uma análise mais robusta, proporcionando insights mais profundos e permitindo uma resposta ágil às necessidades dos usuários.

### Conclusão

Através da análise HEART e GSM, identifiquei os principais desafios na experiência do usuário no aplicativo do Zé Delivery. Para endereçar esses problemas, propus um plano detalhado de coleta de dados quantitativos que visa testar hipóteses específicas relacionadas à performance e usabilidade do aplicativo. Acredito que a implementação deste plano não só proporcionará insights valiosos sobre as áreas críticas de melhoria, mas também permitirá uma abordagem iterativa na implementação de mudanças. Essa estratégia está projetada para aumentar a satisfação e o engajamento dos usuários de forma contínua e sustentada. Além disso, enfatizo a importância de utilizar o feedback dos dados para realizar ajustes e melhorias, garantindo que o aplicativo evolua de acordo com as necessidades e expectativas dos usuários. Com estas medidas, espero não apenas resolver os problemas identificados, mas também melhorar a retenção de usuários e aumentar a conversão de visitantes em clientes regulares.
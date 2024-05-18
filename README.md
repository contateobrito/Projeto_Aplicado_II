# Análise Exploratória de Dados do Airbnb na Cidade de Nova York

## Apresentação dos Dados  
O conjunto de dados utilizado nesta análise foi obtido do Kaggle e contém informações detalhadas sobre as listagens do Airbnb na cidade de Nova York. Os dados incluem variáveis como preço, localização, tipo de propriedade, avaliações, disponibilidade e muito mais. Este conjunto de dados nos proporciona uma visão abrangente do mercado de aluguel de curto prazo na cidade de Nova York.

## Fonte do dataset
- [Base Kaggle](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data?resource=download)

## Video da Apresentação
- [Link youtube](https://youtu.be/IIlg6cYizDc)

## Introdução  
O Airbnb se tornou uma plataforma popular para viajantes em todo o mundo que buscam acomodações únicas e autênticas. Com milhares de listagens em cidades cosmopolitas como Nova York, analisar os dados do Airbnb pode fornecer insights valiosos para viajantes, proprietários de imóveis e pesquisadores. Neste projeto, conduziremos uma análise exploratória de dados para entender melhor o mercado de aluguel de curto prazo na cidade de Nova York e identificar padrões e tendências relevantes.

## Objetivos  
O objetivo deste projeto é realizar uma análise exploratória de dados sobre as listagens do Airbnb na cidade de Nova York. Por meio dessa análise, pretendemos extrair insights significativos sobre os padrões de preços, distribuição geográfica, tipos de propriedades e outras tendências relevantes.

## Cronograma  
![image](https://github.com/contateobrito/Airbnb/assets/79146445/f42a1671-1d5b-4d4b-943a-09d97cf5784d)

### Questionamentos que podem ser respondido atráves de uma analise descritiva

- **Distribuição espacial das listagens**: Como as listagens de Airbnb estão distribuídas geograficamente pela cidade de Nova York? Existem áreas com maior concentração de listagens do que outras?
- **Preços médios por bairro**: Qual é o preço médio de aluguel por noite em diferentes bairros de Nova York? Existem discrepâncias significativas nos preços entre os bairros?
- **Tipos de propriedades mais comuns**: Quais são os tipos de propriedades mais comuns listados no Airbnb em Nova York (apartamentos, casas, quartos compartilhados, etc.)? Qual é a distribuição percentual desses tipos?
- **Duração típica das estadias**: Qual é a duração média das estadias dos hóspedes em listagens de Airbnb? Há uma preferência por estadias curtas ou longas?
- **Correlação entre características e preços**: Existe alguma correlação entre características das propriedades (como número de quartos, comodidades oferecidas, localização) e os preços de aluguel por noite?
- **Distribuição de avaliações**: Como estão distribuídas as avaliações dos hóspedes para as propriedades do Airbnb em Nova York? Qual é a média e a distribuição das avaliações?
- **Comodidades mais populares**: Quais são as comodidades mais comuns oferecidas nas listagens de Airbnb em Nova York? Qual é a frequência de cada uma delas?
- **Distribuição de preços por tipo de propriedade**: Como os preços variam entre diferentes tipos de propriedades (apartamentos, casas, quartos compartilhados, etc.)? Existe uma diferença significativa nos preços entre eles?

### Questionamentos que podem ser respondido atráves de uma analise preditiva 
- **Previsão de Preços:** Como podemos prever os preços de novas listagens com base em características como localização, tipo de propriedade, comodidades oferecidas, etc.?  
- **Segmentação de Mercado:** Podemos identificar segmentos de mercado com base em padrões de reserva e preferências dos hóspedes, e prever quais tipos de propriedades serão mais procurados em diferentes momentos ou por diferentes grupos de hóspedes?  
- **Recomendação de Preços para Anfitriões:** Podemos desenvolver um modelo que recomende preços otimizados para os anfitriões com base em características da listagem e dados de mercado?  
- **Previsão de Popularidade de Novas Listagens:** É possível prever a popularidade de novas listagens com base em características da propriedade, localização e outros fatores?  
- **Detecção de Anomalias:** Podemos desenvolver modelos para detectar anomalias nas reservas, como preços extremamente altos ou baixos em comparação com o padrão do mercado?  
- **Previsão de Lucratividade para Anfitriões:** Podemos prever a lucratividade potencial de uma listagem com base em características da propriedade e custos associados?  
- **Modelos de Demanda de Curto Prazo:** Podemos desenvolver modelos de demanda de curto prazo para prever a demanda por listagens em datas específicas, levando em consideração eventos locais, feriados, etc.?  

## **Tecnologias Utilizadas**:  
- Python
- Pandas
- Matplotlib

🚧 **Análise Exploratória de Dados**: Principais insights e descobertas obtidos durante a análise dos dados.  

Explorando os tipos de variáveis  
![image](https://github.com/contateobrito/Airbnb/assets/79146445/72392122-41c7-44eb-848a-c20a47f1fda2)

Principais estatísticas da base  
![image](https://github.com/contateobrito/Airbnb/assets/79146445/b1a801b4-45e0-4f7f-9c51-e44f633a3d28)

Média de preços de acomodação por distrito  
![image](https://github.com/contateobrito/Airbnb/assets/79146445/fbc4573c-31ca-4e7a-85d1-3d7d055faaf8)

Distribuição por tipo de acomadação por distrito  
![image](https://github.com/contateobrito/Airbnb/assets/79146445/7554cd20-7d83-4668-853d-997bed142b46)

Quantidade de host por distrito  
![image](https://github.com/contateobrito/Airbnb/assets/79146445/07232bd9-f297-4fd4-8006-c1f415c8e83d)

Histograma da frequencia de dias disponiveis para locação  
![image](https://github.com/contateobrito/Airbnb/assets/79146445/6e9fba46-faf1-4385-9d6c-3d7c88cde549)

Tipo de acomodações em forma de dispersão  
![image](https://github.com/contateobrito/Airbnb/assets/79146445/2c8f7c0a-9cc5-47f9-83c0-ac8fab7f14e5)

Correlação entre as variaveis númericas
![image](https://github.com/contateobrito/Airbnb/assets/79146445/3dc2a55c-fb48-498f-9b4b-664f75de269c)

## **Conclusão**   
![image](https://github.com/contateobrito/Projeto_Aplicado_I/assets/79146445/b1fb8087-36d5-43c5-9aa3-c483c29e7dbf)  

A análise utilizada foi de Regressão Linear. O modelo deve inferir valores de diárias para novas empreendimento com base no bairro e tipo de alocação. No entanto, após termos separado a base, treinamento e teste, e feito todo o procedimento adequado, deparou-se com um MSE, muito alto. Tornando inviável o a utilização do modelo.
A partir disso, será avaliado o motivo, a seguir possíveis motivos listados.
•	Modelo inadequado: O modelo de regressão linear pode não ser apropriado para os dados em questão. Pode ser necessário explorar modelos mais complexos ou técnicas de modelagem diferentes.
•	Dados de entrada inadequados: Os preditores podem não estar capturando adequadamente a relação com a variável de resposta. Talvez seja necessário considerar outros preditores ou transformações nos dados.
•	Problemas de escala: Se os preditores estiverem em diferentes escalas, isso pode afetar a performance do modelo. Normalmente, é uma boa prática padronizar ou normalizar os dados antes de ajustar um modelo de regressão.
•	Presença de outliers: Outliers nos dados podem distorcer o ajuste do modelo e aumentar o MSE. É importante examinar os dados em busca de valores atípicos e considerar maneiras de lidar com eles, como remoção ou transformação.
Overfitting ou underfitting: O modelo pode estar sofrendo de overfitting (ajuste excessivo) ou underfitting (ajuste insuficiente). Overfitting ocorre quando o modelo se ajusta muito bem aos dados de treinamento, mas não generaliza bem para novos dados. Underfitting ocorre quando o modelo é muito simples para capturar a relação nos dados.
Diante dos valores apresentados não foi possível inferir e comprovar nossas hipóteses a respeitos do dataset em questão. Pois destaca-se a ausência de informações pertinentes como: histórico de alocações, avaliação dos locais e descrição dos locais.


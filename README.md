# Análise de Campeões League of Legends

Projeto de análise de dados dos campeões do League of Legends, extraindo informações da API oficial do Ddragon e realizando análises exploratórias com visualizações 2D e 3D.

## 📋 Descrição

Este projeto coleta dados estatísticos de todos os campeões do League of Legends e realiza análises dimensionais dos atributos, utilizando PCA (Principal Component Analysis) para visualização e exploração dos dados.

## 📂 Estrutura do Projeto

```
LoL/
├── get_data.py           # Script para coleta e transformação de dados
├── main.ipynb            # Notebook principal com análises e visualizações
├── champions_db.csv      # Banco de dados de campeões
└── assets/images/        # Pasta com imagens dos campeões e gráficos
```

## 🛠️ Funcionalidades

### `get_data.py`

- Coleta dados da API oficial do Ddragon
- Transforma dados JSON em DataFrame pandas
- Extrai estatísticas dos campeões (HP, Armadura, Velocidade de Ataque, etc.)
- Baixa imagens dos campeões
- Salva dados em formato CSV

### `main.ipynb`

- Carregamento e exploração dos dados
- Análises exploratórias com pandas
- Aplicação de PCA para redução dimensional
- Visualizações 2D e 3D dos dados

## 📊 Gráficos e Visualizações

### Gráficos 2D

![Gráfico 2D](assets/readme/2d.PNG)

É possível notar que já foi separado entre campeões com alto Alcance de Ataque (Direita do gráfico) e os com baixo (Esquerda do gráfico).
No lado Direito mantém-se campeões mais conhecidos como lutadores ou tanques e na Direita parte superior estão os Magos (mais mana e Poder de Habilidade) e na parte inferior da Direita estão os com maior Dano de Ataque.

### Gráficos 3D

<!-- ![Gráfico 3D](assets/readme/3d.gif) -->
![Gráfico 3D](assets/readme/3d_v2.gif)

Ao plotar uma outra dimensão, usando como exemplo a parte inferior da Direita (Atiradores) os com maior Dano de Ataque aparecem mais próximos.

📦 Dependências

- `pandas` - Manipulação e análise de dados
- `matplotlib` - Visualizações
- `pyvista` - Visualização 3D
- `scikit-learn` - Aprendizado de máquina (PCA, Escaladores)
- `requests` - Requisições HTTP

## 🚀 Como Usar

1. **Coleta de dados:**

   ```bash
   python get_data.py
   ```

   Isso irá baixar os dados dos campeões, transformá-los em um DataFrame e salvar em `champions_db.csv`, além de baixar as imagens.
2. **Análise e visualizações:**
   Abra `main.ipynb` em um Jupyter Notebook para explorar os dados e visualizar os gráficos.

## 📊 Conclusão PCA
Adicionar um novo eixo torna a análise mais detalhada, porém mais custosa em certo ponto. O 3D deixa ver com mais clareza pontos de dados escondidos que o 2D não deixaria (Profundidade, eixo Z). Mas esse detalhe torna um pouco mais complexo a análise do gráfico.

Em resumo, nesse caso, é um trade-off, ver com mais detalhes campeões que ficaram escondidos no 2D, em compensação, ter uma análise mais complexa.

## 🔗 Referências

- [API Ddragon do League of Legends](http://ddragon.leagueoflegends.com/)

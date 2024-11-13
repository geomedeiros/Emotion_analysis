
# Backend de Detecção de Emoções

Este projeto utiliza Flask e DeepFace para detectar emoções em imagens enviadas pelo frontend.

## Pré-requisitos

- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)

## Instalação

1. Clone o repositório e navegue até o diretório do projeto:

   ```bash
   git clone https://github.com/geomedeiros/Emotion_analysis
   cd Emotion_analysis/backend
   ```

2. Instale as dependências listadas em `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

## Executando o Backend

Para iniciar o servidor Flask, execute o seguinte comando:

```bash
python ia.py
```

O servidor estará rodando em `http://127.0.0.1:5000`.

## Endpoints

- **POST** `/detect_emotion`: Recebe uma imagem e retorna a emoção detectada.

## Notas

- Certifique-se de que o backend está rodando antes de acessar pelo frontend.
- Para modificar configurações, edite o arquivo `ia.py`.

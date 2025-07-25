from openai import OpenAI
from tools import *
from dotenv import load_dotenv
import os

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_caso_uso(prompt, modelo=MODELO_REFINADO):
  documento_casos = carrega("documentos\explicacao_casos.txt")

  prompt_sistema = f"""
    Você é um especialista em desenvolver casos de uso. Você deve adotar o padrão abaixo para gerar seu caso de uso:
    
    {documento_casos}

    Considere os dados de entrada sugeridos pelo usuário e gere o caso de uso no formato adequado.
  """

  #prompt_usuario = f"""
  #  Ana que deseja realizar login na plataforma AcordeLab.
  #"""

  resposta = cliente.chat.completions.create(
    model=modelo,
    messages = [
      { "role": "system", "content": prompt_sistema },
      { "role": "user", "content": prompt }
    ],
    temperature=0.5
  )

  return resposta.choices[0].message.content
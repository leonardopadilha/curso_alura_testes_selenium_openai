from gerador_casos_uso import *
from gerador_cenarios_teste import *
from gerador_script_teste import *
from tools import *

def main():
  pedido_usuario = input("Digite um caso de uso: ")

  casos_uso = gerar_caso_uso(pedido_usuario, MODELO_GPT_3_5)
  print("\n\nCaso de Uso - Não Refinado:\n", casos_uso)

  casos_uso = gerar_caso_uso(pedido_usuario, MODELO_REFINADO)
  print("\n\nCaso de Uso - Refinado:\n", casos_uso)

"""
  cenario_teste = gerar_cenario_teste(casos_uso)
  print("\n\nCenário de Teste:\n", cenario_teste)

  script_teste = gerar_script_teste(casos_uso, cenario_teste)
  print("\n\nScript de Teste:\n", script_teste)
  salva('script_temp_ia.py', script_teste)
"""

if __name__ == "__main__":
  main()
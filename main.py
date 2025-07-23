from gerador_casos_uso import *
from gerador_cenarios_teste import *
from gerador_script_teste import *

def main():
  casos_uso = gerar_caso_uso()
  print("\n\nCaso de Uso:\n", casos_uso)

  cenario_teste = gerar_cenario_teste(casos_uso)
  print("\n\nCenário de Teste:\n", cenario_teste)

  script_teste = gerar_script_teste(casos_uso, cenario_teste)
  print("\n\nScript de Teste:\n", script_teste)
  salva('script_temp_ia.py', script_teste)

if __name__ == "__main__":
  main()
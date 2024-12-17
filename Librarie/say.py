# ==================== Saudação com argumentos de Linha de Comando ==================== 
import sys
from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])

import os
import shutil

caminhoOriginal = "Y:/7. RENATO ALVES/foto/CARTEIRINHA/teste"
caminhoNovo = "Y:/7. RENATO ALVES/foto/CARTEIRINHA/teste/copia"

try: os.mkdir(caminhoNovo)
except FileExistsError as e:
    print("caminho {} já existe",format(caminhoNovo))

for root, dirs, files in os.walk(caminhoOriginal):
    for file in files:
        caminhoAntigoPath = os.path.join(root, file)
        caminhoNovoPath = os.path.join(caminhoNovo, file)
        shutil.copy(caminhoAntigoPath, caminhoNovoPath)
    
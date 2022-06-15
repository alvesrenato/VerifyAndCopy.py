from genericpath import exists
import os
import shutil

caminhoNovo = input('selecione a pasta de destino: ')
caminhoNovo += '/'


meuArquivo = open('U:/PROJETOS/Rosário/2022/CARTEIRINHA PROVISÓRIA/15-06-22-PRODUÇÃO - CARTEIRINHA ESCOLAR - FUTUROESCOLAR/matriculas.txt','r')
matriculas = meuArquivo.readlines()

# print(matriculas)

caminhoOriginal = 'Y:/7. RENATO ALVES/foto/CARTEIRINHA/'


for matricula in matriculas:
    matricula = matricula.replace('\n','')
    
    if os.path.exists(caminhoOriginal+matricula+'.jpg'):
        shutil.copy(caminhoOriginal+matricula+'.jpg', caminhoNovo+matricula+'.jpg')
    else:
        print('Não foi: '+ matricula)



# if os.path.exists(caminhoOriginal):
#     print ("o arquivo existe")
# else:
#     print("o arquivo no ecxiste")
        
    


# caminhoNovo = "Y:/7. RENATO ALVES/foto/CARTEIRINHA/teste/copia"

# try: os.mkdir(caminhoNovo)
# except FileExistsError as e:
#     print("caminho {} já existe",format(caminhoNovo))

# for root, dirs, files in os.walk(caminhoOriginal):
#     for file in files:
#         caminhoAntigoPath = os.path.join(root, file)
#         caminhoNovoPath = os.path.join(caminhoNovo, file)
#         shutil.copy(caminhoAntigoPath, caminhoNovoPath)
        
        
        
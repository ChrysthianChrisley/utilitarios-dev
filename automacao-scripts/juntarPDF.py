import os
from PyPDF2 import PdfMerger, PdfReader
from PyPDF2.errors import EmptyFileError

def executar():
    # Lista todos os arquivos PDF no diretório atual
    listaArquivosnaPata = [a for a in os.listdir() if a.endswith(".pdf")]
     
    juntarPDF = PdfMerger()
     
    for pdf in listaArquivosnaPata:
        try:
            # Verifica se o arquivo não está vazio antes de tentar mesclar
            if os.path.getsize(pdf) > 0:
                juntarPDF.append(open(pdf, 'rb'))
            else:
                print(f"Arquivo vazio ignorado: {pdf}")
        except EmptyFileError:
            print(f"Erro: O arquivo {pdf} está vazio e será ignorado.")
        except Exception as e:
            print(f"Erro ao processar o arquivo {pdf}: {e}")
     
    with open("result1.pdf", "wb") as fout:
        juntarPDF.write(fout)
        print("Concluído.")
        
if __name__ == '__main__':
    try:
        executar()
    except Exception as e:
        print(f"Erro inesperado: {e}")

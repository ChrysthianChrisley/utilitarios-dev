import glob
import os
from pypdf import PdfWriter
import sys

# --- Configurações ---
NOME_ARQUIVO_SAIDA = "documentos_mesclados.pdf"
PADRAO_BUSCA = "*.pdf"

def mesclar_pdfs():
    """
    Busca todos os arquivos PDF na pasta atual, os ordena e os mescla em um único arquivo.
    """
    print("Iniciando a busca por arquivos PDF na pasta atual...")
    
    # 1. Encontrar e ordenar os arquivos
    arquivos_pdf = sorted(glob.glob(PADRAO_BUSCA))
    
    # 2. Remover o arquivo de saída, caso ele exista e esteja na lista
    if NOME_ARQUIVO_SAIDA in arquivos_pdf:
        arquivos_pdf.remove(NOME_ARQUIVO_SAIDA)
    
    if not arquivos_pdf:
        print("\n---")
        print(f"ERRO: Nenhum arquivo que corresponda ao padrão '{PADRAO_BUSCA}' foi encontrado nesta pasta.")
        print("---")
        return
    
    print(f"Arquivos encontrados (ordem de mesclagem):")
    for i, arquivo in enumerate(arquivos_pdf):
        print(f"  {i+1}. {arquivo}")
    
    # 3. Inicializar o objeto PdfWriter
    writer = PdfWriter()
    
    try:
        # 4. Anexar cada PDF ao objeto writer
        for pdf in arquivos_pdf:
            writer.append(pdf)
        
        # 5. Escrever o resultado no arquivo de saída
        with open(NOME_ARQUIVO_SAIDA, "wb") as saida:
            writer.write(saida)
        
        print("\n------------------------------------------------------")
        print("Mesclagem concluída com sucesso!")
        print(f"Total de arquivos mesclados: {len(arquivos_pdf)}")
        print(f"O novo arquivo está salvo como: {NOME_ARQUIVO_SAIDA}")
        print("------------------------------------------------------")
        
    except Exception as e:
        print(f"\nOcorreu um erro durante a mesclagem: {e}")
    finally:
        # 6. Fechar o writer para liberar recursos
        writer.close()

if __name__ == "__main__":
    mesclar_pdfs()
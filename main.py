from PIL import Image
import io

# Crie um dicionário para armazenar os dados dos contatos
contatos = {
    '12345': {
        'nome': 'João',
        'telefone': '123-456-7890',
        'imagem': 'images/joao.jpg'
    },
    '67890': {
        'nome': 'Maria',
        'telefone': '987-654-3210',
        'imagem': 'maria.jpg'
    }
}


# Função para buscar um contato pelo número
def buscar_contato(numero):
  if numero in contatos:
    contato = contatos[numero]
    print(f"Nome: {contato['nome']}")
    print(f"Telefone: {contato['telefone']}")

    # Exiba a imagem do contato
    imagem_path = contato['imagem']
    try:
      imagem = Image.open(imagem_path)
      imagem.show()
    except Exception as e:
      print(f"Erro ao exibir a imagem: {e}")
  else:
    print("Contato inexistente, tente novamente!")


# Loop principal
while True:
  numero = input("Digite o número do contato (ou 'sair' para encerrar): ")

  if numero.lower() == 'sair':
    break

  buscar_contato(numero)

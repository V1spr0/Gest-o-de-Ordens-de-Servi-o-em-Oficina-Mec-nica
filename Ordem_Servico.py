from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class OrdemServico(Base):
    __tablename__ = "OrdemServico"

    id = Column(Integer, primary_key=True)
    nome_cliente = Column(String, nullable=False)
    placa_veiculo = Column(String, nullable=False, unique=True)
    tipo_servico = Column(String, nullable=False)


def criar_ordem_servico(session):
    nome_cliente = input("Digite seu nome: ").strip()
    placa_veiculo = input("Digite a placa do veículo: ").strip()
    tipo_servico = input("Digite o tipo de serviço solicitado: ").strip()

    nova_ordem = OrdemServico(
        nome_cliente=nome_cliente,
        placa_veiculo=placa_veiculo,
        tipo_servico=tipo_servico
    )

    session.add(nova_ordem)
    session.commit()
    print("\nOrdem de serviço inserida com sucesso!\n")


def lisar_ordem_servico(session):
    OrdemServico = session.query(OrdemServico).all()
    print("\n--- Lista de Ordens de Serviço ---")
    for u in OrdemServico:
        print(f"ID: {u.id} | Nome: {u.nome_cliente} | Placa: {u.placa_veiculo} | Tipo de serviço: {u.tipo_servico}")
    print("-------------------------\n")



def menu():
    while True:
        print("\n=== MENU ===")
        print("1 - Criar")
        print("2 - Listar ")
        print("3 - Atualizar")
        print("4 - Excluir")

        op = input("Escolha: ")

        if op == "1":
            criar_ordem_servico()

        elif op == "2":
            lisar_ordem_servico()
                 
                
            break

        else:
            print("Opção inválida!")

menu()
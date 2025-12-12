#=======IMPORTAÇÃO======#

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, ForeignKey, DECIMAL, Float
from datetime import datetime
import enum

#=======CONEXÃO======#

engine = create_engine("mysql+pymysql://root:@127.0.0.1:6363/pagamentos", echo=False)
Base = declarative_base()
conn = engine.connect()

print("Conectou!")
SessionLocal = sessionmaker(bind=engine)

#=======ENUM======#

class StatusPagamento(enum.Enum):
     PENDENTE = 'PENDENTE'
     ATRASADO = 'ATRASADO'
     PAGO = 'PAGO'
     CANCELADO = 'CANCELADO'

#=======CLASSES======#

class Pagamento(Base):
    __tablename__ = "pagamentos"

    id_pagamento = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Float, nullable=False)
    data_pagamento = Column(DateTime, default=datetime.now)
    status = Column(Enum(StatusPagamento),default=StatusPagamento.PENDENTE)   

    cliente = relationship("", back_populates="pagamentos")

#=======FUNÇÕES======#
#=======INSERIR======#

def inserir_pagamento():
    session = SessionLocal()
    
    try:
        id_cliente = int(input("ID do cliente: "))
        valor = Float(input("Valor: "))   # corrigido
        
        novo = Pagamento(
            id_cliente=id_cliente,
            valor=valor,
            status=StatusPagamento.PENDENTE
        )
        
        session.add(novo)
        session.commit()
        print("Pagamento Registrado!")
        return True  

    except Exception as e:
        session.rollback()
        print("Pagamento não foi registrado.")
        return False  

    finally:
        session.close()

#=======ATUALIZAR======#

def atualizar_pagamento():
    session = SessionLocal()
    
    id_pag = int(input("ID do pagamento: "))
    novo_status = input("Novo status(PENDETE,PAGO,ATRASADO,CANCELADO): ")
    
    pag = session.query(Pagamento).filter_by(id_pag=id_pag).first()
    
    if pag:
        pag.status = StatusPagamento[novo_status]
        session.commit()
        print("Status atualizado!!")
    else:
        print("Pagamento não encontrado.")
    session.close()

#=======LISTAR======#
    
def listar_pagamentos():
    session = SessionLocal()
    pagamentos = session.query(Pagamento).all()

    for p in pagamentos:
        print(p.id, p.valor, p.status)

    session.close()    
 
#=======MENU======# 
    
def menu():
    while True:
        print("\n===MENU PAGAMENTO===")
        print("1 - Inserir pagamento")
        print("2 - Atualizar pagamento")
        print("3 - Listar pagamentos")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            inserir_pagamento()
        
        elif op == "2":
            atualizar_pagamento()

        elif op == "3":
            listar_pagamentos()
                 
        elif op == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

menu()

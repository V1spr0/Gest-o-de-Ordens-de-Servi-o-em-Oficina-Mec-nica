
class Oficina(Base):
    __tablename__ = 'oficina'

    CNPJ: Mapped[str] = mapped_column(String(14), primary_key=True, nullable=False)
    id_mecanico: Mapped[int] = mapped_column(ForeignKey('mecanico.id'), primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    endereco: Mapped[str] = mapped_column(String(100), nullable=False)

    id_mecanico: Mapped["Mecanico"] = relationship(back_populates="oficinas")

    def adicionar_oficina(self, session, cnpj, nome, endereco):
        nova_oficina = Oficina(CNPJ=cnpj, id_mecanico=self.id, nome=nome, endereco=endereco)
        session.add(nova_oficina)
        session.commit()
        return nova_oficina

    def listar_oficinas(self, session):
        return session.query(Oficina).all()

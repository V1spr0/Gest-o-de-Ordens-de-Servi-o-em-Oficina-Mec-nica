CREATE DATABASE sistema_mecanica
    CHARSET utf8mb4
    COLLATE utf8mb4_unicode_ci;
    USE sistema_mecanica;
    
CREATE TABLE OrdemServico(
id INT AUTO_INCREMENT PRIMARY KEY,
nome_cliente VARCHAR(100) NOT NULL,
placa_veiculo VARCHAR(100) NOT NULL UNIQUE,
tipo_servico VARCHAR(100) NOT NULL,
data_abertura DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
status ENUM('PENDENTE', 'EM_ANDAMENTO', 'CONCLUIDA', 'CANCELADA') NOT NULL DEFAULT 'PENDENTE',
FOREIGN KEY(mecânico_id) REFERENCES Mecanico(mecânico_id)
)

ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci;



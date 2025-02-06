# Dicionário que mapeia números de portas aos serviços correspondentes
port_services = {
    21: "FTP",      # Serviço de transferência de arquivos
    22: "SSH",      # Secure Shell (acesso remoto seguro)
    23: "Telnet",   # Protocolo de acesso remoto inseguro
    25: "SMTP",     # Serviço de envio de emails
    53: "DNS",      # Serviço de tradução de nomes de domínio
    80: "HTTP",     # Protocolo de transferência de hipertexto (web)
    110: "POP3",    # Serviço de recebimento de emails
    143: "IMAP",    # Serviço de recebimento de emails com suporte a pastas
    443: "HTTPS",   # Protocolo seguro de transferência de hipertexto
    3306: "MySQL",  # Banco de dados MySQL
    3389: "RDP",    # Remote Desktop Protocol (Acesso remoto ao Windows)
    5432: "PostgreSQL", # Banco de dados PostgreSQL
    6379: "Redis"   # Banco de dados Redis
}

# Função que realiza a enumeração de serviços
def enumerate_services(ports):

    services = [] 

    for list_ports in ports:
            
            if list_ports in port_services:
                services.append(port_services[list_ports])
            else:
                services.append("Desconhecido")

    return services

# Função principal que lida com a entrada do usuário e exibe o resultado:
def main():
    ports_input = input()  
    
    valores = [int(val.strip()) for val in ports_input.split(",")]

    servicos = enumerate_services(valores)

    print(servicos)


if __name__ == "__main__":
    main()
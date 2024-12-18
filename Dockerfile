# Usa a imagem oficial do PostgreSQL na versão mais recente
FROM postgres:latest

# Define as variáveis de ambiente para configurar o banco de dados
ARG POSTGRES_PASSWORD
ARG POSTGRES_USER
ARG POSTGRES_DB

ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_DB=${POSTGRES_DB}


# Expõe a porta padrão do PostgreSQL
EXPOSE 5432

# Comando padrão para rodar o PostgreSQL
CMD ["postgres"]

# Integrantes
| Nome                       | RM     |
|----------------------------|--------|
| Felipe Souza Carvalho      | 564779 |
| Gustavo Hackime Costa      | 563751 |
| Luiz Henrique Macedo Graça | 564704 |
| Riquelme Santos da Mata    | 565053 |

# Como executar

Clone o repositório:
```bash
git clone https://github.com/IAmIndex/cp2-edge-computing/
cd cp2-edge-computing
```

Crie o arquivo de variáveis de ambiente:
```bash
cp .env.example .env
```
> É necessário configurar manualmente as variáveis de ambiente

Crie o container do Docker:
```bash
docker built -t cp .
```

Rode o container:
```bash
docker run --env-file .env cp
```

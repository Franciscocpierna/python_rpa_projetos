# Definição de um dicionário representando uma estrutura empresarial
empresa = {
    "TI": {
        "Desenvolvimento": {
            "Maria": {"cargo": "Sénior", "salario": 8000},
            "João": {"cargo": "Júnior", "salario": 3500}
        },
        "Infraestrutura": {
            "Carlos": {"cargo": "Analista", "salario": 5000}
        }
    },
    "RH": {
        "Recrutamento": {
            "Ana": {"cargo": "Coordenadora", "salario": 6000}
        }
    }
}

cargo_maria = empresa.get("TI", {}).get("Desenvolvimento", {}).get("Maria", {}).get("cargo", "Não encontrado")
print(cargo_maria)

try:
    cargo_maria = empresa["TI"]["Desenvolvimento"]["Maria"]["cargo"]
    #cargo_maria = empresa["TI"]["Desenvolvimento"]["Joao"]["cargo"]
except KeyError as e:
    print(f"Erro capturado! A chave {e} não foi encontrada.")


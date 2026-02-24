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
    
    # lista

nome = 'Mariosvaldo'

# Método 1: Usando o construtor list() (O mais direto)
lista_caracteres = list(nome)

print("Método 1:", lista_caracteres)
# Saída: ['M', 'a', 'r', 'i', 'o', 's', 'v', 'a', 'l', 'd', 'o']
print()

# Método 2: List Comprehension (Útil se quiser aplicar alguma lógica)
lista_com_loop = [char for char in nome]
print('metodo 2',lista_com_loop)
print()
# Exemplo Extra: Se quiser apenas os caracteres únicos (sem repetição)
lista_unica = list(set(nome))
print(" Metodo 3 Caracteres únicos:", lista_unica)


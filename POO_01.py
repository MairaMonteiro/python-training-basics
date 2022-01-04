class Veiculo():
    def __init__(self, tipo, chassi, marca, modelo, ano):
        self.tipo = tipo
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

#self = parâmetro que se refere a ele mesmo
#init = método referente ao construtor -deve ser excplícito. Para ser criado o objeto é necessário respeitar o que está sendo passado em sua estrutura

class Aviao():
    def __init__(self, tipo, motor, linha_aerea, modelo, ano):
        self.tipo = tipo
        self.motor = motor
        self.linha_aerea = linha_aerea
        self.modelo = modelo
        self.ano = ano


carro = Veiculo('carro', '7546485121', 'MarcaX', 'z001', '2021')
feiji = Aviao('Carga', 'motoreta', 'VoePassarinho', 'MilCavalosAlados', '2020')

print(vars(carro))
print(vars(feiji))


class Funcionario():
    def __init__(self, nome, cpf, salario, valor_hora, cargo):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.valor_hora = valor_hora
        self.cargo = cargo
        self.__sal = 0 #atributo privado
        self.__hora_trabalhadas = 0 #atributo privado

    def get_salario(self):
        print("Meu salário é: ", self.salario)

    def get_bonificacao(self):
        return self.salario * 0.15

jose = Funcionario("José", "123456789-99", 5000)
jose.get_salario()
print(jose.get_bonificacao())

@property
def sal(self):
    return self.__sal

@sal.setter
def sal(self, novo_sal):
    self.novo_sal
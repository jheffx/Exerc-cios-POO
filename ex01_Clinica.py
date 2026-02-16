#Classe do Paciente 
class Paciente:
    def __init__(self, nome, idade:int ):
        self.nome = nome
        self.idade = idade
        self.atendimento = False
		
   
#Classe da Clínica 
class Clinica:
    def __init__(self):
        self.pacientes = []

	
    def verPacientes(self):
        if not self.pacientes:
           return "» Nenhum paciente na lista"
			
        status = {}
        for paciente in self.pacientes: 
             status[self.pacientes.index(paciente)] = {
                 paciente.nome: self.status(paciente)
             }

        listaSit = []
        for chave, valor in status.items():
            nomes = ''.join(list(valor.keys()))
            situacao = ''.join(list(valor.values()))
            texto = f"""
{nomes:<15}{situacao:>20}
            """
            listaSit.append(texto)
            
        pacientes = ''.join(listaSit)
        listaPacientes = f"""
======= Lista de Pacientes =========
NOMES                         STATUS
====================================
{pacientes}
...................................
        """
		return listaPacientes
          
    def status(self, paciente):
        if paciente.atendimento is True:
            status = "Em Atendimento"
            return status
        else:
            status = "Na espera"
            return status
            
    def addPaciente(self, paciente):
        if paciente not in self.pacientes:
            self.pacientes.append(paciente)
            return "» Paciente adicionado na lista de espera."
        else:
            return "» O paciente já está na lista de espera."
       
    def iniciarAtendimento(self, paciente):
        if paciente not in self.pacientes:
            return "» O paciente não está na lista."
        
        if not paciente.atendimento:
            paciente.atendimento = True
            return "» O paciente pode ser atendido"
        else:
            return "» O paciente já está em atendimento. "
            
        
             
    def finalizarAtendimento(self, paciente):
        if paciente not in self.pacientes:
            return "» O paciente não está na lista."
        if not paciente.atendimento:
            return "» O paciente não está em atendimento."
        else:
            paciente.atendimento = False
            return """
» Atendimento encerrado. 

Agradecemos a preferência. Volte Quando precisar!

Abraços!
"""
 
p1 = Paciente("Jheff", 28)
p2 = Paciente("Yanne", 6)
p3 = Paciente("Maria", 23)

c = Clinica()
c.addPaciente(p1)
c.addPaciente(p2)
c.addPaciente(p3)
print(c.verPacientes())


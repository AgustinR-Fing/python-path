class Category:

    def __init__(self,nombre):
        self.nombre = nombre
        self.ledger = []
        self.balance = 0;

    
    def deposit (self,amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})
        self.balance+= amount
        return
    
    def withdraw(self,amount,description = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            self.balance -= amount
            return True
        else: 
            return False
    
    def get_balance(self):
        return self.balance

    def transfer(self,amount,other): 
        if self.withdraw(amount, f'Transfer to {other.nombre}'):
            other.deposit(amount, f'Transfer from {self.nombre}')
            return True
        return False
        
    def check_funds(self,amount):
        if self.balance < amount: # Si no tengo el dinero suficiente
            return False 
        else:
            return True

    def __str__ (self): 
        lista = [] # Junto todas las lineas

        # Resuelvo el titulo
        resto = 30 - len(self.nombre)
        parte1 = resto // 2
        parte2 = resto - parte1

        titulo = ''
        for i in range(parte1):
            titulo += '*'
        titulo+= self.nombre
        for i in range(parte2):
            titulo += '*'
        
        lista.append(titulo)

        total = 0
        # Resuelvo entradas ledger
        
        for i in self.ledger:
            linea_nueva = ''
            linea_nueva += i["description"][:23].ljust(23) # alineado a la izq
            linea_nueva += f'{i["amount"]:.2f}'.rjust(7) # alineado a la der
            lista.append(linea_nueva)
        
        lista.append(f'Total: {self.balance:.2f}')

        resultado = "\n".join(lista)

        return resultado
    

def create_spend_chart(categories):
    title = 'Percentage spent by category\n'

    # 1) cuanto gasto cada categoría, y el total entre todas:
    gastos = []          
    total_gastado = 0
    maximo = 0

    for c in categories:
        if len(c.nombre) > maximo:
            maximo = len(c.nombre)

        gastado = 0
        for movimiento in c.ledger:
            if movimiento['amount'] < 0:
                gastado += -movimiento['amount']

        gastos.append(gastado)
        total_gastado += gastado

    # 2) calculo el porcentaje
    porcentaje = []
    for gastado in gastos:
        numero = (gastado / total_gastado) * 100
        porcentaje.append((numero // 10) * 10)
    
    # Parte de los nombres vertical
    nombres_lineas = ''
    for i in range(maximo):
        nombres_lineas += '     ' 
        for c in categories:
            try:
                nombres_lineas += f'{c.nombre[i]}  '
            except IndexError: 
                nombres_lineas += '   '
        if (i != maximo - 1):
            nombres_lineas += "\n"


    # Parte de la barra horizontal
    barra = '    -'
    for i in range(len(categories)): 
        barra += '---'
    barra += "\n"

    # Parte de los porcentajes y barras
    new_line = ''
    i = 10
    while (i>= 0):
        new_line+=f'{i * 10}| '.rjust(5)
        for j in porcentaje: 
            if j >= i*10 : 
                new_line+='o  '
            else:
                new_line += '   '
        new_line+='\n'
        i-=1
    
    resultado = title + new_line + barra + nombres_lineas
    return resultado


food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(300, 'nuevo')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
#print(food)


cama = Category('Camas')
cama.deposit(1000, 'initial deposit')
cama.withdraw(10.15, 'groceries')
cama.withdraw(15.89, 'restaurant and more food for dessert')
cama.transfer(50, clothing)
cama.withdraw(600, 'xd')


print('\n')

print(create_spend_chart([food,cama]))
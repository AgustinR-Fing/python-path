class HashTable:
    def __init__(self):
        self.collection = {}
    
    def hash(self, cadena):
        resultado = 0
        for x in cadena: 
            resultado += ord(x)
        return resultado
    
    def add(self, clave, valor):
        res = self.hash(clave)
        if res in self.collection:
            self.collection[res][clave] = valor
        else:
            self.collection[res] = {clave : valor}
        
        print (f"Se aniadio el elemento {self.collection}")
        print (f"------------")
    
    def remove(self, clave):
        res = self.hash(clave)
        if res in self.collection:
            self.collection[res].pop(clave, None)
        
        print(f"Se removio el elemento {self.collection}")
        print (f"------------")
        

    def lookup(self, clave):
        res = self.hash(clave)
        if (self.collection.get(res) is None) or (self.collection[res].get(clave) is None):
            return None
        else:
            return self.collection[res][clave]

'''
h1 = HashTable()

h1.add('ab', 23)
h1.add('ba',42)

print(h1.lookup('ab'))
'''
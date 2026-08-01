def hanoi_solver(cant_discos: int):
    varilla = [[x for x in range(cant_discos, 0, -1)],[],[]]
    lista = []
    
    def actualizar_estado(v): 
        lista.append(f'{v[0]} {v[1]} {v[2]}')
        

    def recursion(origen, auxiliar, destino, n):
        if n != 0:
            recursion(origen, destino, auxiliar, n - 1)

            varilla[destino].append(varilla[origen][-1])
            del varilla[origen][-1]
            actualizar_estado(varilla)

            recursion(auxiliar, origen, destino, n - 1)
    
    actualizar_estado(varilla)
    recursion(0,1,2,cant_discos)
   
    res = "\n".join(lista)
    return res


print(hanoi_solver(2))

def add_setting(configuracion: dict, clave_valor: tuple):
    # no pide programacion defensiva respecto al parametro clave_valor
    key, value = clave_valor
    key = key.lower()
    value = value.lower()
    clave_valor = (key,value)
    # print (f'{key}  | {value}')
    if key in configuracion.keys(): 
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        configuracion.update({key:value})
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(configuracion: dict, clave_valor: tuple):
    key, value = clave_valor
    key = key.lower()
    value = value.lower()
    if key in configuracion.keys():     
        configuracion[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        configuracion.update({'key':value})
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(configuracion: dict, key: str):
    key = key.lower()
    if key in configuracion.keys():     
        configuracion.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"    

def view_settings(configuracion: dict):
    if configuracion == {}:
        return f'No settings available.'
    resultado = "Current User Settings:\n"
    for clave, valor in configuracion.items():
        resultado += f"{clave.capitalize()}: {valor}\n"
    return resultado

test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}
# print (view_settings(test_settings))
pepe = add_setting(test_settings, ('TESTING', 'TRUE'))
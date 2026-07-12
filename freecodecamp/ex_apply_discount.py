def apply_discount(price, discount):
    # Verifico parametros
    if (not isinstance(price,(int,float))):
        return f"The price should be a number"
    
    if (not isinstance(discount,(int,float))):
        return f"The discount should be a number"
    
    if (price <= 0):
        return f"The price should be greater than 0"
    
    if (discount < 0 or discount > 100):
        return f"The discount should be between 0 and 100"
    
    # Calculo el descuento
    precio_final = price - (price * (discount / 100))
    return precio_final

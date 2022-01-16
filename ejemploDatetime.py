import datetime
# fecha que ingresa el terminal a taller
fechaIn = datetime.datetime(2017,5,12) # formato fecha es Anno mes Dia
# fecha de compra de telefono
fechaCompra = datetime.datetime(2017,4,3)

# como calculo los dias transcurridos
tiempo =  fechaIn - fechaCompra 
print(tiempo)


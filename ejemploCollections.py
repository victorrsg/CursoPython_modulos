# Subclase de diccionario utilizada para hacer cuentas
from collections import Counter
l = [1,2,3,4,1,2,3,1,2,1]
c= (Counter(l))
print(c)

# Se utilizan para crear diccionarios con un valor 
# por defecto aunque el registro no haya sido definido anteriormente.
from collections import defaultdict

# Otra subclase de diccionario que conserva el 
# orden en que añadimos los registros.
from collections import OrderedDict

# Subclase de las tuplas utilizada para crear pequeñas estructuras inmutables,
# parecidas a una clase y sus objetos pero mucho más simples.
from collections import namedtuple
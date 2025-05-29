# repo_structure
 Standard structure of a repository


Para ejecutar el código pararse en la carpeta del proyecto y ejecutar el siguiente comando:

```bash
python -m src.main.main
```
Nótese que no hay .py al final del comando, ya que el módulo main es un paquete y no un archivo.

Por otro lado, para importar funciones de otros files en el mismo paquete, se debe hacer de la siguiente manera:

```python
from src.lib.fun_definition import function
```
Esto es, importación relativa al paquete src, que es el paquete raíz del proyecto.
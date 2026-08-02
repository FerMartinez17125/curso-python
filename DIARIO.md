# Diario de aprendizaje

Referencia breve de Python, VS Code, Git y GitHub.

## Sesión 1: inicio del proyecto

### Python

- Una variable guarda un valor, pero no lo muestra en la terminal.
- `print(valor)` muestra un valor.
- `texto.upper()` devuelve el texto en mayúsculas.
- `texto.lower()` devuelve el texto en minúsculas.
- Los strings son inmutables: los métodos devuelven un string nuevo.

```python
texto = "Hola Fernando"
texto_mayusculas = texto.upper()
texto_minusculas = texto.lower()

print(texto)
print(texto_mayusculas)
print(texto_minusculas)
```

### VS Code

- El botón normal de ejecución utiliza la terminal integrada.
- `F5` utiliza la configuración de `.vscode/launch.json`.
- `"console": "externalTerminal"` abre una terminal independiente.

### Git

- Git guarda el historial local del proyecto.
- Un repositorio es una carpeta controlada por Git.
- `main` es la rama principal.
- Un commit es un punto guardado en el historial.
- El área de preparación contiene los cambios elegidos para el próximo commit.

#### Flujo habitual

```powershell
git status
git add .
git commit -m "Describe brevemente el cambio"
git push
```

#### Comandos iniciales utilizados

```powershell
git --version
git init
git status
git add .
git commit -m "Agrega estructura inicial y ejercicios de introduccion"
```

#### Detalles importantes

- `git add .` lleva un espacio antes del punto.
- `??` significa que Git todavía no sigue el archivo.
- `Changes to be committed` significa que el cambio está preparado.
- `working tree clean` significa que no hay cambios pendientes.
- Los avisos sobre `LF` y `CRLF` se refieren a saltos de línea; no son errores.

### GitHub

- GitHub guarda una copia remota del repositorio Git.
- `origin` es el nombre convencional del repositorio remoto principal.
- `fetch` descarga información del remoto.
- `push` sube commits al remoto.

```powershell
git remote add origin https://github.com/FerMartinez17125/curso-python.git
git remote -v
```

### Estado al finalizar esta nota

- Repositorio local creado.
- Primer commit creado en `main`.
- Repositorio público `curso-python` creado en GitHub.
- Remoto `origin` conectado.
- Pendiente: guardar este diario en un commit y hacer el primer `push`.

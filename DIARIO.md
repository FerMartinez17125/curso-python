# Diario de aprendizaje

Este es mi manual personal de Python, VS Code, Git y GitHub. La idea es poder volver dentro de varios años, seguir los pasos y recordar no solo los comandos, sino también para qué sirve cada uno.

## 1. Crear un repositorio local y publicarlo en GitHub

### La idea general

Git y GitHub no son lo mismo:

- **Git** trabaja en mi computadora y guarda el historial del proyecto.
- **GitHub** guarda una copia remota del repositorio y permite compartirlo.
- **Repositorio local**: carpeta del proyecto en mi computadora.
- **Repositorio remoto**: copia del proyecto alojada en GitHub.

El recorrido completo es:

```text
Crear proyecto → iniciar Git → preparar archivos → crear commit
→ crear repositorio vacío en GitHub → conectarlo → hacer push
```

### Lo que necesito

- Una cuenta de GitHub.
- Git instalado en la computadora.
- Una carpeta para el proyecto.
- Una terminal, por ejemplo PowerShell dentro de VS Code.

Compruebo que Git esté instalado:

```powershell
git --version
```

Si Windows no reconoce `git`, puedo instalarlo con:

```powershell
winget install --id Git.Git -e --source winget
```

Después cierro y vuelvo a abrir VS Code para que reconozca la instalación.

### Configurar mi identidad

Git coloca un nombre y un correo en cada commit. Esto normalmente se configura una sola vez en la computadora:

```powershell
git config --global user.name "MI_USUARIO_O_NOMBRE"
git config --global user.email "MI_CORREO"
git config --global init.defaultBranch main
```

Para comprobarlo:

```powershell
git config --global --get user.name
git config --global --get user.email
git config --global --get init.defaultBranch
```

Buena práctica: uso un correo verificado en GitHub para que la plataforma relacione mis commits con mi cuenta. Si el repositorio será público y no quiero mostrar mi correo real, puedo configurar el correo privado `noreply` proporcionado por GitHub.

### Crear o abrir la carpeta correcta

Antes de usar Git, debo asegurarme de estar dentro de la carpeta raíz del proyecto:

```powershell
cd "C:\ruta\de\mi\proyecto"
```

En este proyecto la raíz es:

```text
C:\Users\FGOMEXDI\Documents\PROGRAMACIÓN-PYTHON
```

No debo ejecutar `git init` a ciegas. Primero reviso dónde estoy porque la carpeta actual se convertirá en el repositorio.

### Iniciar el repositorio local

Dentro de la carpeta correcta ejecuto:

```powershell
git init
```

Esto crea una carpeta oculta llamada `.git`. Ahí vive el historial. No sube archivos a internet y no crea todavía ningún commit.

Compruebo el estado:

```powershell
git status
```

Mensajes habituales:

- `No commits yet`: todavía no existe ningún commit.
- `On branch main`: estoy en la rama principal.
- `?? archivo.py`: Git ve el archivo, pero todavía no lo sigue.
- `working tree clean`: no tengo cambios pendientes.

### Preparar el proyecto antes del primer commit

Conviene crear al menos:

- `README.md`: explica qué es el proyecto y cómo utilizarlo.
- `.gitignore`: indica qué archivos no debe guardar Git.
- Los primeros archivos funcionales del proyecto.

En Python, un `.gitignore` básico puede incluir:

```gitignore
__pycache__/
*.py[cod]
.venv/
venv/
.env
*.env
```

Buena práctica: nunca subo contraseñas, tokens, llaves API ni archivos `.env`.

### Preparar los archivos: `git add`

Primero reviso:

```powershell
git status
```

Después preparo todos los cambios:

```powershell
git add .
```

El espacio antes del punto es obligatorio:

- `git add.` es incorrecto porque Git interpreta `add.` como un comando.
- `git add` está incompleto porque no indica qué agregar.
- `git add .` prepara todos los cambios desde la carpeta actual.

También puedo preparar un solo archivo:

```powershell
git add nombre_del_archivo.py
```

Vuelvo a revisar:

```powershell
git status
```

`Changes to be committed` significa que los archivos están en el área de preparación, listos para el próximo commit.

### Crear el primer commit

Creo un punto guardado con un mensaje claro:

```powershell
git commit -m "Agrega estructura inicial del proyecto"
```

Un buen mensaje dice qué cambia. Ejemplos:

```text
Agrega ejercicio de métodos de strings
Corrige validación de edad
Documenta instalación del proyecto
```

Evito mensajes vagos como `cambios`, `cosas` o `prueba`.

Después compruebo:

```powershell
git status
git log --oneline
```

`root-commit` identifica el primer commit. El código corto que aparece, por ejemplo `199d170`, es el identificador del commit.

### Crear el repositorio vacío en GitHub

En GitHub:

1. Presiono `+` y selecciono **New repository**.
2. Elijo el propietario y un nombre sencillo, sin espacios ni acentos.
3. Agrego una descripción breve.
4. Elijo `Public` o `Private`.
5. Si el proyecto local ya tiene archivos, dejo sin marcar README, `.gitignore` y licencia.
6. Presiono **Create repository**.

El repositorio debe quedar vacío. GitHub mostrará una URL parecida a:

```text
https://github.com/USUARIO/REPOSITORIO.git
```

Buena práctica: no ejecuto las instrucciones para crear otro README o repetir `git init` si ya hice esos pasos localmente.

### Conectar el repositorio local con GitHub

Agrego el remoto con el nombre convencional `origin`:

```powershell
git remote add origin https://github.com/USUARIO/REPOSITORIO.git
```

Compruebo la conexión:

```powershell
git remote -v
```

Debe aparecer `origin` dos veces:

- `fetch`: dirección utilizada para descargar cambios.
- `push`: dirección utilizada para subir commits.

Agregar `origin` solo guarda la dirección. Todavía no sube archivos.

### Hacer el primer push

Subo la rama principal por primera vez:

```powershell
git push -u origin main
```

- `push`: sube commits.
- `origin`: repositorio remoto.
- `main`: rama que quiero subir.
- `-u`: relaciona mi `main` local con `origin/main`.

La primera vez GitHub puede abrir el navegador para iniciar sesión. Después de establecer la relación, normalmente basta con:

```powershell
git push
```

### Flujo normal después de la configuración

Cada vez que termine una mejora:

```powershell
git status
git add .
git commit -m "Describe el cambio realizado"
git push
```

En palabras sencillas:

1. Reviso qué cambió.
2. Selecciono qué guardar.
3. Creo el punto en el historial local.
4. Envío ese historial a GitHub.

### Errores y avisos que ya encontré

#### `git: 'add.' is not a git command`

Faltó el espacio. La forma correcta es:

```powershell
git add .
```

#### `Nothing specified, nothing added`

Ejecuté `git add` sin indicar archivos. Debo usar un nombre de archivo o un punto.

#### Aviso sobre `LF` y `CRLF`

Son formatos de salto de línea:

- `LF`: común en Linux y macOS.
- `CRLF`: común en Windows.

Es una advertencia, no un error. Git puede adaptar los saltos de línea al sistema operativo.

#### `nothing to commit, working tree clean`

No es un problema. Significa que todos los cambios ya están guardados en commits.

### Buenas prácticas que quiero mantener

- Ejecuto `git status` antes de `add`, antes de `commit` y cuando tenga dudas.
- Reviso los archivos antes de subirlos.
- Hago commits pequeños y relacionados con un objetivo.
- Escribo mensajes claros en presente: `Agrega`, `Corrige`, `Actualiza`.
- No guardo secretos ni datos personales innecesarios.
- No creo un repositorio distinto para cada archivo del mismo curso.
- Uso carpetas para separar secciones y temas.
- Uso `main` para una versión estable y ramas para experimentos más adelante.
- No uso comandos destructivos que no comprendo.
- No edito ni borro manualmente la carpeta oculta `.git`.

### Estado de este proyecto

- Repositorio local: `PROGRAMACIÓN-PYTHON`.
- Repositorio remoto: `FerMartinez17125/curso-python`.
- Rama principal: `main`.
- Remoto principal: `origin`.
- Primer commit: `199d170`.
- Primer `push`: completado correctamente.

## 2. Notas rápidas de Python y VS Code

### Strings en Python

- Una variable guarda un valor, pero no lo muestra.
- `print(valor)` muestra el valor en la terminal.
- `texto.upper()` devuelve un string en mayúsculas.
- `texto.lower()` devuelve un string en minúsculas.
- Los strings son inmutables: los métodos devuelven un string nuevo.

### Ejecución en VS Code

- El botón normal de ejecución utiliza la terminal integrada.
- `F5` utiliza `.vscode/launch.json`.
- `"console": "externalTerminal"` abre una terminal independiente.

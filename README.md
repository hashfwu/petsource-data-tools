# PetSource Data Tools

Herramienta diseñada para Pet Shops y tiendas caninas que proporciona análisis de datos y reconocimiento de emociones en perros.

# Tabla de Contenidos

- Características
- Requisitos
- Instalación
- Uso
- Estructura del Proyecto
- Despliegue
- Desarrollo
- Licencia

# Características

- Sistema de Recomendación - Basado en registros de ventas históricas
- Reconocimiento de Emociones - Análisis de emociones en perros a través de imágenes
- Dashboard Interactivo - Visualización de métricas y tendencias

# Requisitos

- **Python 3.12**
- **Git**
- **pip**

Las librerias necesarias  se hallan en el archivo `requirements.txt`. Se pueden instalar las dependencias de las siguientes formas:


# Instalación

Para correr la aplicación solo tienes que ejecutar el comando:

```bash
# Clonar el repositorio
git clone https://github.com/tuusuario/petsource-data-tools.git
cd petsource-data-tools

# Crear y activar entorno virtual
python -m venv .venv

# Activar entorno
# Windows:
.venv\Scripts\activate

# macOS/Linux:
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

Con Conda:

```bash
conda create --name env python=3.12
conda activate env
pip install -r requirements.txt
```

# Desarrollo

Para aportar al desarrollo de esta aplicacion sigue los siguientes pasos:

**1. Clona el repositorio**

```
git clone <repo>
cd <proyecto>
```

**2. Instala las dependencias**

Ver [# Dependencias].

**3. Edita y corre la aplicación**

Crea una nueva rama:

```
git create branch --name
```

Usa tu editor favorito y sientete libre de hacer las ediciones que gustes. Para correr el proyecto puedes ver la sección de [# Uso]. Puedes traer los cambios a tu computadora con:

```
git pull
```

Para hacer checkpoints de tus cambios puedes crear un commmit

```
git add <nombre-archivo>
git commmit -m "Nuevo mensaje"
```

Tanto las ramas como los commits deben seguir las convenciones de  [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)

**4. Sube tus cambios**

Una vez hecho tu cambios puedes hacer un merge para unir tus cambio a la raiz principal

```
git merge
```

Realiza un push al repositorio para subir tus cambios

```
git push
```

Esta debe seguir la convenciones de [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)

# Dependencias


**Con Venv:**

En Windows: 

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

En MacOs/Linux:

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```



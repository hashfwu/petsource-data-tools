# PetSource Data Tools

Herramienta diseñada para Pet Shops y tiendas caninas que proporciona análisis de datos y reconocimiento de emociones en perros.

# Tabla de Contenidos

- Características
- Requisitos
- Instalación
- Uso
- Estructura del Proyecto
- Desarrollo
- Despliegue

# Características

- **Sistema de Recomendación**: Basado en registros de ventas históricas
- **Reconocimiento de Emociones**: Análisis de emociones en perros a través de imágenes
- **Dashboard Interactivo**: Visualización de métricas y tendencias

# Requisitos

- **Python 3.12**
- **Git**
- **pip**

Las librerias necesarias se hallan en el archivo `requirements.txt` que deben ser instaladas para que el programa funcione.

# Instalación {#install}

Para correr la aplicación solo tienes que ejecutar el comando:

```bash
# Clonar el repositorio
git clone https://github.com/hashfwu/petsource-data-tools
cd petsource-data-tools
```
Con Venv:

```bash
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
# Crear entorno
conda create --name env python=3.12

# Activar entorno
conda activate env

# Instalar dependencias
pip install -r requirements.txt
```

# Uso {#use}

Para correr la aplicación ejecuta:

```bash
streamlit run app.py
```

# Estructura del proyecto

El proyecto usa la libreria de **Streamlit** para su desplieque. Por dentro usa la librerias de **TensorFlow**, **Scikit-Learn** y **Matplotlib**.

```
├── app.py
├── assets
│   └── style.css
├── models
│   └── model.h5
├── notebooks
├── pages
│   ├── page_01.py
│   ├── page_02.py
│   └── page_03.py
├── README.md
├── requirements.txt
└── utils
    ├── download_models.py
    └── __inti__.py
```

El modelo no se encuentra en este repositorio, si no que se descarga de [Google  Drive](https://drive.google.com/file/d/1ceGVgTTLos_b586g0HsdH6VQMuVQkEfo/view?usp=sharing)

**Nota**: Se debe considerar llevar el modelo a HuggingFaces.

# Desarrollo

Para aportar al desarrollo de esta aplicacion sigue los siguientes pasos:

**1. Clona el repositorio**

```
git clone https://github.com/hashfwu/petsource-data-tools
cd petsource-data-tools
```

**2. Instala las dependencias**

Ver [Instalación](#install).

**3. Edita y corre la aplicación**

Crea una nueva rama:

```bash
git checkout -b nombre-rama
```

Usa tu editor favorito y sientete libre de hacer las ediciones que gustes. Para correr el proyecto puedes ver la sección de [Uso](#use). Puedes traer los cambios a tu computadora con:

```bash
git pull origin main
```

Para hacer checkpoints de tus cambios puedes crear un commmit:

```bash
# Prepara el archivo para el commit
git add <nombre-archivo>

# Crea el commit con un mensaje descriptivo
git commit -m "refactor: descripción del cambio"
```

Alternativamente puedes usar algun pluggin GUI para Git como el que viene por defecto en **VSCode** o el que venga por defecto en tu IDE.


**4. Sube tus cambios**

Realiza un push al repositorio para subir tus cambios

```bash
git push origin nombre-rama
```

Para integrar tus cambios a la rama principal (main), primero regresa a ella y luego realiza la unión:

```bash
# Cambia a la rama principal
git checkout main

# Une los cambios de tu rama a la principal
git merge nombre-rama

# Sube los cambios integrados al repositorio remoto
git push origin main
```

Tanto las ramas como los commits deben seguir las convenciones de  [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

# Despliegue

La aplicación se encuentra ya desplegada en [Streamlit Could](https://share.streamlit.io), de momento solamente accesible para ciertos usuarios mientras la app este en fase de desarrallo y se libera solamente para pruebas.



# Agente de IA Académico — Examen Práctico

**Estudiante:** Edy Martinez
**Examen:** Agente de IA con LM Studio y Streamlit

Aplicación web en Streamlit que implementa un agente de IA conectado a un
modelo Instruct liviano ejecutado localmente con LM Studio. El agente
responde preguntas académicas sobre tecnología, programación o
inteligencia artificial, explicando el concepto, dando un ejemplo, una
aplicación práctica y una pregunta de comprobación.

## Estructura del proyecto

```
EdyMartinez_AgenteIA/
├── app.py             # Aplicación Streamlit
├── requirements.txt   # Dependencias
├── README.md
└── capturas/           # Evidencias (LM Studio + app funcionando)
```

## Requisitos

- Python 3.10 o superior.
- [LM Studio](https://lmstudio.ai/) instalado.
- Un modelo Instruct liviano descargado, por ejemplo:
  - Qwen2.5-1.5B-Instruct o Qwen2.5-3B-Instruct
  - Llama-3.2-1B-Instruct o Llama-3.2-3B-Instruct
  - Phi-3-mini-instruct

## 1. Crear y activar el entorno virtual

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

## 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 3. Configurar LM Studio

1. Abre LM Studio y descarga uno de los modelos Instruct livianos listados
   arriba (pestaña **Search**).
2. Ve a la pestaña **Chat** o **Local Server** y carga el modelo.
3. Ve a la pestaña **Developer** y activa **Start Server**. El servidor
   queda disponible por defecto en `http://localhost:1234`.
4. Copia el identificador exacto del modelo que muestra LM Studio.

## 4. Ejecutar la aplicación

Antes de ejecutar, confirma que:

- LM Studio esté abierto.
- El modelo Instruct liviano esté cargado.
- El servidor local esté iniciado (puerto `1234`).

Luego ejecuta:

```bash
streamlit run app.py
```

Abre el navegador en <http://localhost:8501>. En la barra lateral de la
aplicación, escribe el identificador **exacto** del modelo cargado en LM
Studio (por defecto viene `qwen2.5-1.5b-instruct`).

## Cómo funciona el código

- `app.py` construye la interfaz: título, descripción, campo de texto para
  la consulta y botón **Consultar al Agente**.
- Al hacer clic, valida que la consulta no esté vacía y crea un cliente
  `OpenAI` apuntando a la API local de LM Studio (`http://localhost:1234/v1`).
- Envía un **System Prompt** que obliga al modelo a responder en este
  orden: explicación, ejemplo, aplicación práctica y pregunta de
  comprobación.
- Si LM Studio no está disponible (servidor apagado, modelo no cargado o
  nombre de modelo incorrecto), se captura la excepción y se muestra un
  mensaje de error explicando qué revisar.

## Evidencias

En la carpeta `capturas/` se incluyen dos capturas de pantalla:

1. `lm-studio-modelo-cargado.png` — LM Studio con el modelo cargado y el
   servidor local iniciado.
2. `app-streamlit-funcionando.png` — la aplicación en Streamlit mostrando
   una consulta y la respuesta generada por el agente.

## Repositorio de GitHub

Enlace: `<pegar aquí la URL del repositorio de GitHub>`

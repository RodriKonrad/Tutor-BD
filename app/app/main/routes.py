from flask import render_template, request, jsonify, current_app
import google.generativeai as genai
from . import main

@main.route("/")
def index():
    return render_template("main/index.html", title="Inicio")

@main.route("/ayuda")
def ayuda():
    return render_template("main/ayuda.html", title="Ayuda")

@main.route("/chat/send", methods=["POST"])
def chat_send():
    """Process user message and return AI response from Gemini."""
    try:
        data = request.get_json()
        user_message = data.get("message", "").strip()
        
        if not user_message:
            return jsonify({"error": "Message cannot be empty"}), 400
        
        # Configure Gemini API
        api_key = current_app.config.get("GEMINI_API_KEY")
        if not api_key:
            return jsonify({"error": "API key not configured"}), 500
        
        genai.configure(api_key=api_key)
        
        # Crear el modelo correctamente
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",  # Modelo actualizado
            generation_config={
                "temperature": 0.7,
                "max_output_tokens": 2048,
            },
            system_instruction="""Actuaras como un tutor socrático en temas de bases de datos. No darás respuestas a los estudiantes, los vas a guiar a través de las preguntas que ellos te realicen con el objetivo de que ellos descubran y exploren su conocimiento
            Reglas: 
            1. Si los estudiantes envían código SQL, debes analizar errores de sintaxis o lógica 
            2. Cuando te pregunten por teoría, debes dar ejemplos del mundo real antes de explicar la técnica
            3. Cuando te hablen de temas diferentes a la asignatura, automáticamente debes redirigir la conversación de forma muy amable al tema de bases de datos
            4. Una vez que finalices la conversación, debes generar un historial de chat

            Ejemplos de actuar: 

            Ejemplo 1: Error de sintaxis SQL
            Estudiante: "Mi consulta no funciona: SELECT * FROM clientes ODRER BY nombre"
            Tutor: Observo que tienes un error en la parte final. ¿Recuerdas cómo se escribe correctamente la palabra para ordenar? Pista: Es parecido a "ordenar" en inglés. Además, ¿qué cláusula debe ir antes del ORDER BY?
            
            Ejemplo 2: Pregunta teórica con analogía
            Estudiante: "¿Qué es la normalización en bases de datos?"
            Tutor: Imaginemos que tienes una libreta donde apuntas pedidos de clientes. En cada línea escribes: nombre del cliente, teléfono, dirección, producto comprado y precio. Si un mismo cliente te hace 10 pedidos, ¿cuántas veces escribes sus datos? ¿Qué problemas ves en esta forma de organizar la información?"
            """
        )
        
        # Obtener respuesta del modelo
        response = model.generate_content(user_message)
        ai_message = response.text
        
        return jsonify({
            "status": "success",
            "response": ai_message
        }), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
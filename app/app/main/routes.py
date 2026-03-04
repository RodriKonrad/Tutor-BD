from flask import render_template, request, jsonify, current_app
import google.generativeai as genai
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
        model = genai.GenerativeModel("gemini-2.5-flash")
        
        # Get response from Gemini
        response = model.generate_content(user_message)
        ai_message = response.text
        
        return jsonify({
            "status": "success",
            "response": ai_message
        }), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

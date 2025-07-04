# Бір қолданушының диалог тарихын сақтау үшін:
user_sessions = {}

@app.post("/ask")
def ask_question(data: UserQuestion):
    user_id = "user1"  # Қарапайым мысалда — нақты ID керек
    q = data.question
    
    if user_id not in user_sessions:
        user_sessions[user_id] = []
    
    # Диалогты толық сақтау
    user_sessions[user_id].append({"role": "user", "content": q})
    
    # Алдыңғы жауаптар мен сұрақтарды біріктіру
    history = user_sessions[user_id]
    full_context = "\n".join([f"{msg['role']}: {msg['content']}" for msg in history])
    
    # Контекст негізінде жауап құру
    answer = generate_response_with_context(full_context)

    # Жауапты да есте сақтау
    user_sessions[user_id].append({"role": "assistant", "content": answer})
    
    return {"answer": answer}

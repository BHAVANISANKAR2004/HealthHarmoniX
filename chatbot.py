from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
translator = pipeline("translation", model=model, tokenizer=tokenizer)

languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te"
}

health_guidance = {
    "fever": "Stay hydrated, rest well, and monitor your temperature. If it persists beyond 3 days, consult a doctor.",
    "cough": "Avoid cold drinks, rest your voice, and consider warm fluids. Seek medical help if chronic.",
    "diarrhea": "Consume ORS solution, avoid solid food for a while, and see a physician if symptoms worsen."
}

def get_response(user_input, lang):
    base_response = "General guidance not available. Please consult a medical professional."
    for key in health_guidance:
        if key.lower() in user_input.lower():
            base_response = health_guidance[key]
            break

    if lang != "English":
        translation = translator(base_response, src_lang="en", tgt_lang=languages[lang])
        return translation[0]['translation_text']
    return base_response

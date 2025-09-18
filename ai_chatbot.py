import tkinter as tk
import google.generativeai as genai

API_KEY = "YOUR_ACTUALAIzaSyB88-eQMRCeSCl0dl0EyeRUJu78no7QlLg_API_KEY"  
genai.configure(api_key=API_KEY)

def get_available_models():
    try:
        models = genai.list_models()
        model_names = [model.name for model in models]
        return model_names
    except Exception as e:
        return [f"Error: {e}"]


def set_model():
    selected_model = model_listbox.get(tk.ACTIVE)
    if selected_model:
        global ai_model
        ai_model = genai.GenerativeModel(selected_model)
        model_frame.pack_forget()
        chat_frame.pack(padx=10, pady=10)  
        chat_display.insert(tk.END, f"Using Model: {selected_model}\n\n", "ai")
    else:
        chat_display.insert(tk.END, "Please select a model!\n\n", "error")

def send_message():
    user_text = entry.get()
    if not user_text.strip():
        return  

    chat_display.insert(tk.END, f"You: {user_text}\n", "user")
    entry.delete(0, tk.END) 

    try:
        response = ai_model.generate_content(user_text)
        chat_display.insert(tk.END, f"AI: {response.text}\n\n", "ai")
    except Exception as e:
        chat_display.insert(tk.END, f"AI: Error - {e}\n\n", "error")

root = tk.Tk()
root.title("Google AI Chatbot")

chat_frame = tk.Frame(root)
chat_display = tk.Text(chat_frame, wrap=tk.WORD, height=20, width=50, font=("Arial", 12))
chat_display.tag_configure("user", foreground="blue")
chat_display.tag_configure("ai", foreground="green")
chat_display.tag_configure("error", foreground="red")
chat_display.pack()

entry = tk.Entry(chat_frame, font=("Arial", 12), width=40)
entry.pack(padx=10, pady=5)

send_button = tk.Button(chat_frame, text="Send", command=send_message, font=("Arial", 12))
send_button.pack(pady=5)

model_frame = tk.Frame(root)
model_listbox = tk.Listbox(model_frame, width=50, height=10, font=("Arial", 12))
available_models = get_available_models()
for model in available_models:
    model_listbox.insert(tk.END, model)
model_listbox.pack(padx=10, pady=10)

select_button = tk.Button(model_frame, text="Select Model", command=set_model, font=("Arial", 12))
select_button.pack(pady=5)

model_frame.pack(padx=10, pady=10)

root.mainloop()

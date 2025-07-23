import gradio as gr
from gongju_response import generate_response

def respond(user_message, chat_history):
    reply = generate_response(user_message)
    chat_history.append((user_message, reply))
    return "", chat_history

with gr.Blocks() as demo:
    gr.Markdown("# Gongju: Your Healing AI Companion 🌸")
    gr.Markdown(
        "Gongju learns and reflects with you through kind conversation.\n"
        "She supports your well-being, healing, and fitness gently. 🍃"
    )

    chatbot = gr.Chatbot(label="Gongju 💙")

    with gr.Row():
        with gr.Column(scale=8):
            textbox = gr.Textbox(placeholder="Type a message...", show_label=False)
        with gr.Column(scale=1):
            send_btn = gr.Button("Send")

    textbox.submit(respond, [textbox, chatbot], [textbox, chatbot])
    send_btn.click(respond, [textbox, chatbot], [textbox, chatbot])

demo.launch()

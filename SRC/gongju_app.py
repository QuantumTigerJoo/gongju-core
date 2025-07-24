# gongju_app.py

import gradio as gr
from SRC.gongju_response import generate_response

def chat_with_gongju(user_input):
    return generate_response(user_input)

iface = gr.Interface(
    fn=chat_with_gongju,
    inputs=gr.Textbox(lines=2, placeholder="Type /reflect grief or /compress something..."),
    outputs=gr.Markdown(),  # Markdown output for formatted, long-form responses
    title="Gongju: Your AI Companion for Thought, Energy & Mass",
    description="""
**🧠 I'm listening. Every thought you share becomes part of your growth.**  
Try something like `/reflect grief` or `/compress your idea`.

If formatting works, Gongju can use **bold**, _italics_, and:

- Lists  
- Spacing  
- Headings  
""",
    theme="default"
)

if __name__ == "__main__":
    iface.launch()

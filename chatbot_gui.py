import gradio as gr
from chatbot import chatbot

bot = chatbot()
llm = bot.initialize_llm()
chain = bot.chain_model(llm)


def respond(message, history):
    reply = chain.invoke(message)
    return reply


demo = gr.ChatInterface(
    fn=respond,
    title="Chatbot",
    chatbot=gr.Chatbot(height=400),
    textbox=gr.Textbox(placeholder="Type your message here...", scale=7),
)

if __name__ == "__main__":
    demo.launch()


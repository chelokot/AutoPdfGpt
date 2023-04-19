
import numpy as np
import gradio as gr
from sklearn.neighbors import NearestNeighbors
from Recommender import Recommender
from config import openai_api_key

recommender = Recommender(openai_api_key)

title = 'PDF GPT'
description = """ What is PDF GPT ?
1. The problem is that Open AI has a 4K token limit and cannot take an entire PDF file as input. Additionally, it sometimes returns irrelevant responses due to poor embeddings. ChatGPT cannot directly talk to external data. The solution is PDF GPT, which allows you to chat with an uploaded PDF file using GPT functionalities. The application breaks the document into smaller chunks and generates embeddings using a powerful Deep Averaging Network Encoder. A semantic search is performed on your query, and the top relevant chunks are used to generate a response.
2. The returned response can even cite the page number in square brackets([]) where the information is located, adding credibility to the responses and helping to locate pertinent information quickly. The Responses are much better than the naive responses by Open AI."""

with gr.Blocks() as demo:

    gr.Markdown(f'<center><h1>{title}</h1></center>')
    gr.Markdown(description)

    with gr.Row():
        
        with gr.Group():
            file = gr.File(label='Upload your PDF/ Research Paper / Book here', file_types=['.pdf'])
            question = gr.Textbox(label='Enter your question here')
            btn = gr.Button(value='Submit')
            btn.style(full_width=True)

        with gr.Group():
            answer = gr.Textbox(label='The answer to your question is :')

        btn.click(recommender.question_answer, inputs=[file, question], outputs=[answer])


demo.launch(degub=True)
# This utils functions are based on repo https://github.com/bhaskatripathi/pdfGPT
# Which is the main source of inspiration for this project.

import fitz
import re
from deep_translator import GoogleTranslator


def preprocess_text(text):
    text = text.replace('\n', ' ')
    text = re.sub('\s+', ' ', text)
    return text


def pdf_to_text(path):
    text = ''
    with fitz.open(path) as doc:
        for page_num in range(doc.page_count):
            page_text = doc.load_page(page_num).get_text("text")
            page_text = preprocess_text(page_text)
            text += page_text + ' '

    return text


def text_to_chunks(text, words_per_chunk = 100):
    words = text.split(' ')
    chunks = []
    for i in range(0, len(words), words_per_chunk):
        chunk = ' '.join(words[i:(i+words_per_chunk)])
        chunks.append(chunk)
    return chunks


def translate_chunks(chunks):
    translated_chunks = []
    for chunk in chunks:
        translated_chunk = GoogleTranslator(source='auto', target='en').translate(chunk)
        translated_chunks.append(translated_chunk)
    return translated_chunks


def add_indices(chunks):
    chunks_with_indices = []
    for i, chunk in enumerate(chunks):
        chunks_with_indices.append(f'[{i}] {chunk}')
    return chunks_with_indices


def pdf_to_chunks(path, recursive_summarizer, words_per_chunk = 100):
    text = pdf_to_text(path)
    chunks = text_to_chunks(text, words_per_chunk)
    chunks = translate_chunks(chunks)
    chunks = recursive_summarizer.get_with_summarized_chunks(chunks)
    chunks = add_indices(chunks)
    return chunks
    
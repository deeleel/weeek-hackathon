import gradio as gr
import os
import pickle
# os.system('python -m spacy download en_core_web_sm')
import spacy
from spacy import displacy

nlp = pickle.load(open("nlp.p", 'rb'))
# nlp = model.to_disc('my_model')
# nlp = spacy.from_disk("../spacy/final_2/")

def text_analysis(text):
    doc = nlp(text)
    html = displacy.render(doc, style="ent", page=True)
    html = (
        "<div style='max-width:100%; max-height:360px; overflow:auto'>"
        + html
        + "</div>"
    )
    pos_count = {
        "char_count": len(text),
        "token_count": len(doc.ents),
    }
    # pos_tokens = []
    #
    # for token in doc:
    #     pos_tokens.extend([(token.text, "NOUN"), (" ", None)])

    return pos_count, html

demo = gr.Interface(
    text_analysis,
    gr.Textbox(placeholder="Enter sentence here..."),
    ["json", "html"],
    examples=[
        ["Создать задачу : Подготовить отчет к 15:00 завтра на Анну"],
        ["Создать заметку: Проверить документацию к 9 : 30 утра завтра на Дениса"],
    ],
)

demo.launch()

from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_transformers import Html2TextTransformer


def html_to_text(url):
    loader = WebBaseLoader(url)
    html = loader.load()

    html2text = Html2TextTransformer()
    docs = html2text.transform_documents(html)
    text = docs[0].page_content
    return text

from src.extraction import *
import pandas as pd

articles = grep_articles("6g", 10)
df = pd.DataFrame(articles)
df.to_excel("articles.xlsx")

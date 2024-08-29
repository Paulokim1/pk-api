from fastapi import FastAPI, Query
import os
import uvicorn
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd


df = pd.read_csv("data/data.csv")
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['abstract'])

app = FastAPI()

@app.get("/query")
def query_route(query: str = Query(..., description="Search query")):
    df_temp = df 
    query_vector = vectorizer.transform([query])

    scores = np.array(X.dot(query_vector.T).todense()).flatten()

    # Add scores to the DataFrame
    df_temp['Relevance_Score'] = scores
    
    df_temp_threshhold = df_temp[df_temp['Relevance_Score'] > 0]

    # Sort by relevance score in descending order
    sorted_df = df_temp_threshhold.sort_values(by='Relevance_Score', ascending=False)

    results = []
    for index, row in sorted_df.head(10).iterrows():
        relevant_document = {
            'title': row['title'],
            'content': row['abstract'],
            'relevance': row['Relevance_Score']
        }
        results.append(relevant_document)

    return {"results": results, "message": "OK"}

def run():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    run()
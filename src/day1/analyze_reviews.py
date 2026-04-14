import os
import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from src.day1.models import ReviewAnalysis
from typing import List

load_dotenv("gen/.env")

def analyze_reviews():
    reviews_file = "gen/data/reviews/reviews.jsonl"
    if not os.path.exists(reviews_file):
        print(f"Error: {reviews_file} not found.")
        return

    # 1. Read first 10 reviews
    reviews_text = []
    with open(reviews_file, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i >= 10:
                break
            review = json.loads(line)
            reviews_text.append(f"Rating: {review['rating']} - Comment: {review['comment']}")

    all_reviews_prompt = "\n".join(reviews_text)

    # 2. Setup Gemini
    llm = ChatGoogleGenerativeAI(
        model="gemini-flash-latest",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )
    
    # 3. Use structured output
    structured_llm = llm.with_structured_output(ReviewAnalysis)
    
    print("Analyzing first 10 reviews with Gemini...")
    analysis = structured_llm.invoke(
        f"Analyze these customer reviews and provide a structured summary:\n\n{all_reviews_prompt}"
    )

    # 4. Print results
    print("\n--- Review Analysis ---")
    print(f"Overall Sentiment: {analysis.overall_sentiment}")
    print(f"Summary: {analysis.summary}")
    print(f"Top Complaints: {', '.join(analysis.top_complaints)}")
    print(f"Critical Status: {'YES' if analysis.is_critical else 'NO'}")

if __name__ == "__main__":
    analyze_reviews()

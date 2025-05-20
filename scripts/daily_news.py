"""Daily News Analyzer

이 스크립트는 뉴스 API를 통해 최신 뉴스를 가져와
OpenAI API를 사용해 간단히 요약 및 인사이트를 생성합니다.
환경 변수에서 다음 정보를 읽습니다.
- NEWS_API_KEY: 뉴스 API 키
- OPENAI_API_KEY: OpenAI API 키
"""

import os
import datetime
import requests
import openai

NEWS_API_URL = "https://newsapi.org/v2/top-headlines"


def fetch_news(api_key: str, category: str = "business", country: str = "kr", page_size: int = 5):
    """뉴스 API에서 최신 기사를 가져옵니다."""
    params = {
        "apiKey": api_key,
        "category": category,
        "country": country,
        "pageSize": page_size,
    }
    response = requests.get(NEWS_API_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    return [article["title"] + "\n" + article.get("description", "") for article in data.get("articles", [])]


def analyze_news(news_list, model="gpt-3.5-turbo"):
    """OpenAI API를 사용하여 뉴스 요약 및 인사이트를 생성합니다."""
    prompt = "\n\n".join(news_list) + "\n\n위 기사들을 요약하고 주요 인사이트를 제시해 주세요."
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response["choices"][0]["message"]["content"].strip()


def main():
    news_api_key = os.getenv("NEWS_API_KEY")
    openai.api_key = os.getenv("OPENAI_API_KEY")

    if not news_api_key or not openai.api_key:
        raise RuntimeError("환경 변수 NEWS_API_KEY와 OPENAI_API_KEY를 설정해야 합니다.")

    news_list = fetch_news(news_api_key)
    analysis = analyze_news(news_list)

    today = datetime.date.today().isoformat()
    output_file = f"analysis_{today}.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"# {today} 뉴스 분석\n\n")
        for item in news_list:
            f.write(f"- {item}\n")
        f.write("\n## AI 분석\n")
        f.write(analysis)
    print(f"분석 결과를 {output_file} 파일에 저장했습니다.")


if __name__ == "__main__":
    main()

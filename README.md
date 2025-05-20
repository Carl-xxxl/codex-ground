# Daily Issue AI Repository

이 저장소는 매일 업데이트 되는 경제 및 시사 뉴스를 자동으로 수집하고
AI를 활용해 분석한 뒤 간단한 인사이트를 제공하기 위한 초안 프로젝트입니다.

## 구성
- `scripts/daily_news.py` : 뉴스 수집 및 분석을 담당하는 파이썬 스크립트
- `requirements.txt` : 필요한 파이썬 패키지 목록

## 사용 방법
1. Python 3.8 이상 환경을 준비합니다.
2. 필요한 패키지를 설치합니다.
   ```bash
   pip install -r requirements.txt
   ```
3. 환경 변수에 다음 값을 설정합니다.
   - `NEWS_API_KEY` : 뉴스 데이터를 가져오기 위한 API 키
   - `OPENAI_API_KEY` : 뉴스 요약 및 인사이트 생성을 위한 OpenAI API 키
4. 스크립트를 실행합니다.
   ```bash
   python scripts/daily_news.py
   ```

## 자동화
- 크론(cron) 등을 활용해 위 스크립트를 매일 실행하면
  매일 업데이트 되는 뉴스를 자동으로 분석할 수 있습니다.

## 향후 과제
- 다양한 뉴스 소스 추가
- 분석 결과의 저장 및 시각화
- 다국어 지원

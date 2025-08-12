# love-letter-lab
연애 편지를 템플릿+경량 생성으로 만들어 주고, 퍼스널리티 기반 감정 점수(0~1)로 호감도를 가시화하는 미니프로젝트. Flask + Transformers, Colab 데모/녹화 중심.

# 프로젝트명: Love Letter Lab — AI 연애 작문소

## 개요

- 템플릿+경량 생성으로 연애 편지(고백/위로/격려)를 생성하고, 퍼스널리티 가중치를 반영한 감정 점수(0~1)로 호감도를 시각화하는 미니프로젝트.

- 스택: Flask, Python, Hugging Face Transformers(경량 디코더/인코더), Colab 데모/녹화.

## 기능

- 편지 생성: 관계/상황/톤/길이 입력 → 편지 텍스트 생성(가드레일: 금칙/존댓/길이/반복)

- 호감도 점수: 룰/사전 기반 감정점수 + 퍼스널리티 벡터 가중합 → 시그모이드(0~1)

- 데모: 샘플 입력/스냅샷 JSON으로 안정 재현, 녹화본 제공

## 빠른 실행

- Python 3.10+

- pip install -r requirements.txt

- flask run 또는 python app/main.py

- Colab 노트북은 notebooks/ 참조(환경 셀 포함)

## 폴더 구조

- app/: Flask 라우트와 페이지

- nlp/: templates.py, scoring.py

- config/: personality_presets.json, reason_rules.json

- data/: samples.json, cache.json(내부 스냅샷; 원천 데이터 없음)

- notebooks/: 기능별 ipynb(검증 셀 포함)

- docs/: 안전 가드레일·데모 가이드

## 데이터 및 라이선스

- 본 레포는 코드와 소규모 샘플만 포함합니다. AI-Hub 등 외부 데이터는 재배포하지 않습니다.

- Code License: MIT (데이터는 각 출처 약관 준수)

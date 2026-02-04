# Soccer AI Predictor PRO

## Installation

1. Crée un dépôt GitHub et ajoute ces fichiers
2. Connecte le dépôt à Render.com
3. Build command: `pip install -r requirements.txt && playwright install chromium`
4. Start command: `python app.py`

## Utilisation

- Endpoint API: POST `/analyze`
- JSON Body: `{ "url": "https://www.365scores.com/..." }`
- Réponse JSON:
```json
{
  "match": { "home": "Flamengo", "away": "Internacional", "competition": "Brasileirão Série A", "time": "21:00" },
  "prediction": { "main_score": "2-1", "others": ["1-1","2-0"], "winner": "Flamengo", "btts": "YES", "over_under": "Over 2.5", "mtft": "X / 1" }
}

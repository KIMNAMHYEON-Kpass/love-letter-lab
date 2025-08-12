import math

def score_affinity(text: str, personality: dict):
  base = 0.5
  pos_words = ["좋", "고맙", "따뜻", "응원", "함께", "설렘"]
  neg_words = ["미안", "불안", "걱정", "슬픔"]
  bonus = sum(0.05 for w in pos_words if w in text) - sum(0.05 for w in neg_words if w in text)
  raw = base + bonus
  score = 1/(1+math.exp(-(raw-0.5)*4))
  reasons = [{"rule":"positive_words","count":sum(w in text for w in pos_words)},
    {"rule":"negative_words","count":sum(w in text for w in neg_words)}]
  return float(score), reasons

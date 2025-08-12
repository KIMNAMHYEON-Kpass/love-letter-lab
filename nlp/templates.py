def generate_letter(name, relation, situation, tone="달달", length="short"):
  sentences = [
    f"{name}님, {situation} 속에서도 마음이 자꾸 따뜻해집니다.",
    f"{relation}로 지내며 알게 된 소중함을 조심스레 전해요.",
    "부담되지 않는 선에서, 더 자주 함께 걷고 싶습니다."
  ]
  return " ".join(sentences) if length=="short" else " ".join(sentences*3)[:600]

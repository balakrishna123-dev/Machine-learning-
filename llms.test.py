from llm_utils import generate_explanation

explanation = generate_explanation("rice", "N=90, P=42, K=43, Temp=20.87°C, Humidity=82%, pH=6.5, Rainfall=202mm")
print(explanation)

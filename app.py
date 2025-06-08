from llm_interface import run_llm

print("🧬 GeneSpeak: Ask about gene expression")
while True:
    q = input("🔍 Ask a question (or 'exit'): ")
    if q.lower() == 'exit':
        break
    try:
        result = run_llm(q)
        print("📊 Result:", result)
    except Exception as e:
        print("❌ Error:", str(e))

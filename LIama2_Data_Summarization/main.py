from meta_llama import MetaLlama2

model = MetaLlama2(model_name='meta-llama-2')

prompt = "What is the future of artificial intellegence?"
generated_text = model.generate_text(prompt)

print("Generated Text:", generated_text)

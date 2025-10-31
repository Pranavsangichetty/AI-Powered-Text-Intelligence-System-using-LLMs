from transformers import AutoTokenizer, AutoModelForCausalLM

def generate_sql_query(nl_query):
    model_name = "defog/sqlcoder-7b-2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    inputs = tokenizer(nl_query, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=100)
    sql_query = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return sql_query


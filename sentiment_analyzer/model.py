from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline


class Model:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("savasy/bert-base-turkish-sentiment-cased")
        self.model = AutoModelForSequenceClassification.from_pretrained("savasy/bert-base-turkish-sentiment-cased")
        self.sa = pipeline("sentiment-analysis", tokenizer=self.tokenizer, model=self.model)
        
    def predict(self, text):
        result = self.sa(text)[0]
        return (result.get("label"), result.get("score"))


model = Model()

def get_model():
    return model
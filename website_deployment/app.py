from flask import Flask, render_template, request
from gradio_client import Client

app = Flask(__name__)

# Initialize the Gradio Client
client = Client("mdfaisalahmed025/Multilabel-News-Article-Classifier")

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        input_text = request.form.get('text', '')
        
        try:
            # 1. Get the raw dictionary from your function
            output = predict_genres(input_text)
            
            # 2. Access 'confidences' directly (based on your log output)
            confidence_list = output['confidences']
            
            # 3. Filter labels with confidence >= 0.5
            labels = [elem['label'] for elem in confidence_list if elem['confidence'] >= 0.5]
            
            # 4. Build the comma-separated string
            label_text = ""
            for idx, label in enumerate(labels):
                label_text = label_text + label
                if idx != len(labels) - 1: 
                    label_text = label_text + ", "
            
            # 5. Render your result template
            return render_template("result.html", input_text=input_text, output_text=label_text)
        
        except Exception as e:
            return f"Error: {str(e)}", 500
            
    return render_template("index.html")

def predict_genres(input_text):
    # This matches the api_name and parameter from your docs
    result = client.predict(
        description=input_text,
        api_name="/classify_news_category"
    )
    return result

if __name__ == "__main__":
    app.run(debug=True)
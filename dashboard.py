from flask import Flask, render_template_string
import json
import plotly.graph_objs as go
import plotly.offline as pyo

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Modellmetriken Dashboard</title>
    <meta http-equiv="refresh" content="10">
</head>
<body>
    <h1>Modellmetriken über Versionen</h1>
    {{ plot_div|safe }}
</body>
</html>
"""

@app.route("/")
def dashboard():
    with open("metrics.json", "r") as f:
        metrics = json.load(f)

    versions = [m["version"] for m in metrics]
    accuracy = [m["accuracy"] for m in metrics]
    precision = [m["precision"] for m in metrics]
    recall = [m["recall"] for m in metrics]
    f1 = [m["f1_score"] for m in metrics]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=versions, y=accuracy, mode='lines+markers', name='Accuracy'))
    fig.add_trace(go.Scatter(x=versions, y=precision, mode='lines+markers', name='Precision'))
    fig.add_trace(go.Scatter(x=versions, y=recall, mode='lines+markers', name='Recall'))
    fig.add_trace(go.Scatter(x=versions, y=f1, mode='lines+markers', name='F1-Score'))

    fig.update_layout(title="Modellmetriken", xaxis_title="Version", yaxis_title="Wert", yaxis_range=[0, 1.05])

    plot_div = pyo.plot(fig, output_type='div', include_plotlyjs='cdn')
    return render_template_string(TEMPLATE, plot_div=plot_div)

if __name__ == "__main__":
    app.run(debug=True, port=5050)

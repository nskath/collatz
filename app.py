from flask import Flask, request, render_template_string
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            number = int(request.form.get('number'))
            sequence = collatz_sequence(number)
            max_value = max(sequence)
            steps = len(sequence) - 1

            # Plotting the sequence
            plt.figure()
            plt.plot(sequence, label=f'Collatz Path for {number}')
            plt.legend()
            plt.title('Collatz Conjecture Path')
            plt.xlabel('Step')
            plt.ylabel('Value')

            # Convert plot to PNG image
            img = io.BytesIO()
            plt.savefig(img, format='png')
            plt.close()
            img.seek(0)
            plot_url = base64.b64encode(img.getvalue()).decode()

            return render_template_string(TEMPLATE, plot_url=plot_url, max_value=max_value, steps=steps)
        except ValueError:
            return render_template_string(TEMPLATE, error="Please enter a valid integer.")

    return render_template_string(TEMPLATE)

TEMPLATE = """
<!doctype html>
<html>
<head><title>Collatz Conjecture</title></head>
<body>
    <h1>Collatz Conjecture Calculator</h1>
    <form method="post">
        Enter a number: <input type="text" name="number"/>
        <input type="submit" value="Calculate"/>
    </form>
    {% if plot_url %}
        <h2>Results</h2>
        <img src="data:image/png;base64,{{ plot_url }}">
        <p>Maximum value in path: {{ max_value }}</p>
        <p>Number of steps: {{ steps }}</p>
    {% endif %}
    {% if error %}
        <p style="color: red;">{{ error }}</p>
    {% endif %}
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)

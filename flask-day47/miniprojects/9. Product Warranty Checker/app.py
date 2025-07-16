from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

# Dummy warranty data
warranty_data = {
    "ABC123": {"product": "Laptop", "years": 2},
    "XYZ789": {"product": "Smartphone", "years": 1},
    "LMN456": {"product": "Tablet", "years": 3},
}

@app.route('/check-warranty', methods=['GET', 'POST'])
def check_warranty():
    if request.method == 'POST':
        serial = request.form['serial']
        return redirect(url_for('warranty_result', serial=serial))
    return render_template('check_warranty.html')

@app.route('/result')
def warranty_result():
    serial = request.args.get('serial')
    data = warranty_data.get(serial.upper())
    if data:
        return render_template('warranty_result.html', serial=serial, product=data['product'], years=data['years'])
    return f"<h3>No warranty info found for serial: {serial}</h3>"

@app.route('/warranty/<product>')
def product_warranty(product):
    matches = [s for s, d in warranty_data.items() if d['product'].lower() == product.lower()]
    if matches:
        return f"<h3>{product.capitalize()} warranty: {warranty_data[matches[0]]['years']} year(s)</h3>"
    return f"<h3>No warranty data found for {product}.</h3>"

if __name__ == '__main__':
    app.run(debug=True)

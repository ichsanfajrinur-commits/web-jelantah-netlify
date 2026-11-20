from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Penyimpanan data sementara
data_setoran = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nama = request.form.get('nama')
        no_hp = request.form.get('no_hp')
        alamat = request.form.get('alamat')
        liter = float(request.form.get('liter', 0))
        estimasi_harga = int(liter * 6000)

        data_setoran.append({
            'nama': nama,
            'no_hp': no_hp,
            'alamat': alamat,
            'liter': liter,
            'harga': estimasi_harga
        })
        return redirect(url_for('index'))

    return render_template('index.html', setoran=data_setoran)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
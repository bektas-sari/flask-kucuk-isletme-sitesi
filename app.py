from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'gizli-key'  # Güvenli bir key kullanın.
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Upload klasörü yoksa oluşturuluyor.
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Örnek veri depolaması (gerçekte veritabanı kullanmalısınız)
site_texts = {
    'hero_text': 'Hoşgeldiniz! En iyi hizmet burada.',
    'about_text': 'Hakkımızda bilgisi burada yer alır.',
    'products_text': 'Ürünlerimiz ile ilgili açıklamalar burada yer alır.'
}

# Yüklenen görsellerin listesi (gerçekte veritabanında tutulabilir)
uploaded_images = []

@app.route('/')
def index():
    return render_template('index.html', hero_text=site_texts['hero_text'], images=uploaded_images)

@app.route('/hakkimizda')
def hakkimizda():
    return render_template('hakkimizda.html', about_text=site_texts['about_text'])

@app.route('/urunlerimiz')
def urunlerimiz():
    return render_template('urunlerimiz.html', products_text=site_texts['products_text'], images=uploaded_images)

@app.route('/iletisim')
def iletisim():
    return render_template('iletisim.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        # Görsel yükleme
        if 'upload_image' in request.form:
            file = request.files.get('image')
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                uploaded_images.append(filename)
                flash('Görsel başarıyla yüklendi!', 'success')
            else:
                flash('Geçerli bir dosya seçilmedi ya da dosya türü uygun değil.', 'danger')
        # Hero yazısı güncelleme
        elif 'update_hero_text' in request.form:
            new_text = request.form.get('hero_text')
            site_texts['hero_text'] = new_text
            flash('Hero yazısı güncellendi!', 'success')
        # Hakkımızda yazısı güncelleme
        elif 'update_about_text' in request.form:
            new_text = request.form.get('about_text')
            site_texts['about_text'] = new_text
            flash('Hakkımızda yazısı güncellendi!', 'success')
        # Ürünler yazısı güncelleme
        elif 'update_products_text' in request.form:
            new_text = request.form.get('products_text')
            site_texts['products_text'] = new_text
            flash('Ürünler yazısı güncellendi!', 'success')
        # Görsel silme işlemi
        elif 'delete_image' in request.form:
            filename = request.form.get('delete_image')
            if filename in uploaded_images:
                uploaded_images.remove(filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                if os.path.exists(file_path):
                    os.remove(file_path)
                flash('Görsel silindi!', 'success')
        return redirect(url_for('admin'))
    return render_template('admin.html', site_texts=site_texts, images=uploaded_images)

if __name__ == '__main__':
    app.run(debug=True)

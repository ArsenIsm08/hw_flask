from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

# Статичные данные для категорий и товаров
categories_data = {
    'clothing': {'name': 'Одежда', 'description': 'Широкий выбор стильной одежды.'},
    'shoes': {'name': 'Обувь', 'description': 'Качественная обувь для всех сезонов.'},
}

products_data = {
    'item1': {'name': 'Товар 1', 'description': 'Описание товара 1.', 'price': 19.99},
    'item2': {'name': 'Товар 2', 'description': 'Описание товара 2.', 'price': 29.99},
}

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/category/<category>')
def category(category):
    category_data = categories_data.get(category)
    if not category_data:
        return render_template('404.html'), 404

    return render_template('category.html', category_data=category_data, products_data=products_data)

@app.route('/product/<product_name>')
def product(product_name):
    product_data = products_data.get(product_name)
    if not product_data:
        return render_template('404.html'), 404

    return render_template('product.html', product_data=product_data)

if __name__ == '__main__':
    app.run(debug=True)

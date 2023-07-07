import flask 
from flask import Flask, render_template, url_for
from MARKET.forms import Contact
from MARKET import ShopSite, db

from MARKET.models import Market

import json

from MARKET import ShopSite

@ShopSite.route('/')
def home():
    return render_template('home.html')

@ShopSite.route('/products')
def products():
    with open('product_db.json', 'r') as f:
        data = json.load(f)

    return render_template('products.html', data=data)
    


@ShopSite.route('/product/<product_id>')
def product_detailsID(product_id):
    with open('product_db.json', 'r') as f:
        data = json.load(f)

        def return_id(produit):
            return produit["ProductId"] == product_id 

        produit = list(filter(return_id, data))
        if produit:
            produit = produit[0]
            print(produit)
            return render_template('search_by_ID.html', product_id = product_id, produit=produit)
        else:
            return"ID not found"

@ShopSite.route('/product/search/by-name/<product_name>')
def product_detailsNAME(product_name):
    with open('product_db.json', 'r') as f:
        data = json.load(f)

    def return_NAME(produit):
        return produit["Name"] == product_name

    products = list(filter(return_NAME, data))
    
    if products:
        products = products[0]
        return render_template('search_by_name.html', products=products, product_name=product_name)
    else:
        return "Product not found"


@ShopSite.route('/search/by-category/<product_category>')
def search_by_category(product_category):
    with open('product_db.json', 'r') as f:
        data = json.load(f)

        def return_id(produits):
            return produits["Category"] == product_category

        produits = list(filter(return_id, data))
        return render_template('category.html', pcategory = product_category, produits=produits)


@ShopSite.route('/Contact', methods=['GET', 'POST'])
def Contacte():
    form = Contact()
    if form.validate_on_submit():
      
            Nom = form.Nom.data,
            Prenom = form.Prenom.data,
            Email = form.Email.data,
            Message = form.Message.data,
        

            Contacts = Market(Nom=Nom, Prenom=Prenom, Email= Email,  Message= Message)


            db.session.add(Contacts)
            db.session.commit()
       
    return render_template('Contact.html', form=form)
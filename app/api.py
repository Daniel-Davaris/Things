""" 
API is a file handling the product selling of the site

Written by (proudly at the time): Stephan Kashkarov
"""
import json
from requests import Session
from flask import Blueprint, request
# from keys import api_key, retailer_credentials

<<<<<<< HEAD
# from app import db, celery
=======
from app import app, db
>>>>>>> 14fad91ae290824b7ff1702b48becc3e44565d06
from app.models import (
    Item,
    Image,
    Category,
    Category_Item,
    Details,
    Brand,
    Brand_Item,
    Bullets,
    Orders
)

zinc = 'https://api.zinc.io/v1/'
http = Session()
http.auth = (api_key, '')
api = Blueprint('API', __name__)

@api.route('/getProduct/<productID>') # Send a get request to url.com/api/getProduct/*ID*HERE*
def getProduct(productID):
    """ 
    Get Product

    This api route takes a product ID from our database
    and returns the related product in json form.
    
    An example of the format can be seen below in a json schema:
    ```
    {
        'id': int,
        'product_id': int,
        'title': str,
        'desc': str,
        'details': List<str>,
        'bullets': str,
        'brand': str,
        'imgs': List<urls>, # 0th image is primary img
        'categories': List<str>,
        'old_price': int,
        'new_price': int,
    }
    ```
    
    """
    item    = Item.query.filter_by(id=productID).first_or_404()
    imgs    = sorted(Image.query.filter_by(item_id=item.id).all(), key=lambda x: x.is_primary)
    cats    = [Category.get(x.category_id) for x in Category_Item.query.filter_by(item_id=item.id).all()]
    brand   = [Brand.query.get(x.brand_id) for x in Brand_Item.query.filter_by(item_id=item.id).all()]
    details = Details.query.filter_by(item_id=item.id).all()
    bullets = Bullets.query.filter_by(item_id=item.id).all()

    return json.dumps({
        'id'        :item.id,
        'product_id':item.product_id,
        'title'     :item.title,
        'desc'      :item.desc,
        'details'   :details,
        'bullets'   :bullets,
        'brand'     :brand,
        'imgs'      :imgs,
        'categories':cats,
        'old_price' :item.old_price,
        'new_price' :item.new_price,
    })


@api.route('/addProduct', methods=['POST'])
def addProduct():
    """
    Add Product

    The add product route takes a ZINC api product ID
    and adds said product to the database with all connections
    nessesery

    Post example:
    ```
    {
        'retailer': 'aliexpress', # Only recommended for now
        'product_id': '32850545097' # some random bag
    }
    ```


    The code here is an antipattern
    """
    # try:
    data = request.get_json()
    data = http.get(
        f"{zinc}/products/{data['product_id']}",
        params=[('retailer', data['retailer'])],
        auth=(api_key, '')
    )
    data = data.json()
    item = Item(
        product_id=data['product_id'],
        title=data['title'],
        desc=data['product_description'],
        old_price=data['price'],
        new_price=(int(data['price'])*1.4),
    )
    categories = [
        Category(
            title=x
        )
        for x in data['categories']
    ]
    brand = Brand.query.filter_by(title=data['brand']).first()
    brand = brand if brand else Brand(title=data['brand'])
    db.session.add_all([
            item,
            brand,
            *categories,
            Brand_Item(
                item_id=item.id,
                brand_id=brand.id
            ),
            *[
                Bullet(
                    item_id=item.id,
                    text=x
                )
                for x in data['feature_bullets']
            ],
            *[
                Image(
                    item_id=item.id,
                    img_url=x,
                    is_primary=False if index != 0 else True,
                )
                for index, x in enumerate(data['images'])
            ],
            *[
                Category_Item(
                    item_id=item.id,
                    category_id=x.id
                )
                for x in categories
            ],
            *[
                Details(
                    item_id=item.id,
                    text=x
                )
                for x in data['details']
            ]
        ]
    )
    db.session.commit()
    return "Success", 200
    # except:
    return "Invalid json format", 400


@api.route('/makeOrder', methods=['POST'])
def makeOrder():
    """
    Make Order

    This route takes a list of product(s) and creates a
    zinc order 
    
    """
    try:
        data = request.get_json()
        data = http.post(
            f"{zinc}/orders",
            data=json.dumps({
                "retailer": "aliexpress",
                "products": data['products'],
                "max_price": 1000, # Change in future
                "shipping_address": data['shipping'],
                "billing_address": data['billing'],
                "shipping": data['shipping_params'],
                "is_gift": True,
                "payment_method": data['payment'],
                "retailer_credentials": retailer_credentials,
                "shipping_method": data['shipping_method']
            }),
            auth=(api_key)
        ).json()
        db.session.add(
            Orders(
                code=data['order'],
            )
        )
    except:
        return "Invalid json format", 500


@app.before_request
def check_orders():
    for order in Orders.query.filter_by(active=True).all():
        order.check_active()

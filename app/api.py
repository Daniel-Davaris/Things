from flask import Blueprint, request
from app import db
from app.models import (
    Item,
    Image,
    Category,
    Category_Item,
    Details,
    Brand,
    Brand_Item
)
import json
import requests
from keys import api_key

zinc = 'https://api.zinc.io/v1/'

api = Blueprint('API', __name__)

@api.route('/getProduct/<productID>') # Send a get request to url.com/api/getProduct/*ID*HERE*
def product(productID):
    """ 
    This api route takes a product ID and returns the related product in json form.
    
    An example of the format can be seen below in a json schema:

    {
        id: int,
        product_id: int,
        title: str,
        desc: str,
        details: List<str>,
        bullets: str,
        brand: str,
        imgs: List<urls>, # 0th image is primary img
        categories: List<str>,
        old_price: int,
        new_price: int,
    }
    
    """
    item    = Item.query.filter_by(product_id=productID).first_or_404()
    imgs    = sorted(Image.query.filter_by(item_id=item.id).all(), key=lambda x: x.is_primary)
    cats    = [Category.get(x.category_id) for x in Category_Item.query.filter_by(item_id=item.id).all()]
    brand   = [Brand.query.get(x.brand_id) for x in Brand_Item.query.filter_by(item_id=item.id)]
    details = Details.query.filter_by(item_id=item.id)

    return json.dumps({
        'id'        :item.id,
        'product_id':item.product_id,
        'title'     :item.title,
        'desc'      :item.desc,
        'details'   :details,
        'bullets'   :item.bullets,
        'brand'     :brand,
        'imgs'      :imgs,
        'categories':cats,
        'old_price' :item.old_price,
        'new_price' :item.new_price,
    })

@api.route('/addProduct', methods=['POST'])
def addProduct():
    try:
        data = request.get_json()

        data = requests.get(
            f"{zinc}/products/{data['product_id']}",
            params=[('retailer', retailer)],
            auth=(',client_token>', api_key)
        )
    except:
        return "Invalid input format", 500

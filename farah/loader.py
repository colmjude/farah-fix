from datetime import datetime

from application.models import Company, Product
from farah.logger import log_product_changes, log_new_product


schema_map = {
    "name": "title",
    "slug": "handle",
    "product_type": "product_type",
    "farah_product_id": "id",
    "rrp": "compare_at_price_max_gbp",
    "description": "body_html",
    "farah_published_date": "published_at"
}


def add_product(new_product):

    # handle dates that aren't in python date format
    new_product[schema_map['farah_published_date']] = datetime.fromisoformat(new_product[schema_map['farah_published_date']])

    product, is_new = Product.get_or_create(farah_product_id=new_product['id'])
    if is_new:
        farah = Company.query.get(1)
        product.company_id = farah.id
        product.update(
            name=new_product[schema_map['name']],
            slug=new_product[schema_map['slug']],
            product_type=new_product[schema_map['product_type']],
            farah_product_id=new_product[schema_map['farah_product_id']],
            rrp=new_product[schema_map['rrp']],
            description=new_product[schema_map['description']],
            farah_published_date=new_product[schema_map['farah_published_date']]
        )
        log_new_product({
            "date": datetime.today().strftime("%Y-%m-%d"),
            "product": product.id,
            "log": [
                {
                    "attr": "farah_product_id",
                    "from": product.farah_product_id
                }
            ]
        })
    else:
        print(product)
        changes = check_for_changes(product, new_product)
        if len(changes['log']):
            # update record
            updates = {change['attr']: change['to'] for change in changes['log']}
            product.update(**updates)
            # log changes
            log_product_changes(changes)


def check_for_changes(original, updated):
    changes = {
        "date": datetime.today().strftime("%Y-%m-%d"),
        "product": original.id,
        "log": []
    }

    # cast id to string for comparison
    if isinstance(updated['id'], int):
        updated['id'] = str(updated['id'])
        updated[schema_map['farah_published_date']] = updated[schema_map['farah_published_date']].date()

    # Iterate over the attributes of the original object
    for attr_name, attr_value in vars(original).items():
        # Skip attributes that are not user-defined
        if not attr_name.startswith("__") and not attr_name.startswith("_sa") and not callable(attr_value):
            if attr_name not in ['id', 'entry_date', 'company_id', 'end_date']:
                print(attr_name)
                original_value = getattr(original, attr_name, None)
                updated_value = updated.get(schema_map[attr_name], None)
                print(original_value, type(original_value), updated_value, type(updated_value))

                # Compare attribute values and record changes
                if original_value != updated_value:
                    changes["log"].append({
                        "attr": attr_name,
                        "from": original_value,
                        "to": updated_value
                    })

    return changes


def reconcile_products(products):
    # split between available and unavailable
        # need to check products still exist
    # for product in products:
    add_product(products[6618973732963])


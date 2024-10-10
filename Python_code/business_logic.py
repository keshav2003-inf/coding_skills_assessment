def process_orders(products, orders):
    for order in orders:
        for product_id, quantity in order.items():
            product = next((p for p in products if p.product_id == product_id), None)
            if product and product.stock >= quantity:
                product.stock -= quantity
                if product.stock < 10:
                    print(f"Alert: {product.name} needs restocking!")
            else:
                print(f"Error: {product.name} is out of stock!")
    return products


def restock_items(products, restock_list):
    for product_id, restock_qty in restock_list.items():
        product = next((p for p in products if p.product_id == product_id), None)
        if product:
            product.stock += restock_qty
    return products

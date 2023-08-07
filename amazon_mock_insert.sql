INSERT INTO customer(
    customer_id,
    first_name,
    last_name,
    address,
    billing_info
)VALUES(
    01,
    'Alex',
    'Lucchesi',
    '123 Main Street, Seattle, WA 98007',
    '4242-4242-4242-4242 623 08/07'
);

INSERT INTO brand(
    seller_id,
    brand_name,
    contact_number,
    address
)VALUES(
    01,
    'Coding Temple Trading Company',
    '773-555-4490',
    '222 W Ontario Street, Chicago, IL'
);

INSERT INTO inventory(
    upc,
    product_amount
)VALUES(
    01,
    20.00
);

INSERT INTO product(
    item_id,
    amount,
    prod_name,
    seller_id,
    upc
)VALUES(
    01,
    20.00,
    'Python 101',
    01,
    01
);
--
--
INSERT INTO orders(
    order_id,
    sub_total,
    total_cost,
    upc
)VALUES(
    01,
    40.00,
    43.50,
    01
);
--
INSERT INTO cart(
    cart_id,
    customer_id,
    order_id
)VALUES(
    01,
    01,
    01
);
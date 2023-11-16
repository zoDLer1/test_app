import requests


def test_oroduct_order_form_1():
    response = requests.post('http://127.0.0.1:5000/get_form', {
        'customer_name': 'name',
        'email': 'test@email.ru',
        'quantity': '2',
        'product_name': 'pr_name',
        'phone_number': '+7 999 232 45 34'
    })
    assert 'Product Order' == response.text


def test_oroduct_order_form_2():
    response = requests.post('http://127.0.0.1:5000/get_form', {
        'customer_name': 'name',
        'email': 'test@email.ru',
        'product_name': 'pr_name',
        'phone_number': '+7 999 232 45 34'
    })
    assert {
        'customer_name': 'TEXT',
        'email': 'EMAIL',
        'product_name': 'TEXT',
        'phone_number': 'PHONE'
    } == response.json()


def test_registation_form_1():
    response = requests.post('http://127.0.0.1:5000/get_form', {
        "user_name": "Alex",
        "email": "alex@text.se",
        "password": "234sdrflw",
        "created_at": "10/11/2023"
    })
    assert 'User Registration' == response.text


def test_registation_form_2():
    response = requests.post('http://127.0.0.1:5000/get_form', {
        "email": "alex@text.se",
        "password": "234sdrflw",
        "created_at": "10/11/2023"
    })
    assert {
        "email": "EMAIL",
        "password": "TEXT",
        "created_at": "DATE"
    } == response.json()

def test_feedback_form_1():
    response = requests.post('http://127.0.0.1:5000/get_form', {
        "user_name": "alex",
        "email": "alex@text.se",
        "phone_number": "+7 999 232 45 34",
        "feedback_message": "message...",
        "created_at": '2023/02/34'
    })
    assert 'Feedback Form' == response.text

def test_feedback_form_2():
    response = requests.post('http://127.0.0.1:5000/get_form', {
        "email": "alex@text.se",
        "user_name": "alex",
        "phone_number": "+7 999 232 45 34",
        "created_at": '2123/02/24'
    })
    assert {
        "email": "EMAIL",
        "phone_number": "PHONE",
        "user_name": "TEXT",
        "created_at": 'DATE'
    } == response.json()

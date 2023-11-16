from tinydb import TinyDB

db = TinyDB('database.json')

initilal_data = [
    {
        "name": "User Registration",
        "user_name": "text",
        "email": "email",
        "password": "text",
        "created_at": "date"
    },
    {
        "name": "Product Order",
        "customer_name": "text",
        "email": "email",
        "phone_number": "phone",
        "product_name": "text",
        "quantity": "text"
    },
    {
        "name": "Feedback Form",
        "user_name": "text",
        "email": "email",
        "phone_number": "phone",
        "feedback_message": "text",
        "created_at": "date"
    },
    {
        "name": "Survey Form",
        "participant_name": "text",
        "email": "email",
        "age": "text",
        "feedback": "text",
        "created_at": "date"
    }
]

def insert_data():
    if (not db.tables()):
        for data in initilal_data:
            db.insert(data)

insert_data()

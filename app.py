from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# ---------- Database Connection ----------
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # change if your MySQL username is different
        password="root",        # enter your MySQL password
        database="zomato"   # make sure this DB exists
    )

# ---------- Home Page ----------
@app.route('/')
def index():
    return render_template('home.html')

# ---------- Place Order ----------
@app.route('/place_order', methods=['POST'])
def place_order():
    try:
        data = request.get_json()
        address = data.get('address')
        cart = data.get('cart')

        if not cart or not address:
            return jsonify({"error": "Cart or address missing!"})

        conn = get_db_connection()
        cursor = conn.cursor()

        total_price = 0
        order_id = None

        for item in cart:
            item_name = item['name']
            quantity = item['quantity']
            price = item['price']
            total_price += price * quantity

            # insert each item as a new order
            cursor.execute("""
                INSERT INTO orders (user_id, item_id, quantity, delivery_address)
                VALUES (%s, %s, %s, %s)
            """, (1, 1, quantity, address))  # user_id=1, item_id=1 are placeholders

            order_id = cursor.lastrowid  # last inserted order_id

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({
            "message": f"Order placed successfully! Total = ₹{total_price}",
            "order_id": order_id
        })

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)})

# ---------- Run the App ----------
if __name__ == '__main__':
    app.run(debug=True)


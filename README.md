# 🍽️ ZomatoApp — SQL Mini Project

This project is a simple **food ordering system** built using **MySQL** and **Flask (Python)**.  
It demonstrates how to manage and store order details in a database.

---

## 🗄️ Database Details

**Database:** `zomato`

**Table:** `orders`
| Column | Type | Description |
|--------|------|-------------|
| order_id | INT | Primary Key |
| user_id | INT | Customer ID |
| item_id | INT | Linked item |
| quantity | INT | Quantity ordered |
| delivery_address | VARCHAR(255) | Address entered |
| order_date | TIMESTAMP | Order time |

---

## ⚙️ Technologies Used
- **Frontend:** HTML  
- **Backend:** Flask (Python)  
- **Database:** MySQL  

---

BASE zomato;
   USE zomato;

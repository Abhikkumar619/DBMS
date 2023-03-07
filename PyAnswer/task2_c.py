import cx_Oracle
from getpass import getpass
un=input("Enter userName: ")
pw=getpass()
def check_cashback(order_id):
    conStr= 'un/pw@localhost:1521/xe'
    conn = cx_Oracle.connect(conStr)
    cur = conn.cursor()

# validating the input
    if not order_id:
        print("Error: Please enter a valid Order ID.")
        return
    if not order_id.isnumeric():
        print("Error: Order ID must be a number.")
        return

#  PL/SQL function
    cur.execute("""
    BEGIN
        EXECUTE IMMEDIATE 'CREATE OR REPLACE FUNCTION get_order_price(p_order_id NUMBER) 
            RETURN NUMBER IS 
            v_order_price NUMBER;
            BEGIN 
                SELECT SUM(filling.gramprice*sandwichfilling.quantity)
                INTO v_order_price
                FROM ordertab
                JOIN sandwichfilling ON ordertab.sandwichid = sandwichfilling.sandwichid
                JOIN filling ON sandwichfilling.fillingid = filling.fillingid
                WHERE ordertab.orderid = p_order_id;
                RETURN v_order_price;
            END;';
    END;""")
    conn.commit()

# calling the PL/SQL stored function
    cur.execute("SELECT get_order_price(:order_id) FROM DUAL", {
                   "order_id": order_id})
    order_price = cur.fetchone()[0]

# Checking if the order price is above the threshold for cashback
    if order_price > 5:
        print("This order qualifies for cashback.")
    else:
        print("This order does not qualify for cashback.")


order_id = input("Enter the Order ID: ")
check_cashback(order_id)
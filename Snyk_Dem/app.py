from flask import Flask
from flask import jsonify
import os
import sqlite3

app = Flask(__name__)

def change(amount):
    # calculate the resultant change and store the result (res)
    res = []
    coins = [1, 5, 10, 25]  # value of pennies, nickels, dimes, quarters
    coin_lookup = {25: "quarters", 10: "dimes", 5: "nickels", 1: "pennies"}

    # divide the amount*100 (the amount in cents) by a coin value
    # record the number of coins that evenly divide and the remainder
    coin = coins.pop()
    num, rem = divmod(int(amount * 100), coin)
    # append the coin type and number of coins that had no remainder
    res.append({num: coin_lookup[coin]})

    # while there is still some remainder, continue adding coins to the result
    while rem > 0:
        coin = coins.pop()
        num, rem = divmod(rem, coin)
        if num:
            if coin in coin_lookup:
                res.append({num: coin_lookup[coin]})
    return res


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside great world")
    return 'Hello World! Welcome to the python_flask demo website.'


@app.route('/change/<dollar>/<cents>')
def changeroute(dollar, cents):
    print(f"Make Change for {dollar}.{cents}")
    amount = f"{dollar}.{cents}"
    result = change(float(amount))
    return jsonify(result)


# ------------------------------------------------------------------
# ❌ Insecure functions below (to trigger SonarCloud AI Code Assurance)
# ------------------------------------------------------------------

# 1) Command injection (unsafe)
def run_cmd(user_input):
    # BAD: directly passing user input to shell
    os.system("ping " + user_input)


# 2) SQL injection (unsafe)
def get_user(conn, name):
    # BAD: vulnerable string concatenation
    q = "SELECT * FROM users WHERE name = '" + name + "'"
    return conn.execute(q).fetchall()


# 3) Insecure deserialization / eval (unsafe)
def calc(expr):
    # BAD: executing arbitrary user input
    return eval(expr)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)

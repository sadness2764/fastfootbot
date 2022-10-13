import sqlite3

database = sqlite3.connect('fastfood.db')
cursor = database.cursor()


def create_users_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        telegram_id BIGINT NOT NULL UNIQUE,
        phone TEXT
    )
    ''')
    # INT - INTEGER -2147483648 до 2147483647
    # BIGINT -9223372036854775808 до 9223372036854775808
    # TINYINT -128 до 127


def create_cart_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS carts(
        cart_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER REFERENCES users(user_id) UNIQUE,
        total_products INTEGER DEFAULT 0,
        total_price DECIMAL(12, 2) DEFAULT 0
    )
    ''')


def create_cart_products_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cart_products(
        cart_product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        cart_id INTEGER REFERENCES carts(cart_id),
        product_name TEXT,
        quantity INTEGER NOT NULL,
        final_price DECIMAL(12, 2) NOT NULL,
        UNIQUE(cart_id, product_name)
    )
    ''')


def create_categories_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories(
        category_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name VARCHAR(30) NOT NULL UNIQUE
    )
    ''')


def insert_categories():
    cursor.execute('''
    INSERT OR IGNORE INTO categories(category_name) VALUES
    ('Лаваш'),
    ('Бургер'),
    ('Хот-дог'),
    ('Чизбургер')
    ''')


def create_products_table():
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS products(
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_id INTEGER NOT NULL,
            product_name VARCHAR(30) NOT NULL UNIQUE,
            price DECIMAL(12, 2) NOT NULL,
            description VARCHAR(150),
            image TEXT,
            FOREIGN KEY(category_id) REFERENCES categories(category_id)
        );
        '''
    )


def insert_products():
    cursor.execute('''
    INSERT INTO products(category_id, product_name, price, description, image)
    VALUES
    (1, 'Big Lavash', 45000, ' +998 (12) 345-67-89', 'media/lavash_1.jpg'),
    (1, 'Острый Lavash', 30000, ' +998 (12) 345-67-89', 'media/lavash_2.jpg'),
    (1, 'Mini Lavash', 25000, ' +998 (12) 345-67-89', 'media/lavash_3.jpg'),
    (2, 'Big Burger', 28000, ' +998 (12) 345-67-89', 'media/burger_1.jpg' ),
    (2, 'Black Burger', 30000, ' +998 (12) 345-67-89', 'media/burger_2.jpg' ),
    (2, 'Mini Burger', 20000, ' +998 (12) 345-67-89', 'media/burger_3.jpg' ),
    (3, 'Big Hot-Dog', 15000, ' +998 (12) 345-67-89', 'media/hotdog_1.jpg' ),
    (3, 'Hot-Dog Americano', 34000, ' +998 (12) 345-67-89', 'media/hotdog_2.jpg' ),
    (3, 'Mini Hot-Dog', 20000, ' +998 (12) 345-67-89', 'media/hotdog_3.jpg' ),
    (4, 'Cheeseburger Classic', 28000, ' +998 (12) 345-67-89', 'media/chburger_1.jpg' ),
    (4, 'Cheeseburger Mexico', 40000, ' +998 (12) 345-67-89', 'media/chburger_2.jpg' ),
    (4, 'Mini Cheeseburger', 21000, ' +998 (12) 345-67-89', 'media/chburger_3.jpg' )
    ''')


def create_orders_table():
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS orders( 
            order_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            telegram_id TEXT, 
            cart_id INTEGER REFERENCES carts(cart_id), 
            text TEXT, 
            price TEXT, 
            status TEXT NOT NULL DEFAULT 'nready' 
        ) 
    ''')


create_users_table()
create_cart_table()
create_cart_products_table()
create_categories_table()
insert_categories()
create_products_table()
insert_products()
create_orders_table()

database.commit()
database.close()
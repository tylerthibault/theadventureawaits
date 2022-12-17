SELECT * FROM bakedblessingsdb.users;
SELECT * FROM bakedblessingsdb.categories;
SELECT * FROM bakedblessingsdb.products;

INSERT INTO users (first_name, last_name, email, pw, level) 
VALUES ("tyler", "tbo", "tt@email.com", "$2b$12$5lN2BDNHzJXKUDzUPuXk1O4ZAW/.pmQUaYq0tgNdx1TIXUoLOkeUG", 2);

INSERT INTO categories (id, name) VALUES (5, "Other");
INSERT INTO categories (id, name) VALUES (6, "Bread");
INSERT INTO categories (id, name) VALUES (7, "Sweets");

INSERT INTO products (name, size, price, is_available, qty, category_id, description) 
VALUES ("8\" Loaf", 8, 7, 1, 1, 6, "Lorem ipsum dolor sit amet consectetur adipisicing elit. Sequi, temporibus. Corrupti facilis quam ratione quia esse sint minus corporis. Quidem, vero? Voluptatem nesciunt non sint.");

INSERT INTO products (name, size, price, is_available, qty, category_id, description) 
VALUES ("6\" Loaf", 6, 5, 1, 1, 6, "A great loaf of sourdough bread for the someone to eat all to themselves.");

INSERT INTO products (name, size, price, is_available, qty, category_id, description) 
VALUES ("English Muffins (6 pack)", 8, 6, 1, 1, 6, "Nothing better than starting a morning with some coffee and a homemade sourdough English Muffin!");

INSERT INTO products (name, size, price, is_available, qty, category_id, description) 
VALUES ("English Muffins (12 pack)", 8, 12, 1, 1, 6, "Nothing better than starting a morning with some coffee and a homemade sourdough English Muffin!");

INSERT INTO products (name, size, price, is_available, qty, category_id, description) 
VALUES ("Pizza Dough (Thick Crust)", 8, 8, 1, 1, 6, "The dough makes a 14\" thick crust homemade pizza without all the hassle.");

INSERT INTO products (name, size, price, is_available, qty, category_id, description) 
VALUES ("Pizza Dough (Thin Crust)", 8, 5, 1, 1, 6, "The dough makes a 12\" thin crust homemade pizza without all the hassle.");

INSERT INTO products (name, size, price, is_available, qty, category_id, description) 
VALUES ("Cinnamon Rolls (Small)", 8, 12, 1, 1, 7, "Lorem ipsum dolor sit amet consectetur adipisicing elit. Sequi, temporibus. Corrupti facilis quam ratione quia esse sint minus corporis. Quidem, vero? Voluptatem nesciunt non sint.");

INSERT INTO products (name, size, price, is_available, qty, category_id, description) 
VALUES ("Cinnamon Rolls (Medium)", 8, 12, 1, 1, 7, "Lorem ipsum dolor sit amet consectetur adipisicing elit. Sequi, temporibus. Corrupti facilis quam ratione quia esse sint minus corporis. Quidem, vero? Voluptatem nesciunt non sint.");


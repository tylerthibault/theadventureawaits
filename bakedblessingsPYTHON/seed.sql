SELECT * FROM bakedblessingsdb.users;
SELECT * FROM bakedblessingsdb.categories;
SELECT * FROM bakedblessingsdb.products;

INSERT INTO users (first_name, last_name, email, pw, level) 
VALUES ("tyler", "tbo", "tt@email.com", "$2b$12$5lN2BDNHzJXKUDzUPuXk1O4ZAW/.pmQUaYq0tgNdx1TIXUoLOkeUG", 1);

INSERT INTO users (first_name, last_name, email, pw, level) 
VALUES ("kendal", "tbo", "kt@email.com", "$2b$12$5lN2BDNHzJXKUDzUPuXk1O4ZAW/.pmQUaYq0tgNdx1TIXUoLOkeUG", 2);

INSERT INTO config (max_daily_orders) VALUES (4);

INSERT INTO categories (id, name) VALUES (5, "Other");
INSERT INTO categories (id, name) VALUES (6, "Bread");
INSERT INTO categories (id, name) VALUES (7, "Sweets");

INSERT INTO products (name, size, price, qty, is_available, category_id, description, img_url) 
VALUES ("8\" Loaf", 8, 7, 1, 1, 6, "Lorem ipsum dolor sit amet consectetur adipisicing elit. Sequi, temporibus. Corrupti facilis quam ratione quia esse sint minus corporis. Quidem, vero? Voluptatem nesciunt non sint.", "https://i.ibb.co/hcxD4v1/20cd655122af.png");

INSERT INTO products (name, size, price, qty, is_available, category_id, description, img_url) 
VALUES ("6\" Loaf", 6, 5, 1, 1, 6, "A great loaf of sourdough bread for the someone to eat all to themselves.", "https://i.ibb.co/vXxRpXz/cf4dbc0eeae4.png");

INSERT INTO products (name, size, price, qty, is_available, category_id, description, img_url) 
VALUES ("English Muffins (6 pack)", 4, 6, 6, 1, 6, "Nothing better than starting a morning with some coffee and a homemade sourdough English Muffin!", "https://i.ibb.co/2jFXzfq/ea002102e2ed.jpg");

INSERT INTO products (name, size, price, qty, is_available, category_id, description, img_url) 
VALUES ("English Muffins (12 pack)", 4, 12, 12, 1, 6, "Nothing better than starting a morning with some coffee and a homemade sourdough English Muffin!", "https://i.ibb.co/fXmRt0V/8aa5a0af7200.jpg");

INSERT INTO products (name, size, price, qty, is_available, category_id, description, img_url) 
VALUES ("Pizza Dough (Thick Crust)", 14, 8, 1, 1, 6, "The dough makes a 14\" thick crust homemade pizza without all the hassle.", "https://i.ibb.co/MRJZPvs/a9b6dd9cb7e5.jpg");

INSERT INTO products (name, size, price, qty, is_available, category_id, description, img_url) 
VALUES ("Pizza Dough (Thin Crust)", 14, 5, 1, 1, 6, "The dough makes a 12\" thin crust homemade pizza without all the hassle.", "https://i.ibb.co/MRJZPvs/a9b6dd9cb7e5.jpg");

INSERT INTO products (name, size, price, qty, is_available, category_id, description, img_url) 
VALUES ("Cinnamon Rolls (Small)", 4, 12, 8, 1, 7, "Lorem ipsum dolor sit amet consectetur adipisicing elit. Sequi, temporibus. Corrupti facilis quam ratione quia esse sint minus corporis. Quidem, vero? Voluptatem nesciunt non sint.", "https://i.ibb.co/gFn3wSF/ae7ceab64d0e.jpg");

INSERT INTO products (name, size, price, qty, is_available, category_id, description, img_url) 
VALUES ("Cinnamon Rolls (Medium)", 6, 12, 4, 1, 7, "Lorem ipsum dolor sit amet consectetur adipisicing elit. Sequi, temporibus. Corrupti facilis quam ratione quia esse sint minus corporis. Quidem, vero? Voluptatem nesciunt non sint.", "https://i.ibb.co/gFn3wSF/ae7ceab64d0e.jpg");


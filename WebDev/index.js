const { stringify } = require('querystring');

const sqlite3 = require('sqlite3').verbose();

let db = new sqlite3.Database('./SQLite/website.db', (err) => {
    if (err) {
      console.error(err.message);
    }
    console.log('Connected to the database.');
  });

const createTableSql = `
  CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      username TEXT NOT NULL,
      email TEXT UNIQUE NOT NULL,
      password TEXT NOT NULL
  )`;
db.run(createTableSql, (err) => {
    if (err) {
        return console.error('Error creating table:', err.message);
    }
    console.log('Table created successfully');
});

const InsertQueries = ["INSERT INTO users (username, email, password) VALUES ('John1', 'john@johnston.com', 'johnPass')", 
    "INSERT OR IGNORE INTO users (username, email, password) VALUES ('John1', 'john@johnston.com', 'johnPass')",
    "INSERT OR IGNORE INTO users (username, email, password) VALUES ('John2', 'john2@johnston.com', 'notPass')",
    "INSERT OR IGNORE INTO users (username, email, password) VALUES ('John3', 'john3@johnston.com', 'NotjohnPass')",
    "INSERT OR IGNORE INTO users (username, email, password) VALUES ('John4', 'john4@johnston.com', 'johnBlock')",
    "INSERT OR IGNORE INTO users (username, email, password) VALUES ('John5', 'john5@johnston.com', 'johnPass1')",
    "INSERT OR IGNORE INTO users (username, email, password) VALUES ('John6', 'john6@johnston.com', 'johnPass2')",
    "INSERT OR IGNORE INTO users (username, email, password) VALUES ('John7', 'john7@johnston.com', 'johnPass3')",
    "INSERT OR IGNORE INTO users (username, email, password) VALUES ('John8', 'john8@johnston.com', 'johnPass4')",
    "INSERT OR IGNORE INTO users (username, email, password) VALUES ('John9', 'john9@johnston.com', 'johnPass5')",
    "INSERT OR IGNORE INTO users (username, email, password) VALUES ('Jerry', 'jerry@johnston.com', 'jerryPass')",
    "INSERT OR IGNORE INTO users (username, email, password) VALUES ('Mary', 'mary@johnston.com', 'maryPass')",
    "INSERT OR IGNORE INTO users (username, email, password) VALUES ('Sue', 'gary@johnston.com', 'garyPass')",
];
for (i in InsertQueries) {
    db.run(InsertQueries[i], (err) => {
        if (err) {
            console.log(InsertQueries[i]);
            return console.error('Error inserting into table:', err.message);
        }
        console.log('Inserted ' + stringify(InsertQueries[i])+ ' successfully');
    });
}

const SelectCommand = "SELECT * FROM users";

db.all(SelectCommand, [], (err, rows) => {
    if (err) {
      throw err;
    }
    rows.forEach((row) => {
      console.log(row);
    });
  });

db.close((err) => {
    if (err) {
      console.error(err.message);
    }
    console.log('Close the database connection.');
  });
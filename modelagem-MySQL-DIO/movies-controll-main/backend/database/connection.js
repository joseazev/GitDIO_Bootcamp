const mysql = require('mysql');

const Connection = mysql.createConnection({
    host: 'localhost',
    port: 3306,
    user: 'root',
    password: 'root',
    database: 'movies_controll'
})

module.exports = Connection;

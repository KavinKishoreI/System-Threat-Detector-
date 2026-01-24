import mysql from "mysql2/promise";
import dotenv from "dotenv";

dotenv.config();

let connection;

try {
  connection = await mysql.createConnection({
    host: "localhost",
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: "systemthreat",
  });

  console.log("Connected to MySQL database as id " + connection.threadId);
} catch (err) {
  console.error("Error connecting to the database:", err.message);
  process.exit(1);
}

export default connection;

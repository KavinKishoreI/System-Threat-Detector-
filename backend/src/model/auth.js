import connection from "../dbConfig/config.js";
import bcrypt from "bcrypt";
import jwt from "jsonwebtoken";

const addUser = async (user_name, password) => {
  try {
    const hashedPassword = await bcrypt.hash(password, 10);

    const query = `
      INSERT INTO USERS (user_name, password)
      VALUES (?, ?);
    `;

    await connection.query(query, [user_name, hashedPassword]);

    return { message: "User added successfully", status: 201 };
  } catch (error) {
    if (error.code === "ER_DUP_ENTRY") {
      return { message: "User already exists", status: 409 };
    }

    console.error("Error adding user:", error);
    return { message: "Database Error", status: 500 };
  }
};

const loginUser = async (user_name, password) => {
  try {
    const query = `
      SELECT user_id, password
      FROM USERS
      WHERE user_name = ?;
    `;

    const [rows] = await connection.query(query, [user_name]);

    if (rows.length === 0) {
      return { message: "User not found", status: 401 };
    }

    const user = rows[0];
    const passwordMatch = await bcrypt.compare(password, user.password);

    if (!passwordMatch) {
      return { message: "Invalid credentials", status: 401 };
    }

    const token = jwt.sign({ user_name: user_name }, process.env.JWT_SECRET);

    return { token, status: 200 };
  } catch (error) {
    console.error("Error authenticating user:", error);
    return { message: "Database Error", status: 500 };
  }
};

const searchUser = async (user_id) => {
  const option = `SELECT user_name from users where user_id = ?`;
  const [getUser] = await connection.query(option, [user_id]);
  console.log(getUser);
  return { username: "dummy" };
};

export { addUser, loginUser, searchUser };

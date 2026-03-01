import { addUser, loginUser, searchUser } from "../model/auth.js";
import jwt, { decode } from "jsonwebtoken";

function isAlphaNumeric(str) {
  const alphaNumeric = /^[A-Za-z0-9_]+$/;
  return alphaNumeric.test(str);
}

const register = async (request, response) => {
  const { user_name, password } = request.body;

  if (!isAlphaNumeric(user_name)) {
    return response.status(422).send({
      message: "Cannot use special characters other than _",
    });
  }
  if (user_name.length < 8 || password.length < 8) {
    return response.status(422).json({
      message: "Username or password cannot have less than 8 characters ",
    });
  } else {
    // try to  register user
    const result = await addUser(user_name, password);
    return response.status(result.status).json(result);
  }
};

const login = async (request, response) => {
  const { user_name, password } = request.body;

  if (!isAlphaNumeric(user_name)) {
    return response.status(422).json({
      message: "username cannot have special characters other than _ ",
    });
  } else if (user_name.length < 8 || password.length < 8) {
    return response.status(422).json({
      message: "Username or password cannot have less than 8 characters ",
    });
  } else {
    // Pasword and username validated now authenticate
    const result = await loginUser(user_name, password);
    return response.status(result.status).send(result);
  }
};
// Token authentication middleware
const authToken = async (request, response, next) => {
  const authHeader = request.headers["authorization"];
  if (authHeader === undefined) {
    return response.status(401).send({ message: "Missing Auth token" });
  }
  const token = authHeader.split(" ")[1];

  if (token === undefined) {
    return response.status(403).send({ message: "Missing Auth token" });
  }
  jwt.verify(token, process.env.JWT_SECRET, (err, decodedUser) => {
    if (err) {
      return response
        .status(403)
        .json({ message: "Invalid or expired token." });
    }

    request.body.userName = decodedUser;
    next();
  });
};

const apiAuth = async (request, response) => {
  const authHeader = request.headers["authorization"];
  const authToken = authHeader.split(" ")[1];
  try {
    const user = jwt.verify(
      authToken,
      process.env.JWT_SECRET,
      async (err, decodedUser) => {
        if (err) {
          return response
            .status(403)
            .json({ message: "Invalid or expired token." });
        }
        console.log(decodedUser);

        response.status(200).send({ user_name: decodedUser.user_name });
      },
    );
  } catch (e) {
    console.log("Invalid token ", authToken);
    console.log(e);
    response.status(501).send({ message: "Server error" });
  }
};

export { register, login, authToken, apiAuth };

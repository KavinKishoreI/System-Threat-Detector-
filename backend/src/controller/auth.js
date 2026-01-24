import { addUser, loginUser } from "../model/auth.js";
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
    const result = await loginUser(user_name, password);
    return response.status(result.status).json(result);
  }
};

export { register, login };

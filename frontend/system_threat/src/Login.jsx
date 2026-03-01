import { useState } from "react";
import { useNavigate } from "react-router-dom";
import Cookies from "js-cookie";

const Login = (history) => {
  const navigate = useNavigate();

  const [user_name, setuserName] = useState("");
  const [password, setPassword] = useState("");
  const [loginStatus, setLoginStatus] = useState("");

  const onSubmit = async (event) => {
    event.preventDefault();
    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify({
        user_name,
        password,
      }),
    };
    try {
      const authResult = await fetch("http://localhost:3000/login", options);
      const result = await authResult.json();
      if (authResult.ok === false) setLoginStatus("Invalid Credentials");
      else {
        setLoginStatus("Login Successful");
        Cookies.set("token", result.token);
        setLoginStatus("Login Successful");
        setTimeout(() => navigate("/"), 1000);
        console.log("JWT stored in cookie");
      }
    } catch {
      setLoginStatus("Server Error TRY AGAIN LATER");
    }
  };

  return (
    <>
      <form onSubmit={onSubmit}>
        <label htmlFor="user_name">USERNAME</label>
        <input
          type="text"
          id="user_name"
          value={user_name}
          onChange={(event) => setuserName(event.target.value)}
        />{" "}
        <br />
        <label htmlFor="password">PASSWORD</label>
        <input
          type="password"
          id="password"
          value={password}
          onChange={(event) => setPassword(event.target.value)}
        />
        <button className="sign-up-button"> Submit </button>
        <p>{loginStatus}</p>
      </form>
    </>
  );
};

export default Login;

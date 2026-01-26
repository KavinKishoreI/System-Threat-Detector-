import { useState } from "react";

const Register = () => {
  const [user_name, setuserName] = useState("");
  const [password, setPassword] = useState("");
  const [loginStatus, setLoginStatus] = useState("");
  console.log(user_name);
  console.log(password);

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
      const authResult = await fetch("http://localhost:3000/register", options);
      const result = await authResult.json();
      if (authResult.ok === false) setLoginStatus(result.message);
      else setLoginStatus("User Created!");
      console.log(result);
    } catch (e) {
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
        <button className="sign-up-button"> Register </button>
        <p>{loginStatus}</p>
      </form>
    </>
  );
};

export default Register;

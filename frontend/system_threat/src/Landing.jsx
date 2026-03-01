import "./Landing.css";
import logo from "./assets/logo.png";
import { Link } from "react-router-dom";
import Working from "./working.jsx";
import Cookies from "js-cookie";
import { useEffect, useState } from "react";

const Landing = () => {
  const [username, setUserName] = useState(undefined);
  useEffect(() => {
    const token = Cookies.get("token");
    if (token === undefined) return;
    const apiAuth = async () => {
      const option = {
        method: "GET",
        headers: {
          Authorization: `Bearer ${token}`,
        },
      };
      const checkToken = await fetch(
        "http://localhost:3000/tokenAuth/",
        option,
      );
      const authResult = await checkToken.json();
      setUserName(authResult.user_name);
      console.log(authResult);
    };
    apiAuth();
  }, []);

  return (
    <>
      <div className="header">
        <img className="logo" src={logo} alt="Logo" />
        <h1 className="heading">
          {" "}
          AI that Loves Malware
          <br />
        </h1>
        {username === undefined ? (
          <div className="login-signup">
            <Link to="/register/">
              <button className="sign-up-button"> Sign up </button>
            </Link>
            <Link to="/login/">
              <button className="login-button">Login</button>
            </Link>
          </div>
        ) : (
          <div>
            <h2> Hi {username}! </h2>
          </div>
        )}
      </div>
      <div className="heros">
        <div className="heros-left">
          <h1>
            Hunt it Before <br />
            <span className="scary">It Gets you!</span>
            <br />
            Sign up Now
          </h1>
          <a href="#learn-more" className="learn-more">
            Learn More
          </a>
          <br />
          <Link to="/user/">
            <button className="sign-up-button"> Get Started! </button>
          </Link>
        </div>
        <div className="heros-right"></div>
      </div>
      <Working />
    </>
  );
};

export default Landing;

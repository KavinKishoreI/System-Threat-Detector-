import "./Landing.css";
import logo from "./assets/logo.png";
import { Link } from "react-router-dom";

const Landing = () => (
  <>
    <div className="header">
      <img className="logo" src={logo} alt="Logo" />
      <h1 className="heading">
        {" "}
        Our AI Loves Malware
        <br />
      </h1>
      <div className="login-signup">
        <Link to="/register/">
          <button className="sign-up-button"> Sign up </button>
        </Link>

        <Link to="/login/">
          <button className="login-button">Login</button>
        </Link>
      </div>
    </div>
    <div className="heros">
      <div className="heros-left">
        <h1>
          Hunt it Before <br />
          <span className="scary">It Gets you!</span>
          <br />
          Just a few Clicks!
        </h1>
        <a> Learn More! </a>
      </div>
      <div className="heros-right"></div>
    </div>
  </>
);

export default Landing;

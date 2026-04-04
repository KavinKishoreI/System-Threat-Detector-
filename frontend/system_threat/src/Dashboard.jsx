import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import ThreatForm from "./Form.jsx";
import Cookies from "js-cookie";
const Dashboard = () => {
  // Check for token and validate it
  useEffect(() => {
    const token = Cookies.get("token");
    if (!token) {
      navigator("/login");
    } else {
      fetch("http://localhost:3000/tokenAuth/", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
      })
        .then((res) => {
          if (res.ok) {
            return res.json();
          } else {
            navigator("/login");
          }
        })
        .then((data) => {
          setUserName(data.username);
        });
    }
  }, []);
  const navigator = useNavigate();
  const [username, setUserName] = useState(undefined);
  return <ThreatForm />;
};

export default Dashboard;

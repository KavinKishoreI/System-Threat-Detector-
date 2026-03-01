import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import ThreatForm from "./Form.jsx";
const Dashboard = () => {
  const navigator = useNavigate();
  const [username, setUserName] = useState(undefined);
  return <ThreatForm />;
};

export default Dashboard;

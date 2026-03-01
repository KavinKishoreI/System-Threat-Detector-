import React, { useState } from "react";

const ThreatForm = () => {
  const [formData, setFormData] = useState({});

  const handleChange = (e) => {
    const { name, value, type } = e.target;

    let parsedValue = value;

    // Convert types properly
    if (value === "") parsedValue = null;
    else if (type === "number") parsedValue = Number(value);
    else if (value === "true") parsedValue = true;
    else if (value === "false") parsedValue = false;

    setFormData((prev) => ({
      ...prev,
      [name]: parsedValue,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await fetch("http://localhost:8000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      const data = await res.json();
      console.log("Prediction:", data);
    } catch (err) {
      console.error("Error:", err);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>Processor Core Count</label>
      <input
        type="number"
        name="ProcessorCoreCount"
        min={1}
        max={64}
        onChange={handleChange}
      />

      <label>Processor</label>
      <select name="Processor" onChange={handleChange}>
        <option value="">Select</option>
        {["x86", "x64", "arm64"].map((v) => (
          <option key={v} value={v}>
            {v}
          </option>
        ))}
      </select>

      <label>OS Build Number</label>
      <input
        type="number"
        name="OSBuildNumber"
        min={7601}
        max={17763}
        onChange={handleChange}
      />

      <label>Signature Age (Days)</label>
      <input
        type="number"
        name="SignatureAgeDays"
        min={6}
        max={840}
        onChange={handleChange}
      />

      <label>Firewall Enabled</label>
      <select name="FirewallEnabled" onChange={handleChange}>
        <option value="">Select</option>
        <option value="true">True</option>
        <option value="false">False</option>
      </select>

      <button type="submit">Submit</button>
    </form>
  );
};

export default ThreatForm;

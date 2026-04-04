import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import Cookies from "js-cookie";
import "./Form.css";

// Dropdown options
const OPTIONS = {
  Processor: ["x86", "x64", "arm64"],
  SKUEditionName: [
    "Home",
    "Pro",
    "Cloud",
    "Education",
    "Enterprise LTSB",
    "Enterprise",
    "Invalid",
    "Server",
  ],
  OSEdition: [
    "Core",
    "Professional",
    "CoreSingleLanguage",
    "ProfessionalN",
    "ProfessionalEducation",
    "CoreCountrySpecific",
    "Cloud",
    "Education",
    "EnterpriseS",
    "Enterprise",
    "Other",
  ],
  ChassisType: [
    "Notebook",
    "AllinOne",
    "Desktop",
    "Other",
    "Laptop",
    "Portable",
    "Convertible",
    "LowProfileDesktop",
    "Detachable",
    "MiniTower",
  ],
  AppVersion: [
    "4.18.1807.18075",
    "4.18.1806.18062",
    "4.16.17656.18052",
    "4.14.17639.18041",
    "4.12.16299.15",
    "Other",
  ],
  AntivirusConfigID: [
    "53447.0",
    "46413.0",
    "41571.0",
    "23657.0",
    "47238.0",
    "7945.0",
    "62773.0",
    "49480.0",
    "51954.0",
    "46669.0",
    "Other",
    "nan",
  ],
  OSBranch: [
    "rs1_release",
    "rs4_release",
    "rs2_release",
    "rs3_release",
    "rs3_release_svc_escrow",
    "th2_release",
    "th1_st1",
    "th2_release_sec",
    "rs3_release_svc_escrow_im",
    "th1",
    "rs5_release",
    "rs_prerelease_flt",
    "rs_prerelease",
  ],
};

// Numeric field ranges
const RANGES = {
  ProcessorCoreCount: { min: 1, max: 64 },
  OSBuildNumber: { min: 7601, max: 17763 },
  SignatureAgeDays: { min: 0, max: 840 },
  OSUpdateAgeDays: { min: 0, max: 1175 },
};

// Required fields
const REQUIRED_FIELDS = [
  "pcName",
  "ProcessorCoreCount",
  "Processor",
  "OSBuildNumber",
  "IsSystemProtected",
  "FirewallEnabled",
  "SignatureAgeDays",
  "OSUpdateAgeDays",
];

// Field help text
const FIELD_HELP = {
  ProcessorCoreCount: "How many cores in your CPU? (usually 2, 4, or 8)",
  Processor: "Your system type (most modern PCs use x64)",
  SKUEditionName: "Which Windows edition? (Home, Pro, etc.)",
  OSEdition: "Your Windows version type",
  OSBuildNumber: "Find in Settings > About (e.g., 17763)",
  ChassisType: "Laptop, Desktop, or other?",
  AppVersion: "Your Windows Defender version",
  IsSystemProtected: "Is real-time protection on?",
  IsPassiveModeEnabled: "Running in background-only mode? (usually No)",
  AntivirusConfigID: "Your antivirus profile ID",
  FirewallEnabled: "Is your firewall turned on?",
  OSBranch: "Your Windows update type",
  AV_Imbalance: "Did you experience any antivirus configuration issues?",
  SignatureAgeDays: "How old are your virus definitions?",
  OSUpdateAgeDays: "How long since your last Windows update?",
};

// Get risk level based on probability
const getRiskLevel = (probability) => {
  if (probability < 0.5) {
    return { level: "Safe", className: "risk-safe" };
  } else {
    return { level: "Vulnerable", className: "risk-vulnerable" };
  }
};

// Reusable form field component
const FormField = ({
  label,
  name,
  type = "text",
  options,
  required,
  helpText,
  touched,
  formData,
  onChange,
  onBlur,
  placeholder,
  min,
  max,
}) => {
  const isRequired = required || REQUIRED_FIELDS.includes(name);
  const isEmpty =
    formData[name] === null ||
    formData[name] === undefined ||
    formData[name] === "";
  const showError = isRequired && touched && isEmpty;

  return (
    <div className="form-group">
      <label htmlFor={name}>
        {label}
        {isRequired && <span className="required"> *</span>}
        {helpText && (
          <span className="help-tooltip" title={helpText}>
            <span className="help-icon">?</span>
          </span>
        )}
      </label>

      {type === "select" ? (
        <select
          id={name}
          name={name}
          onChange={onChange}
          onBlur={() => onBlur(name)}
          className={showError ? "error" : ""}
        >
          <option value="">Select</option>
          {options &&
            options.map((v) => (
              <option key={v} value={v}>
                {v}
              </option>
            ))}
        </select>
      ) : type === "boolean" ? (
        <select
          id={name}
          name={name}
          onChange={onChange}
          onBlur={() => onBlur(name)}
          className={showError ? "error" : ""}
        >
          <option value="">Select</option>
          <option value="true">Yes</option>
          <option value="false">No</option>
        </select>
      ) : (
        <input
          type={type}
          id={name}
          name={name}
          min={min}
          max={max}
          onChange={onChange}
          onBlur={() => onBlur(name)}
          placeholder={placeholder}
          className={showError ? "error" : ""}
        />
      )}

      {showError && <span className="field-error">This field is required</span>}
    </div>
  );
};

const ThreatForm = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({});
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [touched, setTouched] = useState({});

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

    // Clear error when user fills a required field
    if (touched[name] && parsedValue !== null && parsedValue !== "") {
      setError(null);
    }
  };

  const handleBlur = (name) => {
    setTouched((prev) => ({ ...prev, [name]: true }));
  };

  const validateForm = () => {
    const missing = REQUIRED_FIELDS.filter(
      (field) =>
        formData[field] === null ||
        formData[field] === undefined ||
        formData[field] === "",
    );

    if (missing.length > 0) {
      const newTouched = {};
      missing.forEach((field) => (newTouched[field] = true));
      setTouched(newTouched);
      setError(`Please fill in all required fields marked with *`);
      return false;
    }
    return true;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!validateForm()) {
      return;
    }

    setLoading(true);
    setError(null);
    setPrediction(null);

    try {
      // Derive FirewallWithoutProtection from other fields
      const dataToSend = {
        ...formData,
        FirewallWithoutProtection:
          formData.FirewallEnabled && !formData.IsSystemProtected,
      };

      const res = await fetch("http://localhost:3000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${Cookies.get("token")}`,
        },
        body: JSON.stringify(dataToSend),
      });

      const data = await res.json();
      console.log("Prediction:", data);
      setPrediction(data);
    } catch (err) {
      console.error("Error:", err);
      setError("Failed to get prediction. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="form-container">
      <h2>System Threat Analyzer</h2>

      <form onSubmit={handleSubmit} className="threat-form">
        {/* System Information Section */}
        <div className="form-section">
          <h3>Your Computer</h3>
        </div>

        <FormField
          label="Computer Name"
          name="pcName"
          type="text"
          placeholder="Enter computer name"
          helpText="A name to identify this computer"
          touched={touched.pcName}
          formData={formData}
          onChange={handleChange}
          onBlur={handleBlur}
        />

        <FormField
          label="CPU Cores"
          name="ProcessorCoreCount"
          type="number"
          min={RANGES.ProcessorCoreCount.min}
          max={RANGES.ProcessorCoreCount.max}
          placeholder="1 - 64"
          helpText={FIELD_HELP.ProcessorCoreCount}
          required
          touched={touched.ProcessorCoreCount}
          formData={formData}
          onChange={handleChange}
          onBlur={handleBlur}
        />

        <FormField
          label="System Type"
          name="Processor"
          type="select"
          options={OPTIONS.Processor}
          helpText={FIELD_HELP.Processor}
          required
          touched={touched.Processor}
          formData={formData}
          onChange={handleChange}
          onBlur={handleBlur}
        />

        <FormField
          label="Windows Edition"
          name="SKUEditionName"
          type="select"
          options={OPTIONS.SKUEditionName}
          helpText={FIELD_HELP.SKUEditionName}
          touched={touched.SKUEditionName}
          formData={formData}
          onChange={handleChange}
          onBlur={handleBlur}
        />

        <FormField
          label="Windows Version"
          name="OSEdition"
          type="select"
          options={OPTIONS.OSEdition}
          touched={touched.OSEdition}
          helpText={FIELD_HELP.OSEdition}
          formData={formData}
          onChange={handleChange}
          onBlur={handleBlur}
        />

        <FormField
          label="Build Number"
          name="OSBuildNumber"
          type="number"
          min={RANGES.OSBuildNumber.min}
          max={RANGES.OSBuildNumber.max}
          placeholder="7601 - 17763"
          helpText={FIELD_HELP.OSBuildNumber}
          required
          touched={touched.OSBuildNumber}
          formData={formData}
          onChange={handleChange}
          onBlur={handleBlur}
        />

        <FormField
          label="Device Type"
          name="ChassisType"
          type="select"
          options={OPTIONS.ChassisType}
          helpText={FIELD_HELP.ChassisType}
          touched={touched.ChassisType}
          formData={formData}
          onChange={handleChange}
          onBlur={handleBlur}
        />

        <FormField
          label="Update Channel"
          name="OSBranch"
          type="select"
          options={OPTIONS.OSBranch}
          helpText={FIELD_HELP.OSBranch}
          touched={touched.OSBranch}
          formData={formData}
          onChange={handleChange}
          onBlur={handleBlur}
        />

        {/* Security Settings Section */}
        <div className="form-section">
          <h3>Security Status</h3>
        </div>

        <FormField
          label="Defender Version"
          name="AppVersion"
          type="select"
          options={OPTIONS.AppVersion}
          helpText={FIELD_HELP.AppVersion}
          touched={touched.AppVersion}
          formData={formData}
          onChange={handleChange}
          onBlur={handleBlur}
        />

        <FormField
          label="Is Protection On?"
          name="IsSystemProtected"
          type="boolean"
          helpText={FIELD_HELP.IsSystemProtected}
          required
          touched={touched.IsSystemProtected}
          formData={formData}
          onChange={handleChange}
          onBlur={handleBlur}
        />

        <FormField
          label="Passive Mode?"
          name="IsPassiveModeEnabled"
          type="boolean"
          helpText={FIELD_HELP.IsPassiveModeEnabled}
          touched={touched.IsPassiveModeEnabled}
          formData={formData}
          onChange={handleChange}
          onBlur={handleBlur}
        />

        <FormField
          label="Antivirus Config"
          name="AntivirusConfigID"
          type="select"
          options={OPTIONS.AntivirusConfigID}
          helpText={FIELD_HELP.AntivirusConfigID}
          touched={touched.AntivirusConfigID}
          formData={formData}
          onChange={handleChange}
          onBlur={handleBlur}
        />

        <FormField
          label="Is Firewall On?"
          name="FirewallEnabled"
          type="boolean"
          helpText={FIELD_HELP.FirewallEnabled}
          required
          touched={touched.FirewallEnabled}
          formData={formData}
          onChange={handleChange}
          onBlur={handleBlur}
        />

        <FormField
          label="Configuration Issue?"
          name="AV_Imbalance"
          type="boolean"
          helpText={FIELD_HELP.AV_Imbalance}
          touched={touched.AV_Imbalance}
          formData={formData}
          onChange={handleChange}
          onBlur={handleBlur}
        />

        {/* Update Status Section */}
        <div className="form-section">
          <h3>Updates</h3>
        </div>

        <FormField
          label="Days Since Virus Signature Update"
          name="SignatureAgeDays"
          type="number"
          min={RANGES.SignatureAgeDays.min}
          max={RANGES.SignatureAgeDays.max}
          placeholder="0 - 840"
          helpText={FIELD_HELP.SignatureAgeDays}
          required
          touched={touched.SignatureAgeDays}
          formData={formData}
          onChange={handleChange}
          onBlur={handleBlur}
        />

        <FormField
          label="Days Since Last Update"
          name="OSUpdateAgeDays"
          type="number"
          min={RANGES.OSUpdateAgeDays.min}
          max={RANGES.OSUpdateAgeDays.max}
          placeholder="0 - 1175"
          helpText={FIELD_HELP.OSUpdateAgeDays}
          required
          touched={touched.OSUpdateAgeDays}
          formData={formData}
          onChange={handleChange}
          onBlur={handleBlur}
        />

        <button type="submit" className="submit-btn" disabled={loading}>
          {loading ? "Analyzing..." : "Analyze Threat"}
        </button>
      </form>

      {error && <div className="error-message">{error}</div>}

      {prediction && (
        <div
          className={`prediction-result ${getRiskLevel(prediction.probability_1).className}`}
        >
          <h3>Prediction Result</h3>
          <div className="risk-display">
            <span className="risk-label">Risk Level:</span>
            <span
              className={`risk-value ${getRiskLevel(prediction.probability_1).className}`}
            >
              {getRiskLevel(prediction.probability_1).level}
            </span>
          </div>
          <div className="probability-display">
            <span className="probability-label">Threat Probability:</span>
            <span className="probability-value">
              {(prediction.probability_1 * 100).toFixed(1)}%
            </span>
          </div>
          <div className="probability-bar">
            <div
              className="probability-fill"
              style={{ width: `${prediction.probability_1 * 100}%` }}
            />
          </div>
          <div className="warning-banner">
            ⚠️ This is a student project. The predictions may not be accurate.
          </div>
          <button
            type="button"
            className="back-btn"
            onClick={() => navigate("/")}
          >
            Back to Main Menu
          </button>
        </div>
      )}
    </div>
  );
};

export default ThreatForm;

import "./Working.css";

const Working = () => (
  <section id="learn-more" className="working-section">
    <h1>About System Threat Forecaster</h1>
    <div className="working-grid">
      <div className="project">
        <h2>Why it matters</h2>
        <p>
          Proactively forecast malware risk before it strikes. Help your team
          prioritize fixes and close security gaps faster.
        </p>
      </div>
      <div className="data">
        <h2>The data</h2>
        <p>
          Anonymized telemetry from 60,000+ endpoints worldwide, combined with
          curated threat indicators, drives accurate risk scoring.
        </p>
      </div>
      <div className="features">
        <h2>How it works</h2>
        <p>
          Twelve critical features feed a trained ML model to score device risk
          in seconds and highlight likely attack vectors.
        </p>
      </div>
      <div className="impact">
        <h2>What you get</h2>
        <p>
          Earlier detection, fewer incidents, focused patching, and clear,
          actionable insights that keep systems resilient.
        </p>
      </div>
    </div>
  </section>
);

export default Working;

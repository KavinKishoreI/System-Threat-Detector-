import connection from "../dbConfig/config.js";

const addPc = async (
  userName,
  pcName,
  processorCoreCount,
  processor,
  SKUEditionName,
  OSEdition,
  OSBuildNumber,
  ChassisType,
  AppVersion,
  IsSystemProtected,
  IsPassiveModeEnabled,
  AntivirusConfigID,
  FirewallEnabled,
  OSBranch,
  AV_Imbalance,
  SignatureAgeDays,
  OSUpdateAgeDays,
  FirewallWithoutProtection,
  prediction,
  infection_probability,
) => {
  const insertQuery = `
    INSERT INTO system_threat_features (
      user_name,
      pc_name,
      ProcessorCoreCount,
      Processor,
      SKUEditionName,
      OSEdition,
      OSBuildNumber,
      ChassisType,
      AppVersion,
      IsSystemProtected,
      IsPassiveModeEnabled,
      AntivirusConfigID,
      FirewallEnabled,
      OSBranch,
      AV_Imbalance,
      SignatureAgeDays,
      OSUpdateAgeDays,
      FirewallWithoutProtection,
      prediction,
      infection_probability
    ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
  `;

  try {
    await connection.query(insertQuery, [
      userName,
      pcName,
      processorCoreCount,
      processor,
      SKUEditionName,
      OSEdition,
      OSBuildNumber,
      ChassisType,
      AppVersion,
      IsSystemProtected,
      IsPassiveModeEnabled,
      AntivirusConfigID,
      FirewallEnabled,
      OSBranch,
      AV_Imbalance,
      SignatureAgeDays,
      OSUpdateAgeDays,
      FirewallWithoutProtection,
      prediction,
      infection_probability,
    ]);
    console.log("System:", pcName, "added successfully for user:", userName);
    return { message: "System added successfully", status: 201 };
  } catch (e) {
    console.error("DB Insert Error:", e);
    return { message: "Database error", status: 500 };
  }
};

const getSystems = async (userName) => {
  const query = ` SELECT * FROM system_threat_features WHERE user_name = ?`;
  try {
    const [rows] = await connection.query(query, [userName]);
    return { systems: rows, status: 200 };
  } catch (e) {
    console.error("DB Fetch Error:", e);
    return { message: "Database error", status: 500 };
  }
};

export { addPc, getSystems };

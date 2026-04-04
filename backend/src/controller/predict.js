import { addPc } from "../model/addSystem.js";

const predict = async (request, response) => {
  const {
    userName,
    pcName,
    ProcessorCoreCount = null,
    Processor = null,
    SKUEditionName = null,
    OSEdition = null,
    OSBuildNumber = null,
    ChassisType = null,
    AppVersion = null,
    IsSystemProtected = null,
    IsPassiveModeEnabled = null,
    AntivirusConfigID = null,
    FirewallEnabled = null,
    OSBranch = null,
    AV_Imbalance = null,
    SignatureAgeDays = null,
    OSUpdateAgeDays = null,
    FirewallWithoutProtection = null,
  } = request.body;

  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${process.env.ML_SECRET_KEY} `,
    },
    body: JSON.stringify({
      Processor,
      ProcessorCoreCount,
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
    }),
  };
  try {
    const predictionRequest = await fetch(
      "http://localhost:8000/health",
      options,
    );
    if (!predictionRequest.ok) {
      return response.status(422).send({
        message: "Invalid Prediction request",
      });
    } else {
      const predictions = await predictionRequest.json();
      response.status(201).send(predictions);
      try {
        const dbInsert = await addPc(
          userName,
          pcName,
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
          predictions.prediction,
          predictions.probability_1,
        );

        console.log(dbInsert);
      } catch (e) {
        console.log("error inserting system. ");
        console.log(e);
        return response
          .status(500)
          .send({ message: "DB server error TRY AGAIN LATER" });
      }
    }
  } catch (e) {
    console.log("ML SERVER error ");
    console.log(e);
    return response
      .status(500)
      .send({ message: "ML server error TRY AGAIN LATER" });
  }
};

export { predict };

import { predict } from "../controller/predict.js";
import { authToken } from "../controller/auth.js";
import { getPcs } from "../controller/getPcs.js";
import express from "express";

const predictRouter = express.Router();

predictRouter.use(authToken);
predictRouter.post("/predict", predict);
predictRouter.get("/getpcs", getPcs);
export default predictRouter;

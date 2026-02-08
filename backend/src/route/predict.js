import { predict } from "../controller/predict.js";
import { authToken } from "../controller/auth.js";
import express from "express";

const predictRouter = express.Router();

predictRouter.use(authToken);
predictRouter.post("/predict", predict);

export default predictRouter;

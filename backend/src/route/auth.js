import { apiAuth, login, register } from "../controller/auth.js";
import express from "express";

const authRoutes = express.Router();
authRoutes.use(express.json());
authRoutes.post("/login/", login);
authRoutes.post("/register/", register);
authRoutes.get("/tokenAuth/", apiAuth);
export default authRoutes;

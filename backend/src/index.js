import connection from "./dbConfig/config.js";
import authRoutes from "./route/auth.js";
import express from "express";
import cors from "cors";

const server = express();
server.use(cors({ origin: "http://localhost:5173" }));
if (connection != null) {
  server.listen(3000, () => {
    console.log("Server started in port 3000");
  });
} else {
  console.log("error");
}

server.use(authRoutes);

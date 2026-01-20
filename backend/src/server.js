import connection from "./dbConfig/config.js";
import express from "express";

const server = express();
if (connection != null) {
  server.listen(3000, () => {
    console.log("Server started in port 3000");
  });
} else {
  console.log("error");
}

import { getSystems } from "../model/addSystem.js";

const getPcs = async (request, response) => {
  const { userName } = request.body;
  const result = await getSystems(userName);
  return response.status(result.status).json(result);
};

export { getPcs };

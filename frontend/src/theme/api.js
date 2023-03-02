import axios from "axios";

export const enviarDatos = async (data) => {
  try {
    const response = await axios.post("/profile/", data);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

import axios from "axios";

export const getEmployeeProfiles = async () => {
  try {
    const response = await axios.get(
      "http://localhost:8000/bitacora/employees/"
    );
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
};

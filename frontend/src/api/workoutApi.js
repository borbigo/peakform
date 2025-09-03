import axios from "axios";

// make axios instance
const api = axios.create({
  baseURL: "/",
});

// fetch all workouts
export const fetchWorkouts = async () => {
  const response = await api.get("/workouts");
  return response.data;
};

// add a new workout
export const addWorkout = async (workout) => {
  const response = await api.post("/workouts", workout);
  return response.data;
};

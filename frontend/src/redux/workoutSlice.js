import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  list: [],
};

export const workoutSlice = createSlice({
  name: 'workouts',
  initialState,
  reducers: {
    setWorkouts: (state, action) => {
      state.list = action.payload;
    },
    addWorkout: (state, action) => {
      state.list.push(action.payload);
    },
  },
});

export const { setWorkouts, addWorkout } = workoutSlice.actions;
export default workoutSlice.reducer;
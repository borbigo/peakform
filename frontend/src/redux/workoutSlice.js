import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { fetchWorkouts, addWorkout } from '../api/workoutApi';

// Thunks - type of action creator that returns a function instead of a plain action object
// allows asynchronous logic and side effects to be performed before ultimately dispatching a regular action to the Redux store
export const getWorkouts = createAsyncThunk("workouts/get", async () => {
  return await fetchWorkouts();
});

export const createWorkout = createAsyncThunk("workouts/create", async (workout) => {
  return await addWorkout(workout);
})

export const workoutSlice = createSlice({
  name: 'workouts',
  initialState: {
    items: [],
    status: 'idle',
  },
  reducers: {
    setWorkouts: (state, action) => {
      state.items = action.payload;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(getWorkouts.pending, (state) => {
        state.status = "loading";
      })
      .addCase(getWorkouts.fulfilled, (state, action) => {
        state.status = "success";
        state.items = action.payload;
      })
      .addCase(createWorkout.fulfilled, (state, action) => {
        state.items.push(action.payload);
      });
  },
});

export const { setWorkouts } = workoutSlice.actions;
export default workoutSlice.reducer;
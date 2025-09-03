import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { fetchWorkouts, addWorkout } from '../api/workoutApi';
import axios from 'axios';

// Thunks - type of action creator that returns a function instead of a plain action object
// allows asynchronous logic and side effects to be performed before ultimately dispatching a regular action to the Redux store
export const getWorkouts = createAsyncThunk(
  "workouts/getWorkouts", 
  async () => {
    const response = await axios.get('http://localhost:5000/workouts');
    return response.data;
  }
);

export const createWorkout = createAsyncThunk(
  "workouts/create", 
  async (workout) => {
    return await addWorkout(workout);
  }
);

export const deleteWorkout = createAsyncThunk(
  "workouts/deleteWorkout", 
  async(id) => {
    await axios.delete(`http://127.0.0.1:5000/workouts/${id}`);
    return id;
  }
);

export const workoutSlice = createSlice({
  name: 'workouts',
  initialState: {
    items: [],
    status: 'idle',
    error: null,
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
      .addCase(getWorkouts.rejected, (state, action) => {
        state.status = 'failed';
        state.error = action.error.message;
      })
      .addCase(createWorkout.fulfilled, (state, action) => {
        state.items.push(action.payload);
      })
      .addCase(deleteWorkout.fulfilled, (state, action) => {
        state.items = state.items.filter((w) => w.id !== action.payload);
      });
  },
});

export const { setWorkouts } = workoutSlice.actions;
export default workoutSlice.reducer;
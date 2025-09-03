import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { setWorkouts } from './redux/workoutSlice';
import WorkoutList from './components/WorkoutList';
import WorkoutForm from './components/WorkoutForm';

function App() {
  const dispatch = useDispatch();
  const workouts = useSelector(state => state.workouts.list);

  useEffect(() => {
    // Temporary test data
    dispatch(setWorkouts([
      { id: 1, name: 'Morning Run', date: '2025-09-02' },
      { id: 2, name: 'Evening Bike', date: '2025-09-02' }
    ]));
  }, [dispatch]);

  return (
    <div>
      <h1>PeakForm Workouts</h1>
      <WorkoutForm />
      <WorkoutList />
    </div>
  );
}

export default App;

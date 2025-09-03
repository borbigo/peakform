import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getWorkouts } from '../redux/workoutSlice';

export default function WorkoutList() {
  const dispatch = useDispatch(); // send "actions" to the store
  const workouts = useSelector((state) => state.workouts.items); //receives the entire Redux state as input and returns the desired portion of the state
  const status = useSelector((state) => state.workouts.status);

  useEffect(() => {
    dispatch(getWorkouts());
  }, [dispatch]);

  if (status === 'loading') return <p>Loading...</p>;

  return (
    <div>
      <h2>Workouts</h2>
      <ul>
        {workouts.map((w) => (
          <li key={w.id}>
            {w.name} - {w.date}
          </li>
        ))}
      </ul>
    </div>
  );
}
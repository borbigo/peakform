import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { createWorkout } from '../redux/workoutSlice';

function WorkoutForm() {
  const [name, setName] = useState("");
  const [date, setDate] = useState("");
  const dispatch = useDispatch();

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!name || !date) return;

    dispatch(createWorkout({ name, date }));
    setName("");
    setDate("");
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginTop: '20px' }}>
      <input
        type='text'
        placeholder='Workout Name'
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <input
        type='date'
        value={date}
        onChange={(e) => setDate(e.target.value)}
      />
      <button type='submit'>Add Workout</button>
    </form>
  );
}

export default WorkoutForm;
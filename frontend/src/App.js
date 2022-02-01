import './App.css';
import React from 'react';
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Challenge from './Challenge.jsx';
import Swiper from './Swiper.jsx';

//Time to send reminders
//Start and end dates of challenge (or just the number of days)
//Items (checklist)


//<Button variant="contained">Submit</Button>

function App() {
  return (
    <div className="App">
        <Swiper />
    </div>
  );
}

export default App;

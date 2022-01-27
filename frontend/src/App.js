import logo from './logo.svg';
import './App.css';
import React from 'react';
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Challenge from './Challenge.jsx';

//Time to send reminders
//Start and end dates of challenge (or just the number of days)
//Items (checklist)


function App() {
  return (
    <div className="App">
      <body>
        <h1> ula </h1>
        <Challenge />
        <Button variant="contained">Submit</Button>
      </body>
    </div>
  );
}

export default App;

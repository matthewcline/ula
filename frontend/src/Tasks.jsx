import React from 'react';

import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Task from './Task';

function Tasks(props) {
  return (
    <div style={{display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
        <Task />
    </div>
  );
}

export default Tasks;
import React from 'react';

import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Task from './Task';

function Challenge() {
  return (
    <Box
      component="form"
      sx={{
        '& .MuiTextField-root': { m: 1, width: '25ch' },
      }}
      noValidate
      autoComplete="off"
    >
      <div>
        <TextField id="outlined-basic" label="Challenge Title" variant="outlined" />
      </div>
      <div>
        <TextField id="outlined-basic" label="Challenge Title" variant="outlined" />
      </div>
      <div>
        <Task />
      </div>
    </Box>
  );
}

export default Challenge;
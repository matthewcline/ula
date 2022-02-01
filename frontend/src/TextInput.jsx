import React from 'react';

import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Task from './Task';

function TextInput(props) {
  return (
    <Box
      component="form"
      sx={{
        '& .MuiTextField-root': { m: 1, width: '35ch' },
      }}
      noValidate
      autoComplete="off"
      className={'challenge'}
    >
      <div>
        <TextField id="outlined-basic" label={props.label} variant="outlined" />
      </div>
    </Box>
  );
}

export default TextInput;
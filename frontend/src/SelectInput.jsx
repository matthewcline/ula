import * as React from 'react';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import TextInput from './TextInput';

{/* <MenuItem value={':white_check_mark:'}>✅</MenuItem> */}
{/* <MenuItem value={':nerd_face:'}>🤓</MenuItem> */}
{/* <MenuItem value={':muscle:'}>💪</MenuItem> */}
{/* <MenuItem value={':droplet:'}>💧</MenuItem> */}

export default function SelectInput() {
  const [emoji, setEmoji] = React.useState('yes');

  const handleChange = (event) => {
    console.log("set emoji")
    setEmoji(event.target.value);
  };

  const handleOpen = () => {
    console.log("opened!")
  };

  return (
    <Box sx={{ minWidth: 100 }} style={{flex: 1}}>
      <FormControl fullWidth>
        <InputLabel id="demo-simple-select-label">Emoji</InputLabel>
        <Select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          value={emoji}
          label="Emoji"
          onChange={handleChange}
          onOpen={handleOpen}
        >
          <MenuItem value={'yes'}>yes</MenuItem>
          <MenuItem value={'no'}>no</MenuItem>
        </Select>
      </FormControl>
    </Box>
  );
}
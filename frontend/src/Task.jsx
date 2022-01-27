import * as React from 'react';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';

export default function BasicSelect() {
  const [emoji, setEmoji] = React.useState('');

  const handleChange = (event) => {
    setEmoji(event.target.value);
  };

  return (
    <Box sx={{ minWidth: 120 }}>
      <FormControl fullWidth>
        <InputLabel id="demo-simple-select-label">Emoji</InputLabel>
        <Select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          value={emoji}
          label="Emoji"
          onChange={handleChange}
        >
          <MenuItem value={':white_check_mark:'}>✅</MenuItem>
          <MenuItem value={':nerd_face:'}>🤓</MenuItem>
          <MenuItem value={':muscle:'}>💪</MenuItem>
          <MenuItem value={':droplet:'}>💧</MenuItem>
        </Select>
      </FormControl>
    </Box>
  );
}
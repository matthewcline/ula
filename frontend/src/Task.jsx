import * as React from 'react';
// import Box from '@mui/material/Box';
// import InputLabel from '@mui/material/InputLabel';
// import MenuItem from '@mui/material/MenuItem';
// import FormControl from '@mui/material/FormControl';
// import Select from '@mui/material/Select';
import TextInput from './TextInput';

import SelectInput from './SelectInput';

export default function Task() {
  const [emoji, setEmoji] = React.useState('');

  const handleChange = (event) => {
    setEmoji(event.target.value);
  };

  return (
     <div style={{display: 'flex', flexDirection: 'row', alignItems: 'center'}}>
        <SelectInput />
        <TextInput style={{flex: 1}} label={"Task"}/>
      </div>
  );
}
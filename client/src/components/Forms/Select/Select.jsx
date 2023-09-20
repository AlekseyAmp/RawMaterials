import React, { useState } from 'react';

import { options } from '../../../constants/date';

function Select({ onSelect }) {
  const [selectedMonthYear, setSelectedMonthYear] = useState('');

  const handleChange = (e) => {
    const value = e.target.value;
    setSelectedMonthYear(value);
    onSelect(value);
  };

  return (
    <div>
      <h3 className={`dark-text`}>Выбрать месяц</h3>
      <select value={selectedMonthYear} onChange={handleChange}>
        {options}
      </select>
    </div>
  );
}

export default Select;

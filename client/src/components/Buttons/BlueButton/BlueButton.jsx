import React from 'react';

import styles from './BlueButton.module.scss';

function BlueButton({title, onClick}) {
  return (
    <div onClick={onClick} className={styles.bluebutton}>
      <button>
        {title}
      </button>
    </div>
  )
}

export default BlueButton;
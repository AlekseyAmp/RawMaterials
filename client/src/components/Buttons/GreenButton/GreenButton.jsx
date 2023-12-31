import React from 'react';

import styles from './GreenButton.module.scss';

function GreenButton({title, onClick}) {
  return (
    <div onClick={onClick} className={styles.greenbutton}>
      <button>
        {title}
      </button>
    </div>
  )
}

export default GreenButton;
import React from 'react';

import styles from './Input.module.scss';

function Input({ title, type, name, value }) {
    return (
        <div className={styles.input}>
            <label htmlFor={name} className={`dark-text`}>{title}</label>

            <input
                type={type}
                name={name}
                value={value}
            />

        </div>
    )
}

export default Input;
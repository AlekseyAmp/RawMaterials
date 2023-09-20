import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

import { access_token } from '../../constants/token';
import { getUserInfo } from '../../services/user';

import styles from './Header.module.scss';

import Logout from '../Buttons/Logout/Logout';

function Header() {
    const isAuthorized = !!access_token;
    const [name, setName] = useState('');
    const [surname, setSurname] = useState('');
    const [login, setLogin] = useState('');
    const [role, setRole] = useState('');

    useEffect(() => {
        if (isAuthorized) {
            getUserInfo()
                .then((data) => {
                    setName(data.name);
                    setSurname(data.surname);
                    setLogin(data.login);
                    setRole(data.role);
                })
                .catch((error) => console.log(error));
        }
    }, [isAuthorized]);

    return (
        <div className={styles.header}>
            <Link to='/home' className={styles.logo}>
                <h3 className={`title`}>Raw Material Indicator</h3>
            </Link>
            {/* 
      <div className={styles.menu}>
        <ul>
          <li>
            <Link to='/' className={`link-text`}></Link>
          </li>
        </ul>
      </div> */}

            <div className={styles.menu}>
                <ul>
                    {isAuthorized ? (
                        <>
                            <li>
                                <p className={`gray-text`}>{name} {surname}</p>
                            </li>
                            <div className={`column`}>
                                <li>
                                    <p className={`dark-text`}>Роль - <span className={`green-text`}>{role}</span></p>
                                </li>
                                <li>
                                    <p className={`dark-text`}>Логин - <span className={`blue-text`}>{login}</span></p>
                                </li>
                            </div>
                            <li>
                                <Logout />
                            </li>
                        </>
                    ) : (
                        <>
                            <li>
                                <Link to='/login' className={`link-text`}>Вход</Link>
                            </li>
                        </>
                    )}
                </ul>
            </div>
        </div>
    );
}

export default Header;

import axios from '../utils/axios';
import Cookies from 'js-cookie';


export async function login_user(login, password, setError, setShowError, navigate) {
  try {
    const response = await axios.post('/auth/login', { login, password });

    if (response.data) {
      Cookies.set('access_token', response.data.access_token);
      Cookies.set('refresh_token', response.data.refresh_token);
      navigate('/home')
      window.location.reload();
    }
  } catch (error) {
    const errorMessage = error.response.data.detail;
    setError(errorMessage);
    setShowError(true);
    setTimeout(() => {
      setShowError(false);
      setError(null);
    }, 2500);
  }
}


export async function logout_user(setError, setShowError, navigate) {
  try {
    const response = await axios.get('/auth/logout');

    if (response.data) {
      Cookies.remove('access_token');
      Cookies.remove('refresh_token');
      navigate('/login');
      window.location.reload();
    }
  } catch (error) {
    const errorMessage = error.response.data.detail;
    setError(errorMessage);
    setShowError(true);
    setTimeout(() => {
      setShowError(false);
      setError(null);
    }, 2500);
  }
}


export async function refresh_token() {
  try {
    const response = await axios.get('/auth/refresh_token');

    if (response.data && response.data.access_token) {
      const access_token = response.data.access_token;
      const expirationTimeInMinutes = 60;
      const expirationDate = new Date(new Date().getTime() + expirationTimeInMinutes * 60000);
      Cookies.set('access_token', access_token, { expires: expirationDate });
    }
  } catch (error) {
    console.log(error.response.data.detail);
  }
}



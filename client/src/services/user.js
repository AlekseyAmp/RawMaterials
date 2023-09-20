import axios from '../utils/axios';

export async function getUserInfo() {
    try {
        const response = await axios.get(`/users/me`);

        if (response.data) {
           return response.data;
        }
    } catch (error) {
        console.log(error.response.data.detail);
    }
}

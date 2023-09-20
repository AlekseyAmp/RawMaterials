import axios from "../utils/axios";


export async function getDataFromExcel(year, month) {
    try {
        const response = await axios.get(`/materials/excel?year=${year}&month=${month}`);

        if (response.data) {
            return response.data;
        }
    } catch (error) {
        console.log(error.response.data.detail);
    }
}

export async function getReport(year, month) {
    try {
        const response = await axios.get(`/materials/report?year=${year}&month=${month}`);

        if (response.data) {
            return response.data;
        }
    } catch (error) {
        console.log(error.response.data.detail);
    }
}


export async function addNewRow(material_name, iron_content, silicion_content, aluminum_content, calcium_content, sulphur_content) {
    try {
        const response = await axios.post('/materials/add', { material_name, iron_content, silicion_content, aluminum_content, calcium_content, sulphur_content });

        if (response.data) {
            window.location.reload();
            console.log(response.data);
        }
    } catch (error) {
        console.log(error.response.data.detail);
    }
}
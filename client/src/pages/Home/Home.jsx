import React, { useState, useEffect } from 'react';

import { access_token } from '../../constants/token';
import { currentYear, currentMonth } from '../../constants/date';

import { getDataFromExcel, getReport, addNewRow } from '../../services/material';

import Form from '../../components/Forms/Form/Form';
import Select from '../../components/Forms/Select/Select';
import GreenButton from '../../components/Buttons/GreenButton/GreenButton';
import BlueButton from '../../components/Buttons/BlueButton/BlueButton';

function Home() {
  const isAuthorized = access_token;
  const [data, setData] = useState([]);
  const [selectedYear, setSelectedYear] = useState(currentYear);
  const [selectedMonth, setSelectedMonth] = useState(currentMonth);
  const [showReport, setShowReport] = useState(false);
  const [report, setReport] = useState([]);
  const [showForm, setShowForm] = useState(false);

  const inputConfigs = [
    { title: "Название железнорудного концентрата", type: 'text', name: 'material_name' },
    { title: "Содержание железа", type: 'text', name: 'iron_content' },
    { title: "Содержание кремния", type: 'text', name: 'silicion_content' },
    { title: "Содержание алюминия", type: 'text', name: 'aluminum_content' },
    { title: "Содержание кальция", type: 'text', name: 'calcium_content' },
    { title: "Содержание серы", type: 'text', name: 'sulphur_content' },
  ]

  const handleSelect = async (selectedValue) => {
    const [month, year] = selectedValue.split('.');
    const formattedMonth = month.padStart(2, '0');
    setSelectedYear(year);
    setSelectedMonth(formattedMonth);

    if (isAuthorized) {
      await getDataFromExcel(selectedYear, selectedMonth)
        .then((data) => {
          setData(data);
        })
        .catch((error) => console.log(error));
    }
  };

  const handleReport = async (e) => {
    if (isAuthorized) {
      await getReport(selectedYear, selectedMonth)
        .then((data) => {
          setReport(data);
          setShowReport(true);
        })
        .catch((error) => console.log(error));
    }
  };

  const handleAddRow = async (e) => {
    e.preventDefault();
    const material_name = e.target.material_name.value;
    const iron_content = e.target.iron_content.value;
    const silicion_content = e.target.silicion_content.value;
    const aluminum_content = e.target.aluminum_content.value;
    const calcium_content = e.target.calcium_content.value;
    const sulphur_content = e.target.sulphur_content.value;
    await addNewRow(material_name, iron_content, silicion_content, aluminum_content, calcium_content, sulphur_content)
  };

  const handleShowForm = () => {
    setShowForm(true);
  }

  useEffect(() => {
    if (isAuthorized) {
      getDataFromExcel(selectedYear, selectedMonth)
        .then((data) => {
          setData(data);
        })
        .catch((error) => console.log(error));
    }
  }, [isAuthorized, selectedYear, selectedMonth]);
  return (
    <div>
      {isAuthorized ? (
        <div className={`center`}>
          {showForm ? (
            <Form
              inputConfigs={inputConfigs}
              buttonTitle='Сохранить'
              onSubmit={handleAddRow}
            />
          ) : (
            <div>
              <h3 className={`bold-text mt50px center`}>Данные на {selectedMonth} {selectedYear}</h3>
              <Select onSelect={handleSelect} />
              <table className={`mt50px`}>
                <thead className={`bold-text`}>
                  <tr>
                    <th>Номер</th>
                    <th>Дата добавления</th>
                    <th>Название железнорудного концетрата</th>
                    <th>Содержание железа</th>
                    <th>Содержание кремния</th>
                    <th>Содержание алюминия</th>
                    <th>Содержание кальция</th>
                    <th>Содержание серы</th>
                  </tr>
                </thead>
                <tbody>
                  {data.map((item) => (
                    <tr key={item.number} className={`small-text`}>
                      <td>{item.number}</td>
                      <td>{item.added_date}</td>
                      <td>{item.material_name}</td>
                      <td>{item.iron_content}</td>
                      <td>{item.silicion_content}</td>
                      <td>{item.aluminum_content}</td>
                      <td>{item.calcium_content}</td>
                      <td>{item.sulphur_content}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
              {report && showReport && (
                <div>
                  <h3 className={`bold-text mt50px center`}>Отчет</h3>
                  <table className={`mt50px`}>
                    <thead className={`bold-text`}>
                      <tr>
                        <th>Номер</th>
                        <th>Дата добавления</th>
                        <th>Название железнорудного концетрата</th>
                        <th>Максимальное значение</th>
                        <th>Среднее значение</th>
                        <th>Минимальное значение</th>
                      </tr>
                    </thead>
                    <tbody>
                      {report.map((item) => (
                        <tr key={item.number} className={`small-text`}>
                          <td>{item.number}</td>
                          <td>{item.added_date}</td>
                          <td>{item.material_name}</td>
                          <td>{item.max_value}</td>
                          <td>{item.avg_value}</td>
                          <td>{item.min_value}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              )}
              <div className={`buttons`}>
                <BlueButton
                  title={`Сформировать отчёт за ${selectedMonth} ${selectedYear}`}
                  onClick={handleReport}
                />
                <GreenButton
                  title={"Добавить запись в таблицу"}
                  onClick={handleShowForm}
                />
              </div>
            </div>
          )}
        </div>
      ) : (
        <p className={`title center`}>Нет доступа</p>
      )}
    </div>
  );

}

export default Home;

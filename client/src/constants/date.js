const months = [
    "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
    "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
  ];
const options = [];

const currentDate = new Date();
const startYear = 2000;
const currentYear = currentDate.getFullYear();
const currentMonth = (currentDate.getMonth() + 1).toString().padStart(2, '0');

for (let year = currentYear; year >= startYear; year--) {
  for (let monthIndex = 0; monthIndex < 12; monthIndex++) {
    const month = months[monthIndex]
    const value = `${monthIndex+1}.${year}`;
    const label = `${month} ${year}`;
    options.push(<option key={label} value={value}>{label}</option>);
  }
}

export { currentYear, currentMonth, options }
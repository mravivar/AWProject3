export default function () {
  axios.get(`${API_BASE_URL}/questions`)
  .then((res) => {
    this.questions = res.data.questions;
  });
}
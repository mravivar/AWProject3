export default function (text, code) {
  let title = this.question.title;
  axios.post(`${API_BASE_URL}/answer`, {title, text, code})
  .then (res => {
    this.answers.push(res.data);
  });
}
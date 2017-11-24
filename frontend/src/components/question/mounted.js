export default function  () {
  const id = this.$route.params.id;
  this.isLoading = true;
  axios.get(`${API_BASE_URL}/questions/${id}`)
    .then (res => {
    this.question = res.data.question;
    this.answers = res.data.answers;
    if (res.data.accepted_answer.user_id)
      this.acceptedAnswer = res.data.accepted_answer;
  }).finally( () => {
    this.isLoading = false;
  });
}
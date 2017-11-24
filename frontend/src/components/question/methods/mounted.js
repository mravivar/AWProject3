export default function  () {
  const id = this.$route.params.id;
  this.isLoading = true;
  axios.get(`${API_BASE_URL}/questions/${id}`)
  .then (res => {
    this.processResponse(res);
  }).finally( () => {
    this.isLoading = false;
  });
}
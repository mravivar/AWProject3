export default function  () {
  let url = `${API_BASE_URL}/questions`;
  if (this.page) 
    url += `?page=${this.page}`;
  axios.get(url)
    .then((res) => {
    this.questions = res.data.questions;
    if (res.data.page_context) {
      this.page = res.data.page_context.page;
      this.totalPages = res.data.page_context.total_pages;
    }
  });
}
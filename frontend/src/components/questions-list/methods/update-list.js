export default function (page) {
  let url = `${API_BASE_URL}/questions`;
  let self = this;
  if (!page) 
    page = 1;
  url += `?page=${page}`;
  axios.get(url)
  .then( function (res) {
    self.questions = res.data.questions;
    if (res.data.page_context) {
      self.page = res.data.page_context.page;
      self.totalPages = res.data.page_context.total_pages;
    }
  });
}
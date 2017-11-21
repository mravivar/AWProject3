import appendQueryParam from './append-query-param';

export default function (page, queryString) {
  let self = this;
  let url = `${API_BASE_URL}/questions`;
  
  if (!queryString)
    queryString = this.searchText;
  
  if (queryString && queryString.trim()) {
    queryString = queryString.trim();
    url = `${API_BASE_URL}/search`;
    url = appendQueryParam(url, 'query', queryString);
  }
  
  if (page)
  	url = appendQueryParam(url, 'page', page);
  
  this.isLoading = true;
  
  axios.get(url)
  .then( function (res) {
    self.questions = res.data.questions;
    if (res.data.page_context) {
      self.page = res.data.page_context.page;
      self.totalPages = res.data.page_context.total_pages;
    }
  }).finally( () => {
    this.isLoading = false;
  });
}
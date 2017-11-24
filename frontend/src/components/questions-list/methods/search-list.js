export default function () {
  let queryString = this.searchText;
  if (queryString && queryString.trim()) {
    this.updateList(1, queryString.trim());
  }
}
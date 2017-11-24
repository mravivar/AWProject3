export default function (id) {
  if (typeof id === 'object') {
    id = id.$oid;
  }
  let question_id = this.question._id;
  axios.post(`${API_BASE_URL}/upvote`, {id, question_id})
  	.then (res => {
    	this.processResponse(res);
  });
}
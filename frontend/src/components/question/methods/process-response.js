export default function (res) {
  this.question = res.data.question;
  this.answers = res.data.answers;
  if (res.data.accepted_answer.user_id)
    this.acceptedAnswer = res.data.accepted_answer;
}
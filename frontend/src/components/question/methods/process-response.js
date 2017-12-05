export default function (res) {
  this.question = res.data.question;
  this.answers = res.data.answers;
  this.recommendations = res.data.suggested_questions;
  this.currentUser = res.data.current_user;
  if (res.data.accepted_answer.user_id)
    this.acceptedAnswer = res.data.accepted_answer;
}
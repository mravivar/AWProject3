<template>
  <div class="container main-container">
    <div class="row">
      <div class="col-md-offset-2 col-md-8 col-sm-12" v-if="question">
        <h3>{{question.title}}</h3>
        <div class="tag-list">
          <div v-for="tag in question.tag" class="tag">{{tag}}</div>
        </div>
        <div class="item-box">
          <div class="vote-box">
            <a><span class="glyphicon glyphicon-thumbs-up"></span></a>
            <span class="vote-count">{{question.vote}}</span>
            <a><span class="glyphicon glyphicon-thumbs-down"></span></a>
          </div>
          <div class="item-inner-box">
            <div class="user-details">
              <span><strong>User ID:&nbsp; {{question.user_id}}</strong></span>
              <span class="reputation-tag">{{question.reputation}}</span>
              <span>Accept Rate:&nbsp; {{question.accept_rate}}</span>
              <div class="pull-right"><strong>Posted On {{question.time}}</strong></div>
            </div>
            <div class="item-content" v-html=question.content></div>
          </div>
        </div>
        <h3 v-if="acceptedAnswer" class="answers-count">Accepted Answer(s)</h3>
        <div v-if="acceptedAnswer" class="item-box">
          <div class="vote-box">
            <a><span class="glyphicon glyphicon-thumbs-up"></span></a>
            <span class="vote-count">{{acceptedAnswer.vote}}</span>
            <a><span class="glyphicon glyphicon-thumbs-down"></span></a>
          </div>
          <div class="item-inner-box">
            <div class="user-details">
              <span><strong>User ID:&nbsp; {{acceptedAnswer.user_id}}</strong></span>
              <span class="reputation-tag">{{acceptedAnswer.reputation}}</span>
              <span>Accept Rate:&nbsp; {{acceptedAnswer.accept_rate}}</span>
              <div class="pull-right"><strong>Posted On {{acceptedAnswer.time}}</strong></div>
            </div>
            <div class="item-content" v-html="acceptedAnswer.content"></div>
          </div>
          <hr>
        </div>
        <h3 class="answers-count">{{answers.length}} Answer(s)</h3>
        <div v-for="answer in answers" class="item-box">
          <div class="vote-box">
            <a><span class="glyphicon glyphicon-thumbs-up"></span></a>
            <span class="vote-count">{{answer.vote}}</span>
            <a><span class="glyphicon glyphicon-thumbs-down"></span></a>
          </div>
          <div class="item-inner-box">
            <div class="user-details">
              <span><strong>User ID:&nbsp; {{answer.user_id}}</strong></span>
              <span class="reputation-tag">{{answer.reputation}}</span>
              <span>Accept Rate:&nbsp; {{answer.accept_rate}}</span>
              <div class="pull-right"><strong>Posted On {{answer.time}}</strong></div>
            </div>
            <div class="item-content" v-html="answer.content"></div>
          </div>
          <hr>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
  @import 'src/assets/sass/home/index.scss';
</style>

<script>
export default {
  data () {
    return {
      question : null,
      answers: [],
      acceptedAnswer : null,
      isLoading : false
    }
  },
  mounted () {
    const id = this.$route.params.id;
    this.isLoading = true;
    axios.get(`${API_BASE_URL}/questions/${id}`)
    .then (res => {
      this.question = res.data.question;
//      let answers = res.data.answers.map((ans)=> {
//        ans.content = ans.content.replace(/\r\n|\n|\r/gm, '<br />');
//        return ans;
//      })
      this.answers = res.data.answers;
      this.acceptedAnswer = res.data.accepted_answer;
    }).finally( () => {
      this.isLoading = false;
    });
  }
}
</script>
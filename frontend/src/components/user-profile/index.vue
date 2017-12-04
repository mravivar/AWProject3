<template>
  <div class="container main-container">
    <div class="row">
      <div class="col-sm-12">
        <ul class="nav nav-tabs">
          <li role="presentation" class="active"><a href="#questions" data-toggle="tab">Questions</a></li>
          <li role="presentation"><a href="#answers" data-toggle="tab">Answers</a></li>
          <li role="presentation"><a href="#accepted_answers" data-toggle="tab">Accepted Answers</a></li>
          <li role="presentation"><a href="#graph" data-toggle="tab">Graph</a></li>
        </ul>
        <loading v-if="isLoading" />
        <div v-else class="tab-content">
          <div id="questions" class="tab-pane fade in active">
            <user-line-item :items="questions" />
          </div>
          <div id="answers" class="tab-pane fade">
            <user-line-item :items="answers" />
          </div>
          <div id="accepted_answers" class="tab-pane fade">  
            <user-line-item :items="accepted_answers" />
          </div>
          <div id="graph" class="tab-pane fade">  
            <graph :activity="activity" :range="range"></graph>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
  @import 'src/assets/sass/home/index.scss';
</style>

<script>
const moment = require('moment');

export default {
  data (){
    return {
      questions: [],
      answers: [],
      accepted_answers: [],
      activity: null,
      range: [],
      isLoading: false
    };
  },
  mounted () {
    this.isLoading = true;
    axios.get(`${API_BASE_URL}/userprofile`)
    .then(res => {
      let tuples = res.data.user_tuples;
      this.questions = tuples.filter(tuple => tuple.type === 'question');
      this.answers = tuples.filter(tuple => tuple.type === 'answer');
      this.accepted_answers = tuples.filter(tuple => tuple.type === 'accepted_answers');
      let _a = [];
      for (let e in res.data.activity) {
        _a.push({created_at: moment(e).format('YYYY-MM-DD'), counting: res.data.activity[e]});
      }
      console.log(_a);
      this.activity = _a;
    }).finally(()=>{
      this.isLoading = false;
    });
  }
}

</script>
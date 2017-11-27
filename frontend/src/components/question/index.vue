<template>
  <div class="container main-container">
    <div class="row">
      <div class="col-sm-12" v-if="question">
        <router-link to="/">Go back</router-link>
        <h3>{{question.title}}</h3>
        <div class="tag-list">
          <div v-for="tag in question.tag" class="tag">{{tag}}</div>
        </div>
        <line-item :item="question" @on-upvote='upvote'/>
        <h3 v-if="acceptedAnswer" class="answers-count">Accepted Answer(s)</h3>
        <line-item :item="acceptedAnswer" @on-upvote='upvote' />
        <h3 class="answers-count">{{answers.length}} Answer(s)</h3>
        <div v-for="answer in answers">
          <line-item :item="answer" @on-upvote='upvote' />
        </div>
        <add-answer @add-answer='addAnswer'/>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
  @import 'src/assets/sass/home/index.scss';
</style>

<script>
import mounted from './methods/mounted';
import data from './methods/data';
import processResponse from './methods/process-response';
import upvote from './methods/upvote';
import addAnswer from './methods/add-answer';
  
export default {
  data,
  mounted,
  methods: {
    upvote,
    processResponse,
    addAnswer
  }
}
</script>
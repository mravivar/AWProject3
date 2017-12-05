<template>
  <div class="container-fluid question-details">
    <loading v-if="isLoading"></loading>
    <div v-else class="question-container">
    <div class="row" v-if="question">
      <div class="col-sm-8">
        <a @click="goBack">Go back</a>
        <h3>{{question.title}}</h3>
        <div class="tag-list">
          <div v-for="tag in question.tag" class="tag">{{tag}}</div>
        </div>
        <line-item :item="question" @on-upvote='upvote'/>
        <h3 v-if="acceptedAnswer" class="answers-count">Accepted Answer(s)</h3>
        <line-item :item="acceptedAnswer" @on-upvote='upvote' />
        <h3 class="answers-count">{{answers.length}} Answer(s)</h3>
        <div v-for="answer in answers">
          <line-item :item="answer" @on-upvote='upvote' :canAccept="!acceptedAnswer" :owner="currentUser" @on-accept='acceptAnswer' />
        </div>
        <add-answer @add-answer='addAnswer'/>
      </div>
      <div class="col-sm-4" style="margin-top: 95px" v-if="recommendations">
        <h3>Suggested Questions</h3>
        <div class="row">
          <div class="col-sm-12 suggested-question" v-for="question in recommendations">
            <router-link :to="{name: 'question', params: { id: question.id}}">
              <div class="vote">
                <div class="count">{{question.stats.votes}}</div>
              </div>
              <div class="text"><strong>{{question.description}}</strong></div>
            </router-link>
          </div>
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
import mounted from './methods/mounted';
import data from './methods/data';
import processResponse from './methods/process-response';
import upvote from './methods/upvote';
import acceptAnswer from './methods/accept-answer';
import addAnswer from './methods/add-answer';
import goBack from '../../utils/go-back';
  
export default {
  data,
  mounted,
  methods: {
    upvote,
    processResponse,
    addAnswer,
    acceptAnswer,
    goBack
  }
}
</script>
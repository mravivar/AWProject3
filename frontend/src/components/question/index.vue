<template>
  <div class="container main-container">
    <div class="row">
      <div class="col-md-offset-2 col-md-8 col-sm-12" v-if="question">
        <h3>{{question.title}}</h3>
        <div class="tag-list">
          <div v-for="tag in question.tag" class="tag">{{tag}}</div>
        </div>
        <line-item :item="question" />
        <h3 v-if="acceptedAnswer" class="answers-count">Accepted Answer(s)</h3>
        <line-item :item="acceptedAnswer" />
        <h3 class="answers-count">{{answers.length}} Answer(s)</h3>
        <div v-for="answer in answers">
          <line-item :item="answer" />
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
  @import 'src/assets/sass/home/index.scss';
</style>

<script>
import mounted from './mounted';
import data from './data';
  
export default {
  data,
  mounted
}
</script>
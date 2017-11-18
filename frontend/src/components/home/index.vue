<template>
  <div class="container">
    <div class="row">
      <div class="col-md-offset-2 col-md-8 col-sm-12">
        <!--div class="list-actions"></div-->
        <div class="row questions-list-item" v-for="question in questions" :key="question.id">
          <div class="col-sm-7">
            <strong>{{question.description}}</strong>
          </div>
          <div class="col-sm-4 pull-right">
            <div class="stats text-center">
              <div><strong>{{question.stats.votes}}</strong></div>
              votes
            </div>
            <div class="stats text-center">
              <div><strong>{{question.stats.answer_count}}</strong></div>
              ans
            </div>
          </div>
        </div>
        <pagination/>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
@import 'src/assets/sass/home/index.scss';
</style>

<script>

import data from './methods/data';
import mounted from './methods/mounted';

export default {
  data,
  mounted
}

</script>
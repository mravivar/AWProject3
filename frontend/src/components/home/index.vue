<template>
  <div class="container">
    <div class="row">
      <div class="col-md-offset-2 col-md-8 col-sm-12">
        <!--div class="list-actions"></div-->
        <div class="row questions-list-item" v-for="question in questions" :key="question.id">
          <div class="col-sm-7">
            <div class="text"><strong>{{question.description}}</strong></div>
            <div class="tag-list">
              <a v-for="tag in question.tags" class="tag font-xs">{{tag}}</a>
            </div>
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
        <pagination v-if="showPagination" :totalPages="totalPages" :page="page" @page-change="updateList" />
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
import updateList from './methods/update-list';
import showPagination from './computed/show-pagination';

export default {
  data,
  mounted,
  computed: {
    showPagination
  },
  methods: {
    updateList
  }
}

</script>
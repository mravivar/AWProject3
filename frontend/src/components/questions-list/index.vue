<template>
  <div class="col-md-offset-2 col-md-8 col-sm-12">
    <div class="list-actions">
      <div class="pull-right">
        <router-link to="ask_question" class="btn btn-primary">Ask Question</router-link>
      </div>
      <div class="row">
        <div class="col-lg-9">
          <div class="input-group">
            <input type="text" class="form-control" placeholder="Search for..." v-model="searchText" @keyup.enter="searchList">
            <span class="input-group-btn">
              <button class="btn btn-default" type="button" @click="searchList">Go!</button>
            </span>
          </div>
        </div>
      </div>
    </div>
    <loading v-if="isLoading" />
    <div v-else>
      <div class="row questions-list-item" v-for="question in questions" :key="question.id">
        <div class="col-sm-8">
          <router-link :to="{name: 'question', params: { id: question.id}}"><div class="text"><strong>{{question.description}}  </strong></div></router-link>
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
</template>

<script>
  
import data from './methods/data';
import mounted from './methods/mounted';
import updateList from './methods/update-list';
import showPagination from './computed/show-pagination';
import searchList from './methods/search-list';

export default {
  data,
  mounted,
  computed: {
    showPagination
  },
  methods : {
    updateList,
    searchList
  }
}

</script>
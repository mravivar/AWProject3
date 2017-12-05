<template>
  <div v-if="items.length > 0">
    <div v-for="item in items">
      <router-link :to="{name: 'question', params: { id: item.id}}" tag="h3" class="cursor-pointer">{{item.title}}</router-link>
      <div class="tag-list">
        <div v-for="tag in item.tags" class="tag">{{tag}}</div>
      </div>
      <div class="item-box">
        <div class="vote-box">
          <a @click="$emit('on-upvote', item._id)" :disabled="true"><span class="glyphicon glyphicon-thumbs-up "></span></a>
          <span class="vote-count">{{item.vote}}</span>
        </div>
        <div class="item-inner-box">
          <div class="user-details">
            <div class="pull-right"><strong>Posted On {{item.time}}</strong></div>
          </div>
          <div class="item-content" v-html="sanitize(item.content)"></div>
        </div>
        <hr>
      </div>
    </div>
  </div>
  <div v-else class="jumbotron">
    Nothing found here!!
  </div>
</template>

<script>

import sanitize from '../../utils/sanitize';
  
export default {
  props: ['items'],
  methods: {
    sanitize
  }
}

</script>
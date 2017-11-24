<template>
  <div v-if="item" class="item-box">
    <div class="vote-box">
      <a @click="$emit('on-upvote', item._id)" :disabled="item.is_upvoted"><span class="glyphicon glyphicon-thumbs-up "></span></a>
      <span class="vote-count">{{item.vote}}</span>
      <!--a><span class="glyphicon glyphicon-thumbs-down"></span></a-->
    </div>
    <div class="item-inner-box">
      <div class="user-details">
        <span><strong>User ID:&nbsp; {{item.user_id}}</strong></span>
        <span class="reputation-tag">{{item.reputation}}</span>
        <span>Accept Rate:&nbsp; {{item.accept_rate}}</span>
        <div class="pull-right"><strong>Posted On {{item.time}}</strong></div>
      </div>
      <div class="item-content" v-html="item.content"></div>
    </div>
    <hr>
  </div>
</template>

<script>

export default {
  props: ['item']
}

</script>
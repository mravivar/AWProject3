<template>
  <div class="container main-container">
    <div class="row">
      <div class="col-md-offset-2 col-md-8 col-sm-12">
        <h3 v-if="question">{{question.description}}</h3>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      question : null
    }
  },
  mounted () {
    const id = this.$route.params.id;
    axios.get(`${API_BASE_URL}/questions/${id}`)
    .then (res => {
      this.question = res.data.question;
    });
  }
}
</script>
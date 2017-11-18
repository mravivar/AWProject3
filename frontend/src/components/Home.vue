<template>
  <div class="container">
    <p>Home page</p>
    <p v-if="sampleData">{{sampleData}}</p>
  </div>
</template>

<script>

export default {
  data () {
    return {
      sampleData: null
    }
  },
  mounted () {
    axios.get(`${API_BASE_URL}/list`)
    .then((res) => {
      this.sampleData = res.data;
    });
  }
}
</script>
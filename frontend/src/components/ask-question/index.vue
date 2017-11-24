<template>
  <div class="container main-container">
    <div class="col-md-offset-2 col-md-8 col-sm-12">
      <div class="row">
        <form action=''>
          <div class="form-group">
            <label for="title">Title</label>
            <input type="text" class="form-control" id="title" placeholder="Question title" v-model='title'>
            <p class="help-block">Question in one sentence</p>
          </div>
          <div class="form-group">
            <label for="description">Description</label>
            <textarea class="form-control" id="description" rows=10 v-model='description'></textarea>
          </div>
          <button type="submit" class="btn btn-primary" @click='askQuestion'>Submit</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      title: '',
      description: ''
    }
  },
  methods: {
    askQuestion () {
      let url = `${API_BASE_URL}/questions`;
      let data = {};
      data.title = this.title;
      data.content = this.description;
      axios.post(url, data)
      .then(res => {
        
      });
    }
  }
}
</script>
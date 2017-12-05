<template>
  <div class="container main-container">
    <div class="row">
      <div class="col-sm-12 form-group">
        <router-link to="/">Go back</router-link>
      </div>
    <div class="col-md-offset-2 col-md-8 col-sm-12">
      <div class="row">
        <form>
          <div class="form-group">
            <label for="title">Title</label>
            <input type="text" class="form-control" id="title" placeholder="Question title" v-model='title'>
            <p class="help-block">Question in one sentence</p>
          </div>
          <div class="form-group">
            <label for="description">Description</label>
            <textarea class="form-control" id="description" rows=5 v-model='description'></textarea>
            <p class="help-block">A detailed description of your question.</p>
          </div>
          <div class="form-group">
            <label for="description">Code</label>
            <textarea class="form-control" id="description" rows=5 v-model='code'></textarea>
            <p class="help-block">If your question has any code in it.</p>
          </div>
          <button type="submit" class="btn btn-primary" @click='askQuestion'>Submit</button>
        </form>
      </div>
    </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      title: '',
      description: '',
      code: ''
    }
  },
  methods: {
    askQuestion (e) {
      e.preventDefault();
      let url = `${API_BASE_URL}/questions`;
      let data = {};
      let self = this;
      data.title = this.title;
      data.text = this.description;
      data.code = this.code;
      axios.post(url, data)
      .then(res => {
        this.$router.push({ path: '/questions' });
      });
    }
  }
}
</script>
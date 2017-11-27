<template>
  <div>
    <div v-if="displayTextArea">
      <div class="row form-group item-box">
        <div class='col-sm-12'>
          <textarea v-model="text" rows='4' class='form-control' placeholder='Add the description of your answer'></textarea>
        </div>
      </div>
      <div class="row form-group item-box">
        <div class='col-sm-12'>
          <textarea v-model="code" rows='4' class='form-control' placeholder='If you want to write any code, do it here!'></textarea>
        </div>
      </div>
      <div class="row form-group">
        <div class='col-sm-12 btn-toolbar'>
          <button class='btn btn-primary' @click="addAnswer">Add Answer</button>
          <button class='btn btn-default' @click='toggleDisplay(false)'>Cancel</button>
        </div>
      </div>
    </div>
    <a v-else @click='toggleDisplay(true)'>Add Answer</a>
  </div>
</template>

<script>

export default {
  data () {
    return {
      displayTextArea: false,
      text: '',
      code: ''
    };
  },
  methods: {
    addAnswer() {
      this.$emit('add-answer', this.text, this.code);
      this.toggleDisplay(false);
    },
    toggleDisplay(isTrue) {
      this.displayTextArea = isTrue? true : false;
    }
  }
} 

</script>
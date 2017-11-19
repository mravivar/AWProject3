<template>
  <nav aria-label="Page navigation">
    <paginate :pageCount="totalPages" containerClass="pagination" ref="paginate" :pageRange="1" :clickHandler="onClick" />
  </nav>
</template>

<script>
Vue.component('paginate', require('vuejs-paginate'));

export default {
  props: ['page', 'totalPages'],
  watch: {
    page (newValue) {
      if (newValue)
        this.$refs.paginate.selected = newValue - 1;
    }
  },
  methods: {
    onClick (page) {
      this.$emit('page-change', page);
    }
  }
}

</script>
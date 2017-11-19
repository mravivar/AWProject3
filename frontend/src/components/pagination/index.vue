<template>
  <nav aria-label="Page navigation">
    <paginate :pageCount="totalPages" containerClass="pagination" ref="paginate" :pageRange="3" :clickHandler="onClick" />
  </nav>
</template>

<script>
Vue.component('paginate', require('vuejs-paginate'));

export default {
  props: ['page', 'totalPages'],
  methods: {
    onClick (page) {
      this.$emit('page-change', page);
    }
  }
}

</script>
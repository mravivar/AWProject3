<template>
  <div class="container-fluid">
    <heat-map :entries=activity :colorrange="range" :tooltipEnabled=true tooltipUnit="event"></heat-map>
  </div>
</template>

<script>
  
  export default {
    data() {
      return {
        range: ['#ebedf0', 'green'],
        entries: []
      };
    },
    
    props: ['activity']
  }

</script>
<template>
  <div align="center" class="loading">
    <div class="load-circle1"></div>
    <div class="load-circle2"></div>
    <div class="load-circle3"></div>
    <div class="load-circle4"></div>
    <div class="load-circle5"></div>
  </div>
</template>

<style scoped>
.loading {
  left: 0;
  right: 0;
  margin-top: 90px;
  height: 35px;
  position: relative;
}

.load-circle1, .load-circle2, .load-circle3, .load-circle4, .load-circle5 {
  width: 8px;
  height: 8px;
  background: grey;
  display: inline-block;
  border-radius: 20px;
  -webkit-animation: loader 1.5s infinite;
  animation: loader 1.5s infinite;
}
  
@-webkit-keyframes loader {
  from {
    opacity:1;
    -webkit-transform:scale(1);
    -ms-transform:scale(1);
    transform:scale(1)
  }
  to {
    opacity:.25;
    -webkit-transform:scale(.3);
    -ms-transform:scale(.3);
    transform:scale(.3)
  }
}
  
@keyframes loader {
  from {
    opacity:1;
    -webkit-transform:scale(1);
    -ms-transform:scale(1);
    transform:scale(1)
  }
  to {
    opacity:.25;
    -webkit-transform:scale(.3);
    -ms-transform:scale(.3);
    transform:scale(.3)
  }
}  

.load-circle2 {
  -webkit-animation-delay: .25s;
  animation-delay: .25s;
}

.load-circle3 {
  -webkit-animation-delay: .5s;
  animation-delay: .5s;
}
  
.load-circle4 {
  -webkit-animation-delay: .75s;
  animation-delay: .75s;
}
  
.load-circle5 {
  -webkit-animation-delay: 1s;
  animation-delay: 1s;
}
  
</style>
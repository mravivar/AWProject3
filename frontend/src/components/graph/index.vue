<template>
  <div class="container-fluid">
    <div class = "activity-chart">

      <h1>Activity Chart</h1>
      <div class = "key">
        <span>Less</span>
        <ul>
          <li class = "activity-four"></li>
          <li class = "activity-three"></li>
          <li class = "activity-two"></li>
          <li class = "activity"></li>
          <li class = "day-key"></li>
        </ul>
        <span>More</span>
      </div>
      <ol class = "days-of-week">
        <li>M</li>
        <li>W</li>
        <li>F</li>
      </ol>
      <div id = "month" class = "month"></div>
      <div id = "days" class = "days"></div>
    </div>
  </div>
</template>

<style>
  ol, li { padding: 0; margin: 0; list-style: none;}
  h1 { 
    font-size: 1.5em; 
    margin: 70px 42px;
  }

  .activity-chart, h1 {color: #525252;}
  .days li, .day-key { background: rgb(235, 237, 240); }
  .activity-chart {
    width: 100%; 
    height: 205px;
  }

  /*** day of week heading ***/

  .days-of-week {
    width: 15px;
    position: relative;
    float: left;
  }

  @-moz-document url-prefix() {
    .days-of-week { left: 23px; }
  }

  .days-of-week { font-size: 0.7em; }
  .days-of-week li:nth-child(2) { margin: 13px 0; }

  /*** month headings ***/

  .month ol {
    position: relative;
    top: -55px;
    float: left;
  }

  .month li {
    float: right;
    margin-left: 39px;
    font-size: 0.75em;
  }

  /*** draw days ***/

  .days { 
    font-size: 0.75em;
    margin-top: 15px;
    display: inline-block;
  }

  /* offset so days of the week line up
  over-specified to win specificity battle */
  .activity-chart .offset:hover { outline: none; }
  .activity-chart .offset { background: none; }

  /* create vertical weeks */
  .week { 
    width: 108px;
    transform: rotate(90deg);
  }

  .days li, .key li {
    width: 12px;
    height: 12px;
    float: right; /* order days starting at the bottom right */
  }

  .days .bold { font-weight: bold; }
  .days li {  margin: 1.5px; }

  /*** color-code by activity level ***/
  .activity-chart .activity { background: #d6e685; }
  .activity-chart .activity-two { background: #8cc665; }
  .activity-chart .activity-three { background: #44a340; }
  .activity-chart .activity-four { background: #1e6823; }

  .key {
    position: absolute;
    bottom: 0;
    right: 55px;
  }

  .key ul {
    display: inline-block; 
    margin: 0;
    padding: 0;
  }

  .key li {  margin: 0px 2px; }

  /*** tooltips ***/

  .days li .tooltip { display: none; }
  .days li:hover
  {  
    /*outline disabled due to firefox cross-broswer issue */
    /*outline: 1px solid #555;*/
    position: relative;
    z-index: 3;
  }

  .days li:hover .tooltip {
    transform: rotate(-90deg);
    display: block;
    position: absolute;
    /* top & left are reversed because the calendar is rotated 90 deg */
    top: -17px;
    left: -75px;
    width: 100px;
    padding: 10px 5px;
    text-align: center;
    background-color: #333; 
    color: #f1f1f1;
    opacity:1
  }

  /*** little triangle on the tooltip ***/
  .tooltip:before {
    content: "";
    position: absolute;
    width: 0; 
    height: 0; 

    bottom: -10px;
    right: 50px;

    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 11px solid #333;
  }

</style>

<script>

  const moment = require('moment');
  const d3 = require('d3-scale');

  export default {
    mounted () {
      
      const day_map = { // should be changed to accept the input from the API
        '01-02-17' : 20,
        '01-03-17' : 50,
        '01-04-17' : 100
      };
      
      const scale = d3.scaleLinear().domain([1,100])
        .range(['#ebedf0', 'green']);
      
      var month = moment();
      var outputMonth = "<ol class = 'month'>";
      for (let i = 0; i <= 12; i++) {
        var durationMonth = moment.duration({'months' : 1});
        outputMonth += "<li>";
        outputMonth += moment(month).format("MMM");
        outputMonth += "</li>";
        month = moment(month).subtract(durationMonth);
      }
      outputMonth += "</ol>";

      var output = "<ol><div class = 'week'>";
      var day = moment();      
      
      console.log(scale(1)+' ' + scale(100));

      /* Calculate the offset for days of the week to line up correctly */
      var dayOfWeekOffset = 6 - (parseInt(moment().format("d"),10));
      for (let i = 0; i < (dayOfWeekOffset); i++) { output += "<li class = 'offset'></li>"; }

      /*** draw calendar ***/

      for (let i = 365; i >= 0; i--) {
        let date = moment(day).format("MM-DD-YY");
        let val = day_map[date];
        let color = val ? scale(val) : '#ebedf0';
        output += `<li style='background-color:${color}'>`;
        output += '<span class = "tooltip">' + date;
        if (val){
         output+= ' - ' + val
        }
        output += '</span>';
        output += "</li>";

        var duration = moment.duration({'days' : 1});
        day = moment(day).subtract(duration);
      }

      output += "</div></ol>";
      document.getElementById("month").innerHTML = outputMonth;
      document.getElementById("days").innerHTML = output;
    }
  }

</script>
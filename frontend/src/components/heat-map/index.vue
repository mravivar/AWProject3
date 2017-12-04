<template>
<div class="heatmap-container"></div>
</template>

<script>
import moment from 'moment'
import _ from 'lodash'
import * as d3 from 'd3'
import HeatMap from 'vuejs-heatmap/src/App.vue' 
import {calendarHeatmap} from 'vuejs-heatmap/src/calendar-heatmap.js'
  
export default {
  extends: HeatMap,
  props: ['tooltipUnit'],
  methods: {
    initHeatMap() {
      let entries = this.entries;
        if(!entries) {
          entries = [{"id":391,"counting":2070,"created_at":"2017-06-21"},{"id":875,"counting":3493,"created_at":"2017-06-22"},{"id":1381,"counting":3207,"created_at":"2017-06-23"},{"id":1896,"counting":3199,"created_at":"2017-06-24"},{"id":2416,"counting":3121,"created_at":"2017-06-25"}]
        }
        let colorrange = this.colorrange;
        if(!colorrange) {
          colorrange = ['#c9ecec', '#09b3af']
        }
        let tooltipEnabled = this.tooltipEnabled;
        if(!tooltipEnabled) {
          tooltipEnabled = true
        }
        let tooltipUnit = this.tooltipUnit;
        if(!tooltipUnit) {
          tooltipUnit = 'API Request';
        }
        let now = moment().endOf('day').toDate();
        let yearAgo = moment().startOf('day').subtract(1, 'year').toDate();
        
        let chartData = d3.time.days(yearAgo, now).map((dateElement) => {
          return {
            date: dateElement,
            count: ((dateElement) => {
              let heatmapEntry = _.find(entries, {created_at: moment(dateElement).format('YYYY-MM-DD')})
              if(!heatmapEntry) {
                return 0;
              } else {
                return heatmapEntry.counting
              }
            })(dateElement)
          };
        });
        let heatmap = calendarHeatmap.init()
                    .data(chartData)
                    .selector('.heatmap-container')
                    .tooltipEnabled(tooltipEnabled)
                    .colorRange(colorrange)
                    .tooltipUnit(tooltipUnit)
        heatmap();  // render the chart
    }
  }
}
</script>
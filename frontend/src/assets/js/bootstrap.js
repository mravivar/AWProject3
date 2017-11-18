window.axios = require('axios');
window.API_BASE_URL = 'http://localhost:5000/api';

require('babel-polyfill');

import Vue from 'vue'

window.Vue = Vue

window.$ = window.jQuery = require('jquery');

require('bootstrap-sass');

<template>
  <nav id='navbar' class="navbar navbar-default navbar-static-top">
      <div class="container">
        <div class="navbar-header">

          <!-- Collapsed Hamburger -->
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#app-navbar-collapse">
            <span class="sr-only">Toggle Navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>

          <!-- Branding Image -->
          <router-link class="navbar-brand" to="/">Q/A Forum</router-link>
        </div>

        <div class="collapse navbar-collapse" id="app-navbar-collapse">
          <ul class="nav navbar-nav navbar-right">
            <li><router-link to="/" exact>Home</router-link></li>
            <li><router-link to="/user_profile">Profile</router-link></li>
            <li><a href="/logout">Logout</a></li>
        </ul>
      </div>
    </div>
  </nav>
</template>
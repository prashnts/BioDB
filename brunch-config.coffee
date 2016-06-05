# BioDB

module.exports = config:
  paths:
    watched: ['biodb']

  plugins:
    autoReload:
      enabled: yes
    coffeelint:
      pattern: /^biodb\/.*\.(coffee)$/
      useCoffeelintJson: yes
    jaded:
      staticPatterns: /^biodb\/markup\/([\d\w]*)\.jade$/
    postcss:
      processors: [
        require('autoprefixer')(['last 8 versions'])
      ]
    stylus:
      plugins: [
        'jeet'
        'bootstrap-styl'
      ]

  npm:
    enabled: yes
    styles:
      'normalize.css': [
        'normalize.css'
      ]

  modules:
    nameCleaner: (path) ->
      path
        .replace /^biodb\//, ''
        .replace /\.coffee/, ''

  files:
    javascripts:
      joinTo:
        'js/libraries.js': /^(?!biodb\/)/
        'js/app.js': /^biodb\//
    stylesheets:
      joinTo:
        'css/libraries.css': /^(?!biodb\/)/
        'css/app.css': /^biodb\//

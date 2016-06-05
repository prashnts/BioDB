# BioDB
React     = require 'react'
ReactDOM  = require 'react-dom'

CardsContainer = require './cardscontainer'

App =
  init: ->
    doc = <CardsContainer/>
    ReactDOM.render doc, document.getElementById('main')


module.exports = App

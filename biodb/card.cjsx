# BioDB
React  = require 'react'
jquery = require 'jquery'


class Card extends React.Component
  constructor: (props) ->
    super props
    {@title, @description, @url, @reference} = props.dat

  render: ->
    <div className='card'>
      <h3>{@title}</h3>
      <p>{@description}</p>
      <h5>Source and reference</h5>
      <a href={@url} target="_blank">Source</a>
      <p>{@reference}</p>
    </div>



module.exports = Card

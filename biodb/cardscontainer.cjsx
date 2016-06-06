# BioDB
React  = require 'react'
jquery = require 'jquery'

ReactPaginate = require 'react-paginate'

Card = require './card'


class CardsContainer extends React.Component
  constructor: (props) ->
    super props
    @state =
      events: []
      pageCount: 0

  componentDidMount: ->
    @fetchCards()

  fetchCards: (pageno = 1) ->
    @setState events: []
    jquery.ajax(
      url: 'api/v1/software'
      method: 'GET'
      data: page: pageno
    ).done (dat) =>
      @setState
        events: dat.data
        pageCount: dat.paginate.total_pages

  renderCards: ->
    @state.events.map (dat, i) ->
      <Card key={dat.id} dat={dat} />

  handlePaginate: (data) =>
    @fetchCards(data.selected + 1)

  render: ->
    <div>
      <section className='search'>
        <span>BioDB</span>
        <div className='input-group'>
          <input type='text' className='form-control'></input>
          <span className='input-group-btn'>
            <button className='btn'>Search</button>
          </span>
        </div>
      </section>
      <div className='cards'>{@renderCards()}</div>
      <ReactPaginate
        previousLabel={"previous"}
        nextLabel={"next"}
        pageNum={@state.pageCount}
        marginPagesDisplayed={2}
        pageRangeDisplayed={5}
        clickCallback={@handlePaginate}
        containerClassName={"pagination"}
        subContainerClassName={"pages pagination"}
        activeClassName={"active"} />
    </div>



module.exports = CardsContainer

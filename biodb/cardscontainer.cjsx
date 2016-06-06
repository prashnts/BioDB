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
    @query =
      page: 1
      q: undefined

  componentDidMount: ->
    @fetchCards()

  fetchCards: ->
    @setState events: []
    jquery.ajax(
      url: 'api/v1/software'
      method: 'GET'
      data: @query
    ).done (dat) =>
      @setState
        events: dat.data
        pageCount: dat.paginate.total_pages

  renderCards: ->
    @state.events.map (dat, i) ->
      <Card key={dat.id} dat={dat} />

  handlePaginate: (data) =>
    @query.page = data.selected + 1
    @fetchCards()

  handleSubmit: (e) =>
    e.preventDefault()
    @query =
      page: 1
      q: @refs.searchq.value
    @fetchCards()

  render: ->
    <div>
      <section className='brand'>
        <span className='logo'>BioDB</span>
        <div className='search'>
          <form onSubmit={@handleSubmit}>
            <div className='input-group'>
              <input type='text' className='form-control' name='q' ref='searchq'/>
              <span className='input-group-btn'>
                <button className='btn' type='submit'>Search</button>
              </span>
            </div>
          </form>
        </div>
      </section>
      <div className='cards'>
        {@renderCards()}
      </div>
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

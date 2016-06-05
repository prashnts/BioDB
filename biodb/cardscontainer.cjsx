# BioDB
React  = require 'react'
jquery = require 'jquery'

ReactPaginate = require 'react-paginate'


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
      <div key={dat.id}>
        <p>{dat.title}</p>
      </div>

  handlePaginate: (data) =>
    @fetchCards(data.selected + 1)

  render: ->
    <div>
      <div className='pages'>{@renderCards()}</div>
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

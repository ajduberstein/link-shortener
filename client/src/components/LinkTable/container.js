import React from 'React'
import PropTypes from 'prop-types'
import { connect } from 'react-redux'

import { postLink } from '../../actions'

import Display from './display'

class Container extends React.Component {
  render () {
    return (
      <Display
        {...this.props}
      />)
  }
}


Container.propTypes = {
  links: PropTypes.array.isRequired
}


const mapStateToProps = (state) => {
  const {
   availableUrls 
  } = state.apiInteraction

  return {
    availableUrls
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    handleAddLink: (link) => {
      dispatch(postLink(link))
    }
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(Container)

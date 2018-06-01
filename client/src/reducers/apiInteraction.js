const apiState = {
  availableUrls: []
}

const apiInteraction = (state = apiState, action) => {
  switch (action.type) {
    case 'FETCH_DATA_SUCCESS':
      return {
        ...state,
        availableUrls: action.payload.availableUrls
      }
    case 'POST_LINK_BEGIN':
      return {
        ...state,
        postingLink: true
      }
    case 'POST_LINK_SUCCESS':
      return {
        ...state,
        postingLink: false
      }
    case 'POST_LINK_FAILURE':
      return {
        ...state,
        postingLink: false,
        error: action.error
      }

    default:
      return state
  }
}

export {
  apiInteraction
}

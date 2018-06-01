const uiState = {
  availableUrls: []
}

// TODO currently filler
const uiInteraction = (state = uiState, action) => {
  switch (action.type) {
    case 'FETCH_DATA_SUCCESS':
      return {
        ...state,
        availableUrls: action.payload.availableUrls
      }
    default:
      return state
  }
}

export {
  uiInteraction
}


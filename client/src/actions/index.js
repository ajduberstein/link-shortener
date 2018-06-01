// Data layer actions
export const fetchDataBegin = () => ({
  type: 'FETCH_DATA_BEGIN'
})

export const fetchDataSuccess = (availableUrls) => ({
  type: 'FETCH_DATA_SUCCESS',
  payload: {
    availableUrls
  }
})

export const fetchDataFailure = (error) => ({
  type: 'FETCH_DATA_FAILURE',
  payload: { error }
})

import { combineReducers } from 'redux'
import { apiInteraction } from './apiInteraction'
import { uiInteraction } from './uiInteraction'

const rootReducer = combineReducers({
  apiInteraction,
  uiInteraction,
})

export {
  rootReducer
}


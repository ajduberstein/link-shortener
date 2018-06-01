import * as actions from './index'


const requestJsonPromise = (url) => {
  return new Promise((resolve, reject) => {
    fetch(url).then(resp => {
      return resp.json()
    }).then(
      data => resolve(data)).catch(
      err => console.error(err)
    )
  })
}

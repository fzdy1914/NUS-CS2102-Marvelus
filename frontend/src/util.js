function getDate (timestamp) {
  return new Date(timestamp * 1000).toLocaleDateString()
}

function parse (candidate) {
  if (candidate && typeof (candidate) === 'string') {
    return parseInt(candidate)
  }
  return candidate
}

function generateArray (start, end) {
  return Array.from(new Array(end + 1).keys()).slice(start)
}

export default {
  getDate,
  parse,
  generateArray
}

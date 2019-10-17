import JsEncrypt from 'jsencrypt'

function getDate (timestamp) {
  return new Date(parse(timestamp)).toLocaleDateString()
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

function encrypt (password) {
  // eslint-disable-next-line
  let encryptor = new JSEncrypt()

  encryptor.setPublicKey('-----BEGIN PUBLIC KEY-----\n' +
   'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQClKNC9Gyk0K2d3x1XnJhsNQOm4\n' +
   'pqem0UmElIH6rvUSHmbx9R1SHZSLqE7biTcYhkU8gYe0+fIBeExt/qW4L6IbEB3X\n' +
   'G/Xv0rarK18vCNulkD43eDaeJZPOIdy3nItXiBIpNQxEu8MiOtqTIPeGIcueIOP0\n' +
   'C3+HeIZFiKPSZMoteQIDAQAB\n' +
   '-----END PUBLIC KEY-----')

  return encryptor.encrypt(password)
}

export default {
  getDate,
  parse,
  generateArray,
  encrypt
}

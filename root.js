const { ethers } = require('ethers')
const { MerkleTree } = require('merkletreejs')
const { keccak256 } = ethers//.utils
const fs = require('fs')

const args = process.argv.slice(2)
let csv_path = args[0]

fs.readFile(csv_path, 'utf8', (err, data) => {

  // load wl from file, filter for remove last empty row
  let whitelist = data.split('\n').map(r => r.split(',')[0].trim()).filter(r => r)
  console.log('total:', whitelist.length)

  // get tree
  let leaves = whitelist.map((addr) => keccak256(addr))
  let tree = new MerkleTree(leaves, keccak256, { sortPairs: true })
  let root = tree.getHexRoot()
  console.log('root:', root)

})
